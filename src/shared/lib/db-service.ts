import { prisma } from "./prisma";
import fs from "fs";
import path from "path";
import { getLevelFromXp } from "@/modules/progress/xp";

const MOCK_DB_PATH = path.join(process.cwd(), "content/local_mock_db.json");

// Define interface for local mock DB structure
interface MockUser {
  id: string;
  name: string | null;
  email: string;
  role: "USER" | "ADMIN";
  xp: number;
  level: number;
  createdAt: string;
}

interface MockLearningItemProgress {
  id: string;
  userId: string;
  learningItemId: number;
  completedAt: string;
  xpEarned: number;
}

interface MockBookmark {
  id: string;
  userId: string;
  learningItemId: number;
  createdAt: string;
}

interface MockStreak {
  id: string;
  userId: string;
  currentCount: number;
  longestCount: number;
  lastActive: string | null;
}

interface MockUserAchievement {
  id: string;
  userId: string;
  achievementCode: string;
  unlockedAt: string;
}

interface MockSettings {
  id: string;
  userId: string;
  theme: string;
  emailNotifications: boolean;
  marketingEmails: boolean;
  publicProfile: boolean;
}

interface MockDatabase {
  users: MockUser[];
  progress: MockLearningItemProgress[];
  bookmarks: MockBookmark[];
  streaks: MockStreak[];
  userAchievements: MockUserAchievement[];
  settings: MockSettings[];
}

const DEFAULT_MOCK_DB: MockDatabase = {
  users: [
    {
      id: "dev-user-id",
      name: "Alex AI",
      email: "alex@neuroforge.ai",
      role: "ADMIN",
      xp: 120,
      level: 2,
      createdAt: new Date().toISOString(),
    },
  ],
  progress: [],
  bookmarks: [],
  streaks: [
    {
      id: "dev-streak-id",
      userId: "dev-user-id",
      currentCount: 2,
      longestCount: 5,
      lastActive: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(), // active yesterday
    },
  ],
  userAchievements: [
    {
      id: "dev-ach-id",
      userId: "dev-user-id",
      achievementCode: "FIRST_QUESTION",
      unlockedAt: new Date().toISOString(),
    },
  ],
  settings: [
    {
      id: "dev-settings-id",
      userId: "dev-user-id",
      theme: "dark",
      emailNotifications: true,
      marketingEmails: false,
      publicProfile: true,
    },
  ],
};

function readMockDb(): MockDatabase {
  try {
    if (!fs.existsSync(MOCK_DB_PATH)) {
      // Create directories if not exists
      const dir = path.dirname(MOCK_DB_PATH);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
      fs.writeFileSync(MOCK_DB_PATH, JSON.stringify(DEFAULT_MOCK_DB, null, 2), "utf-8");
      return DEFAULT_MOCK_DB;
    }
    const content = fs.readFileSync(MOCK_DB_PATH, "utf-8");
    return JSON.parse(content);
  } catch (e) {
    console.error("Error reading mock DB file, returning default mock", e);
    return DEFAULT_MOCK_DB;
  }
}

function writeMockDb(dbData: MockDatabase) {
  try {
    const dir = path.dirname(MOCK_DB_PATH);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    fs.writeFileSync(MOCK_DB_PATH, JSON.stringify(dbData, null, 2), "utf-8");
  } catch (e) {
    console.error("Error writing mock DB file", e);
  }
}

// Global flag to track if Postgres is reachable
let isPostgresAvailable = true;

async function checkDbConnection(): Promise<boolean> {
  try {
    await prisma.$queryRaw`SELECT 1`;
    isPostgresAvailable = true;
    return true;
  } catch (e) {
    if (isPostgresAvailable) {
      console.warn("⚠️ PostgreSQL Database not reachable. Falling back to local file-based mock database.");
      isPostgresAvailable = false;
    }
    return false;
  }
}

export const dbService = {
  /**
   * Get active user session details
   */
  async getCurrentUser(customUserId?: string): Promise<MockUser> {
    const activeUserId = customUserId || "dev-user-id";
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        let user = await prisma.user.findUnique({
          where: { id: activeUserId },
        });

        if (!user) {
          // Auto create user in DB if not exists (for seamless dev experience)
          user = await prisma.user.create({
            data: {
              id: activeUserId,
              name: "Alex AI",
              email: "alex@neuroforge.ai",
              role: "ADMIN",
              xp: 120,
              level: 2,
            },
          });
          // Also create default settings and streak
          await prisma.userSettings.create({
            data: { userId: activeUserId, theme: "dark" },
          });
          await prisma.streak.create({
            data: { userId: activeUserId, currentCount: 2, longestCount: 5, lastActive: new Date(Date.now() - 24 * 60 * 60 * 1000) },
          });
        }
        return {
          id: user.id,
          name: user.name,
          email: user.email,
          role: user.role,
          xp: user.xp,
          level: user.level,
          createdAt: user.createdAt.toISOString(),
        };
      } catch (e) {
        console.error("Prisma error in getCurrentUser, falling back to mock DB", e);
      }
    }

    // Fallback mode
    const dbData = readMockDb();
    let user = dbData.users.find((u) => u.id === activeUserId);
    if (!user) {
      user = {
        id: activeUserId,
        name: "Alex AI",
        email: "alex@neuroforge.ai",
        role: "ADMIN",
        xp: 120,
        level: 2,
        createdAt: new Date().toISOString(),
      };
      dbData.users.push(user);
      writeMockDb(dbData);
    }
    return user;
  },

  /**
   * Get all completed learning items
   */
  async getCompletedLearningItems(userId: string): Promise<number[]> {
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        const progressList = await prisma.learningItemProgress.findMany({
          where: { userId },
          select: { learningItemId: true },
        });
        return progressList.map((p) => p.learningItemId);
      } catch (e) {
        console.error("Prisma error in getCompletedLearningItems", e);
      }
    }

    const dbData = readMockDb();
    return dbData.progress
      .filter((p) => p.userId === userId)
      .map((p) => p.learningItemId);
  },

  /**
   * Get detailed progress with timestamps
   */
  async getDetailedProgress(userId: string): Promise<any[]> {
    const dbConnected = await checkDbConnection();
    if (dbConnected) {
      try {
        const progressList = await prisma.learningItemProgress.findMany({
          where: { userId },
          orderBy: { completedAt: "desc" },
        });
        return progressList.map((p) => ({
          learningItemId: p.learningItemId,
          completedAt: p.completedAt.toISOString(),
          xpEarned: p.xpEarned,
        }));
      } catch (e) {
        console.error("Prisma error in getDetailedProgress", e);
      }
    }
    const dbData = readMockDb();
    return dbData.progress
      .filter((p) => p.userId === userId)
      .map((p) => ({
        learningItemId: p.learningItemId,
        completedAt: p.completedAt,
        xpEarned: p.xpEarned,
      }))
      .sort((a, b) => new Date(b.completedAt).getTime() - new Date(a.completedAt).getTime());
  },

  /**
   * Mark a learning item completed
   */
  async completeLearningItem(
    userId: string,
    learningItemId: number,
    xpReward: number
  ): Promise<{ xpEarned: number; levelUp: boolean; newAchievements: any[] }> {
    const dbConnected = await checkDbConnection();
    let oldXp = 0;
    let newXp = 0;
    let oldLevel = 1;
    let newLevel = 1;
    let newAchievements: any[] = [];

    if (dbConnected) {
      try {
        // Find user
        const user = await prisma.user.findUnique({ where: { id: userId } });
        if (user) {
          oldXp = user.xp;
          oldLevel = user.level;

          // Upsert progress
          await prisma.learningItemProgress.upsert({
            where: {
              userId_learningItemId: { userId, learningItemId },
            },
            update: {
              xpEarned: xpReward,
            },
            create: {
              userId,
              learningItemId,
              xpEarned: xpReward,
            },
          });

          // Update user XP & level
          newXp = oldXp + xpReward;
          newLevel = getLevelFromXp(newXp);
          await prisma.user.update({
            where: { id: userId },
            data: { xp: newXp, level: newLevel },
          });

          // Update Streak
          await this.updateStreakInternal(userId, true);

          // Run Achievements unlock check
          const { checkAndUnlockAchievements } = await import("@/modules/achievements/achievements");
          newAchievements = await checkAndUnlockAchievements(userId);

          return {
            xpEarned: xpReward,
            levelUp: newLevel > oldLevel,
            newAchievements,
          };
        }
      } catch (e) {
        console.error("Prisma error in completeLearningItem", e);
      }
    }

    // Fallback mode
    const dbData = readMockDb();
    let user = dbData.users.find((u) => u.id === userId);
    if (!user) {
      user = {
        id: userId,
        name: "Alex AI",
        email: "alex@neuroforge.ai",
        role: "ADMIN",
        xp: 120,
        level: 2,
        createdAt: new Date().toISOString(),
      };
      dbData.users.push(user);
    }

    oldXp = user.xp;
    oldLevel = user.level;

    // Save progress
    const existingProgressIndex = dbData.progress.findIndex(
      (p) => p.userId === userId && p.learningItemId === learningItemId
    );
    if (existingProgressIndex >= 0) {
      dbData.progress[existingProgressIndex].xpEarned = xpReward;
    } else {
      dbData.progress.push({
        id: Math.random().toString(36).substring(2),
        userId,
        learningItemId,
        completedAt: new Date().toISOString(),
        xpEarned: xpReward,
      });
    }

    // Update user stats
    newXp = oldXp + xpReward;
    newLevel = getLevelFromXp(newXp);
    user.xp = newXp;
    user.level = newLevel;

    // Update Streak
    this.updateStreakInternalMock(dbData, userId);

    // Achievements unlock check mock
    newAchievements = this.checkAchievementsMock(dbData, user);

    writeMockDb(dbData);

    return {
      xpEarned: xpReward,
      levelUp: newLevel > oldLevel,
      newAchievements,
    };
  },

  /**
   * Remove/uncheck completed learning item progress and recalculate XP/Level
   */
  async uncompleteLearningItem(
    userId: string,
    learningItemId: number
  ): Promise<{ success: boolean; xpLost: number }> {
    const dbConnected = await checkDbConnection();
    let xpLost = 0;

    if (dbConnected) {
      try {
        const progress = await prisma.learningItemProgress.findUnique({
          where: {
            userId_learningItemId: { userId, learningItemId },
          },
        });

        if (progress) {
          xpLost = progress.xpEarned;

          await prisma.learningItemProgress.delete({
            where: {
              userId_learningItemId: { userId, learningItemId },
            },
          });

          const user = await prisma.user.findUnique({ where: { id: userId } });
          if (user) {
            const newXp = Math.max(0, user.xp - xpLost);
            const newLevel = getLevelFromXp(newXp);
            await prisma.user.update({
              where: { id: userId },
              data: { xp: newXp, level: newLevel },
            });
          }

          return { success: true, xpLost };
        }
      } catch (e) {
        console.error("Prisma error in uncompleteLearningItem", e);
      }
    }

    // Fallback mode
    const dbData = readMockDb();
    const existingProgressIndex = dbData.progress.findIndex(
      (p) => p.userId === userId && p.learningItemId === learningItemId
    );

    if (existingProgressIndex >= 0) {
      xpLost = dbData.progress[existingProgressIndex].xpEarned;
      dbData.progress.splice(existingProgressIndex, 1);

      const user = dbData.users.find((u) => u.id === userId);
      if (user) {
        const newXp = Math.max(0, user.xp - xpLost);
        user.xp = newXp;
        user.level = getLevelFromXp(newXp);
      }

      writeMockDb(dbData);
      return { success: true, xpLost };
    }

    return { success: false, xpLost: 0 };
  },

  /**
   * Get all bookmarked learning items
   */
  async getBookmarks(userId: string): Promise<number[]> {
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        const bookmarks = await prisma.bookmark.findMany({
          where: { userId },
          select: { learningItemId: true },
        });
        return bookmarks.map((b) => b.learningItemId);
      } catch (e) {
        console.error("Prisma error in getBookmarks", e);
      }
    }

    const dbData = readMockDb();
    return dbData.bookmarks
      .filter((b) => b.userId === userId)
      .map((b) => b.learningItemId);
  },

  /**
   * Toggle a bookmark
   */
  async toggleBookmark(userId: string, learningItemId: number): Promise<boolean> {
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        const existing = await prisma.bookmark.findUnique({
          where: { userId_learningItemId: { userId, learningItemId } },
        });

        if (existing) {
          await prisma.bookmark.delete({
            where: { userId_learningItemId: { userId, learningItemId } },
          });
          return false; // unbookmarked
        } else {
          await prisma.bookmark.create({
            data: { userId, learningItemId },
          });
          return true; // bookmarked
        }
      } catch (e) {
        console.error("Prisma error in toggleBookmark", e);
      }
    }

    // Fallback mode
    const dbData = readMockDb();
    const existingIndex = dbData.bookmarks.findIndex(
      (b) => b.userId === userId && b.learningItemId === learningItemId
    );

    let isBookmarked = false;
    if (existingIndex >= 0) {
      dbData.bookmarks.splice(existingIndex, 1);
    } else {
      dbData.bookmarks.push({
        id: Math.random().toString(36).substring(2),
        userId,
        learningItemId: kbQuestionId(learningItemId),
        createdAt: new Date().toISOString(),
      });
      isBookmarked = true;
    }

    writeMockDb(dbData);
    return isBookmarked;
  },

  /**
   * Get User Streak Info
   */
  async getStreak(userId: string): Promise<MockStreak> {
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        let streak = await prisma.streak.findUnique({
          where: { userId },
        });
        if (!streak) {
          streak = await prisma.streak.create({
            data: { userId, currentCount: 2, longestCount: 5, lastActive: new Date(Date.now() - 24 * 60 * 60 * 1000) },
          });
        }
        return {
          id: streak.id,
          userId: streak.userId,
          currentCount: streak.currentCount,
          longestCount: streak.longestCount,
          lastActive: streak.lastActive ? streak.lastActive.toISOString() : null,
        };
      } catch (e) {
        console.error("Prisma error in getStreak", e);
      }
    }

    const dbData = readMockDb();
    let streak = dbData.streaks.find((s) => s.userId === userId);
    if (!streak) {
      streak = {
        id: "mock-streak-id",
        userId,
        currentCount: 0,
        longestCount: 0,
        lastActive: null,
      };
      dbData.streaks.push(streak);
      writeMockDb(dbData);
    }
    return streak;
  },

  /**
   * Get User achievements list
   */
  async getUserAchievements(userId: string): Promise<{ code: string; unlockedAt: string }[]> {
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        const achs = await prisma.userAchievement.findMany({
          where: { userId },
          include: { achievement: true },
        });
        return achs.map((ua) => ({
          code: ua.achievement.code,
          unlockedAt: ua.unlockedAt.toISOString(),
        }));
      } catch (e) {
        console.error("Prisma error in getUserAchievements", e);
      }
    }

    const dbData = readMockDb();
    return dbData.userAchievements
      .filter((ua) => ua.userId === userId)
      .map((ua) => ({
        code: ua.achievementCode,
        unlockedAt: ua.unlockedAt,
      }));
  },

  /**
   * Get User Settings
   */
  async getSettings(userId: string): Promise<Omit<MockSettings, "id" | "userId">> {
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        let settings = await prisma.userSettings.findUnique({
          where: { userId },
        });
        if (!settings) {
          settings = await prisma.userSettings.create({
            data: { userId, theme: "dark" },
          });
        }
        return {
          theme: settings.theme,
          emailNotifications: settings.emailNotifications,
          marketingEmails: settings.marketingEmails,
          publicProfile: settings.publicProfile,
        };
      } catch (e) {
        console.error("Prisma error in getSettings", e);
      }
    }

    const dbData = readMockDb();
    let settings = dbData.settings.find((s) => s.userId === userId);
    if (!settings) {
      settings = {
        id: "mock-settings-id",
        userId,
        theme: "dark",
        emailNotifications: true,
        marketingEmails: false,
        publicProfile: true,
      };
      dbData.settings.push(settings);
      writeMockDb(dbData);
    }
    return {
      theme: settings.theme,
      emailNotifications: settings.emailNotifications,
      marketingEmails: settings.marketingEmails,
      publicProfile: settings.publicProfile,
    };
  },

  /**
   * Update User Settings
   */
  async updateSettings(
    userId: string,
    data: Partial<Omit<MockSettings, "id" | "userId">>
  ): Promise<void> {
    const dbConnected = await checkDbConnection();

    if (dbConnected) {
      try {
        await prisma.userSettings.update({
          where: { userId },
          data,
        });
        return;
      } catch (e) {
        console.error("Prisma error in updateSettings", e);
      }
    }

    const dbData = readMockDb();
    const settingsIndex = dbData.settings.findIndex((s) => s.userId === userId);
    if (settingsIndex >= 0) {
      dbData.settings[settingsIndex] = {
        ...dbData.settings[settingsIndex],
        ...data,
      };
      writeMockDb(dbData);
    }
  },

  // Internal helper to update streak (connected DB mode)
  async updateStreakInternal(userId: string, isCompletion: boolean) {
    try {
      const { updateUserStreak } = await import("@/modules/progress/streak");
      await updateUserStreak(userId);
    } catch (e) {
      console.error("Failed to update streak internal", e);
    }
  },

  // Internal helper to update streak (mock mode)
  updateStreakInternalMock(dbData: MockDatabase, userId: string) {
    let streak = dbData.streaks.find((s) => s.userId === userId);
    const now = new Date();

    if (!streak) {
      streak = {
        id: Math.random().toString(36).substring(2),
        userId,
        currentCount: 1,
        longestCount: 1,
        lastActive: now.toISOString(),
      };
      dbData.streaks.push(streak);
      return;
    }

    const lastActive = streak.lastActive;
    if (!lastActive) {
      streak.currentCount = 1;
      streak.longestCount = Math.max(streak.longestCount, 1);
      streak.lastActive = now.toISOString();
      return;
    }

    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const lastActiveDate = new Date(new Date(lastActive).getFullYear(), new Date(lastActive).getMonth(), new Date(lastActive).getDate());

    const diffTime = today.getTime() - lastActiveDate.getTime();
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));

    if (diffDays === 0) {
      // Do nothing
    } else if (diffDays === 1) {
      streak.currentCount += 1;
      streak.longestCount = Math.max(streak.longestCount, streak.currentCount);
      streak.lastActive = now.toISOString();
    } else {
      streak.currentCount = 1;
      streak.lastActive = now.toISOString();
    }
  },

  // Mock checking achievements
  checkAchievementsMock(dbData: MockDatabase, user: MockUser): any[] {
    const completedIds = dbData.progress
      .filter((p) => p.userId === user.id)
      .map((p) => p.learningItemId);
    const completedCount = completedIds.length;

    const streak = dbData.streaks.find((s) => s.userId === user.id);
    const streakCount = streak?.currentCount ?? 0;

    const unlockedCodes = new Set(
      dbData.userAchievements.filter((ua) => ua.userId === user.id).map((ua) => ua.achievementCode)
    );

    const checkList = [
      { code: "FIRST_QUESTION", name: "First Step", xpReward: 50, check: () => completedCount >= 1 },
      {
        code: "PYTHON_EXPLORER",
        name: "Python Explorer",
        xpReward: 100,
        check: () => Array.from({ length: 10 }, (_, i) => i + 1).every((id) => completedIds.includes(id)),
      },
      {
        code: "STATS_GURU",
        name: "Statistics Guru",
        xpReward: 150,
        check: () => Array.from({ length: 15 }, (_, i) => i + 11).every((id) => completedIds.includes(id)),
      },
      {
        code: "ML_MASTER",
        name: "Machine Learning Master",
        xpReward: 200,
        check: () => Array.from({ length: 20 }, (_, i) => i + 26).every((id) => completedIds.includes(id)),
      },
      {
        code: "DL_WIZARD",
        name: "Deep Learning Wizard",
        xpReward: 250,
        check: () => Array.from({ length: 15 }, (_, i) => i + 46).every((id) => completedIds.includes(id)),
      },
      {
        code: "LLM_EXPERT",
        name: "LLM Expert",
        xpReward: 250,
        check: () => Array.from({ length: 15 }, (_, i) => i + 61).every((id) => completedIds.includes(id)),
      },
      {
        code: "RAG_CHAMP",
        name: "RAG Champion",
        xpReward: 200,
        check: () => Array.from({ length: 10 }, (_, i) => i + 76).every((id) => completedIds.includes(id)),
      },
      {
        code: "AGENT_COMMANDER",
        name: "Agent Commander",
        xpReward: 200,
        check: () => Array.from({ length: 10 }, (_, i) => i + 86).every((id) => completedIds.includes(id)),
      },
      {
        code: "ARCHITECT",
        name: "System Design Architect",
        xpReward: 250,
        check: () => Array.from({ length: 5 }, (_, i) => i + 96).every((id) => completedIds.includes(id)),
      },
      { code: "STREAK_3", name: "Consistent Learner", xpReward: 100, check: () => streakCount >= 3 },
      { code: "STREAK_7", name: "Unstoppable", xpReward: 250, check: () => streakCount >= 7 },
      { code: "LEVEL_5", name: "Rising Star", xpReward: 200, check: () => user.level >= 5 },
      { code: "LEVEL_10", name: "Elite AI Engineer", xpReward: 500, check: () => user.level >= 10 },
    ];

    const newlyUnlocked: any[] = [];
    let extraXp = 0;

    checkList.forEach((ach) => {
      if (!unlockedCodes.has(ach.code) && ach.check()) {
        dbData.userAchievements.push({
          id: Math.random().toString(36).substring(2),
          userId: user.id,
          achievementCode: ach.code,
          unlockedAt: new Date().toISOString(),
        });
        newlyUnlocked.push({
          code: ach.code,
          name: ach.name,
          xpReward: ach.xpReward,
        });
        extraXp += ach.xpReward;
      }
    });

    if (extraXp > 0) {
      user.xp += extraXp;
      user.level = getLevelFromXp(user.xp);
    }

    return newlyUnlocked;
  },
};

function kbQuestionId(id: number): number {
  return id;
}
