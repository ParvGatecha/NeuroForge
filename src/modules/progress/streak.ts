import { prisma } from "@/shared/lib/prisma";

export async function updateUserStreak(userId: string): Promise<{
  currentCount: number;
  longestCount: number;
  streakUpdated: boolean;
}> {
  const now = new Date();
  const streak = await prisma.streak.findUnique({
    where: { userId },
  });

  if (!streak) {
    const newStreak = await prisma.streak.create({
      data: {
        userId,
        currentCount: 1,
        longestCount: 1,
        lastActive: now,
      },
    });
    return {
      currentCount: 1,
      longestCount: 1,
      streakUpdated: true,
    };
  }

  const lastActive = streak.lastActive;
  if (!lastActive) {
    const updated = await prisma.streak.update({
      where: { userId },
      data: {
        currentCount: 1,
        longestCount: Math.max(streak.longestCount, 1),
        lastActive: now,
      },
    });
    return {
      currentCount: 1,
      longestCount: updated.longestCount,
      streakUpdated: true,
    };
  }

  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const lastActiveDate = new Date(lastActive.getFullYear(), lastActive.getMonth(), lastActive.getDate());

  const diffTime = today.getTime() - lastActiveDate.getTime();
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));

  if (diffDays === 0) {
    return {
      currentCount: streak.currentCount,
      longestCount: streak.longestCount,
      streakUpdated: false,
    };
  } else if (diffDays === 1) {
    const nextCount = streak.currentCount + 1;
    const nextLongest = Math.max(streak.longestCount, nextCount);
    const updated = await prisma.streak.update({
      where: { userId },
      data: {
        currentCount: nextCount,
        longestCount: nextLongest,
        lastActive: now,
      },
    });
    return {
      currentCount: nextCount,
      longestCount: nextLongest,
      streakUpdated: true,
    };
  } else {
    const updated = await prisma.streak.update({
      where: { userId },
      data: {
        currentCount: 1,
        lastActive: now,
      },
    });
    return {
      currentCount: 1,
      longestCount: updated.longestCount,
      streakUpdated: true,
    };
  }
}
