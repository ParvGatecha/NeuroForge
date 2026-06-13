"use server";

import { dbService } from "@/shared/lib/db-service";
import { prisma } from "@/shared/lib/prisma";
import fs from "fs";
import path from "path";

export async function getCurrentUserAction(userId = "dev-user-id") {
  return await dbService.getCurrentUser(userId);
}

export async function getCompletedLearningItemsAction(userId = "dev-user-id") {
  return await dbService.getCompletedLearningItems(userId);
}

export async function getDetailedProgressAction(userId = "dev-user-id") {
  return await dbService.getDetailedProgress(userId);
}

export async function getBookmarksAction(userId = "dev-user-id") {
  return await dbService.getBookmarks(userId);
}

export async function toggleBookmarkAction(learningItemId: number, userId = "dev-user-id") {
  return await dbService.toggleBookmark(userId, learningItemId);
}

export async function completeLearningItemAction(
  learningItemId: number,
  xpReward: number,
  userId = "dev-user-id"
) {
  return await dbService.completeLearningItem(userId, learningItemId, xpReward);
}

export async function uncompleteLearningItemAction(
  learningItemId: number,
  userId = "dev-user-id"
) {
  return await dbService.uncompleteLearningItem(userId, learningItemId);
}

export async function getSettingsAction(userId = "dev-user-id") {
  return await dbService.getSettings(userId);
}

export async function updateSettingsAction(data: any, userId = "dev-user-id") {
  return await dbService.updateSettings(userId, data);
}

export async function getStreakAction(userId = "dev-user-id") {
  return await dbService.getStreak(userId);
}

export async function getUserAchievementsAction(userId = "dev-user-id") {
  return await dbService.getUserAchievements(userId);
}

export async function rebuildSearchIndexAction() {
  const contentDir = path.join(process.cwd(), "content");
  const outputFile = path.join(process.cwd(), "content/search_index.json");

  function getFilesRecursively(dir: string): string[] {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    const files = entries.map((entry) => {
      const res = path.resolve(dir, entry.name);
      return entry.isDirectory() ? getFilesRecursively(res) : res;
    });
    return Array.prototype.concat(...files);
  }

  if (!fs.existsSync(contentDir)) {
    return { success: false, error: "Content directory not found" };
  }

  const allFiles = getFilesRecursively(contentDir);
  const jsonFiles = allFiles.filter(
    (f) =>
      f.endsWith(".json") &&
      !f.includes("index.json") &&
      !f.includes("roadmap.json") &&
      !f.includes("search_index.json") &&
      !f.includes("local_mock_db.json")
  );

  const searchIndex: any[] = [];

  jsonFiles.forEach((filePath) => {
    try {
      const fileContent = fs.readFileSync(filePath, "utf-8");
      const q = JSON.parse(fileContent);

      searchIndex.push({
        id: q.id,
        slug: q.slug,
        title: q.title,
        section: q.section,
        difficulty: q.difficulty,
        theory_resource: q.theory_resource,
        practice_resource: q.practice_resource,
        estimated_time_minutes: q.estimated_time_minutes,
        tags: q.tags,
        learning_objectives: q.learning_objectives,
        description: q.description,
        prerequisites: q.prerequisites
      });
    } catch (e) {
      console.error(`Error indexing file: ${filePath}`, e);
    }
  });

  searchIndex.sort((a, b) => a.id - b.id);
  fs.writeFileSync(outputFile, JSON.stringify(searchIndex, null, 2), "utf-8");
  return { success: true, count: searchIndex.length };
}

export async function resetUserProgressAction(userId = "dev-user-id") {
  try {
    await prisma.$queryRaw`SELECT 1`;

    await prisma.learningItemProgress.deleteMany({ where: { userId } });
    await prisma.bookmark.deleteMany({ where: { userId } });
    await prisma.userAchievement.deleteMany({ where: { userId } });
    await prisma.streak.upsert({
      where: { userId },
      update: { currentCount: 0, longestCount: 0, lastActive: null },
      create: { userId, currentCount: 0, longestCount: 0, lastActive: null },
    });
    await prisma.user.update({
      where: { id: userId },
      data: { xp: 0, level: 1 },
    });
    return { success: true, dbMode: "postgres" };
  } catch (e) {
    // Fallback to mock DB file
  }

  const MOCK_DB_PATH = path.join(process.cwd(), "content/local_mock_db.json");
  if (fs.existsSync(MOCK_DB_PATH)) {
    const content = fs.readFileSync(MOCK_DB_PATH, "utf-8");
    const dbData = JSON.parse(content);

    dbData.progress = dbData.progress.filter((p: any) => p.userId !== userId);
    dbData.bookmarks = dbData.bookmarks.filter((b: any) => b.userId !== userId);
    dbData.userAchievements = dbData.userAchievements.filter((ua: any) => ua.userId !== userId);

    const streak = dbData.streaks.find((s: any) => s.userId === userId);
    if (streak) {
      streak.currentCount = 0;
      streak.longestCount = 0;
      streak.lastActive = null;
    }

    const user = dbData.users.find((u: any) => u.id === userId);
    if (user) {
      user.xp = 0;
      user.level = 1;
    }

    fs.writeFileSync(MOCK_DB_PATH, JSON.stringify(dbData, null, 2), "utf-8");
    return { success: true, dbMode: "file-mock" };
  }

  return { success: false, error: "Mock database not found" };
}

export async function isDatabaseConnectedAction() {
  try {
    await prisma.$queryRaw`SELECT 1`;
    return true;
  } catch (e) {
    return false;
  }
}

export async function saveLearningItemAction(item: any) {
  const baseDir = path.join(process.cwd(), "content");
  const sectionSlug = item.section.toLowerCase().replace(/\s+/g, "-");
  const sectionDir = path.join(baseDir, sectionSlug);
  
  if (!fs.existsSync(sectionDir)) {
    fs.mkdirSync(sectionDir, { recursive: true });
  }
  
  const formattedItem = {
    id: Number(item.id),
    slug: item.slug,
    title: item.title,
    section: item.section,
    difficulty: item.difficulty,
    theory_resource: item.theory_resource ? {
      title: item.theory_resource.title,
      url: item.theory_resource.url,
      type: item.theory_resource.type
    } : {
      title: `Theory: ${item.title}`,
      url: item.external_url || "https://google.com",
      type: item.resource_type || "article"
    },
    practice_resource: item.practice_resource ? {
      platform: item.practice_resource.platform,
      title: item.practice_resource.title,
      url: item.practice_resource.url
    } : {
      platform: "EXTERNAL",
      title: `Practice: ${item.title}`,
      url: item.external_url || "https://google.com"
    },
    estimated_time_minutes: Number(item.estimated_time_minutes),
    tags: Array.isArray(item.tags)
      ? item.tags
      : String(item.tags).split(",").map(t => t.trim()).filter(Boolean),
    learning_objectives: Array.isArray(item.learning_objectives)
      ? item.learning_objectives
      : String(item.learning_objectives).split(",").map(o => o.trim()).filter(Boolean),
    description: item.description,
    prerequisites: Array.isArray(item.prerequisites)
      ? item.prerequisites.map(Number)
      : String(item.prerequisites).split(",").map(p => Number(p.trim())).filter(p => !isNaN(p))
  };
  
  const file_name = `${String(formattedItem.id).padStart(3, "0")}-${formattedItem.slug}.json`;
  
  const sections = ["python", "statistics", "machine-learning", "deep-learning", "llm", "rag", "agents", "system-design"];
  sections.forEach((sec) => {
    const dir = path.join(baseDir, sec);
    if (fs.existsSync(dir)) {
      const files = fs.readdirSync(dir);
      files.forEach((f) => {
        if (f.startsWith(`${String(formattedItem.id).padStart(3, "0")}-`)) {
          try {
            fs.unlinkSync(path.join(dir, f));
          } catch (err) {
            console.error(`Error deleting older file: ${f}`, err);
          }
        }
      });
    }
  });
  
  const file_path = path.join(sectionDir, file_name);
  fs.writeFileSync(file_path, JSON.stringify(formattedItem, null, 2), "utf-8");
  
  await rebuildSearchIndexAction();
  return { success: true };
}

export async function deleteLearningItemAction(itemId: number) {
  const baseDir = path.join(process.cwd(), "content");
  const sections = ["python", "statistics", "machine-learning", "deep-learning", "llm", "rag", "agents", "system-design"];
  let deleted = false;
  
  sections.forEach((sec) => {
    const dir = path.join(baseDir, sec);
    if (fs.existsSync(dir)) {
      const files = fs.readdirSync(dir);
      files.forEach((f) => {
        if (f.startsWith(`${String(itemId).padStart(3, "0")}-`)) {
          try {
            fs.unlinkSync(path.join(dir, f));
            deleted = true;
          } catch (err) {
            console.error(`Error deleting file: ${f}`, err);
          }
        }
      });
    }
  });
  
  if (deleted) {
    await rebuildSearchIndexAction();
  }
  return { success: deleted };
}

export async function bulkImportAction(itemsJson: string) {
  try {
    const items = JSON.parse(itemsJson);
    const importList = Array.isArray(items) ? items : [items];
    
    for (const item of importList) {
      if (!item.id || !item.slug || !item.title || !item.section) {
        return { success: false, error: `Invalid item schema format: ${JSON.stringify(item)}` };
      }
      await saveLearningItemAction(item);
    }
    
    return { success: true, count: importList.length };
  } catch (e: any) {
    return { success: false, error: e.message || "Invalid JSON syntax" };
  }
}
