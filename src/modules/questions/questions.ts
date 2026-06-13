import fs from "fs";
import path from "path";

export interface LearningItem {
  id: number;
  slug: string;
  title: string;
  section: string;
  difficulty: "Easy" | "Medium" | "Hard";
  theory_resource: {
    title: string;
    url: string;
    type: "article" | "blog" | "documentation" | "youtube" | "research-paper" | "github" | "course";
  };
  practice_resource: {
    platform: "DEEP_ML" | "KAGGLE" | "HUGGING_FACE" | "GITHUB" | "LANGCHAIN" | "LANGGRAPH" | "LLAMAINDEX" | "CUSTOM" | "EXTERNAL";
    title: string;
    url: string;
  };
  estimated_time_minutes: number;
  tags: string[];
  learning_objectives: string[];
  description: string;
  prerequisites: number[];
}

export function getLearningItemBySlug(slug: string): LearningItem | null {
  const contentDir = path.join(process.cwd(), "content");

  if (!fs.existsSync(contentDir)) {
    return null;
  }

  function findFile(dir: string): string | null {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        const found = findFile(fullPath);
        if (found) return found;
      } else if (entry.name === `${slug}.json` || entry.name.endsWith(`-${slug}.json`)) {
        return fullPath;
      }
    }
    return null;
  }

  const filePath = findFile(contentDir);
  if (!filePath) return null;

  try {
    const content = fs.readFileSync(filePath, "utf-8");
    return JSON.parse(content) as LearningItem;
  } catch (e) {
    console.error(`Error reading learning item JSON: ${slug}`, e);
    return null;
  }
}
