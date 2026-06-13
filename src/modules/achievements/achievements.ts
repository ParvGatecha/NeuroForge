import { prisma } from "@/shared/lib/prisma";
import { getLevelFromXp } from "@/modules/progress/xp";

interface UnlockResult {
  code: string;
  name: string;
  xpReward: number;
}

export async function checkAndUnlockAchievements(userId: string): Promise<UnlockResult[]> {
  // 1. Fetch user progress, streak, current level
  const user = await prisma.user.findUnique({
    where: { id: userId },
    include: {
      progress: true,
      achievements: {
        include: {
          achievement: true,
        },
      },
      streak: true,
    },
  });

  if (!user) return [];

  // Get already unlocked achievement codes
  const unlockedCodes = new Set(user.achievements.map((ua) => ua.achievement.code));

  // Load all achievements from database
  const allDbAchievements = await prisma.achievement.findMany();
  const achMap = new Map(allDbAchievements.map((a) => [a.code, a]));

  const newlyUnlocked: UnlockResult[] = [];

  // Completed learning item IDs
  const completedIds = user.progress.map((p) => p.learningItemId);
  const completedCount = completedIds.length;

  const pythonIds = Array.from({ length: 10 }, (_, i) => i + 1); // 1-10
  const statsIds = Array.from({ length: 15 }, (_, i) => i + 11); // 11-25
  const mlIds = Array.from({ length: 20 }, (_, i) => i + 26); // 26-45
  const dlIds = Array.from({ length: 15 }, (_, i) => i + 46); // 46-60
  const llmIds = Array.from({ length: 15 }, (_, i) => i + 61); // 61-75
  const ragIds = Array.from({ length: 10 }, (_, i) => i + 76); // 76-85
  const agentIds = Array.from({ length: 10 }, (_, i) => i + 86); // 86-95
  const sysDesignIds = Array.from({ length: 5 }, (_, i) => i + 96); // 96-100

  const meetsCriteria = (code: string): boolean => {
    switch (code) {
      case "FIRST_QUESTION":
        return completedCount >= 1;
      case "PYTHON_EXPLORER":
        return pythonIds.every((id) => completedIds.includes(id));
      case "STATS_GURU":
        return statsIds.every((id) => completedIds.includes(id));
      case "ML_MASTER":
        return mlIds.every((id) => completedIds.includes(id));
      case "DL_WIZARD":
        return dlIds.every((id) => completedIds.includes(id));
      case "LLM_EXPERT":
        return llmIds.every((id) => completedIds.includes(id));
      case "RAG_CHAMP":
        return ragIds.every((id) => completedIds.includes(id));
      case "AGENT_COMMANDER":
        return agentIds.every((id) => completedIds.includes(id));
      case "ARCHITECT":
        return sysDesignIds.every((id) => completedIds.includes(id));
      case "STREAK_3":
        return (user.streak?.currentCount ?? 0) >= 3;
      case "STREAK_7":
        return (user.streak?.currentCount ?? 0) >= 7;
      case "LEVEL_5":
        return user.level >= 5;
      case "LEVEL_10":
        return user.level >= 10;
      default:
        return false;
    }
  };

  // Check each achievement
  for (const ach of allDbAchievements) {
    if (!unlockedCodes.has(ach.code) && meetsCriteria(ach.code)) {
      newlyUnlocked.push({
        code: ach.code,
        name: ach.name,
        xpReward: ach.xpReward,
      });
    }
  }

  if (newlyUnlocked.length === 0) return [];

  // Unlock them in the database and add XP rewards to the user
  let totalXpEarned = 0;
  for (const ach of newlyUnlocked) {
    const dbAch = achMap.get(ach.code);
    if (!dbAch) continue;

    await prisma.userAchievement.create({
      data: {
        userId: user.id,
        achievementId: dbAch.id,
      },
    });
    totalXpEarned += dbAch.xpReward;
  }

  // Update user XP & Level
  if (totalXpEarned > 0) {
    const nextXp = user.xp + totalXpEarned;
    const nextLevel = getLevelFromXp(nextXp);

    await prisma.user.update({
      where: { id: user.id },
      data: {
        xp: nextXp,
        level: nextLevel,
      },
    });
  }

  return newlyUnlocked;
}
