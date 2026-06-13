import roadmapData from "../../../content/roadmap.json";
import searchIndex from "../../../content/search_index.json";

export interface LearningItemMetadata {
  id: number;
  slug: string;
  title: string;
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
  section: string;
}

export function getAllLearningItems(): LearningItemMetadata[] {
  return (searchIndex as LearningItemMetadata[]).sort((a, b) => a.id - b.id);
}

export function getRecommendedNextLearningItem(
  completedLearningItemIds: number[]
): LearningItemMetadata | null {
  const allItems = getAllLearningItems();
  const completedSet = new Set(completedLearningItemIds);

  const sequence = roadmapData.recommended_sequence;
  for (const sectionName of sequence) {
    const sectionItems = allItems.filter(
      (item) => item.section.toLowerCase().replace(/\s+/g, "-") === sectionName
    );
    const uncompleted = sectionItems.find((item) => !completedSet.has(item.id));
    if (uncompleted) {
      return uncompleted;
    }
  }

  const fallback = allItems.find((item) => !completedSet.has(item.id));
  if (fallback) return fallback;

  return null;
}
