export function getXpForLevel(level: number): number {
  if (level <= 1) return 0;
  // Level 2: 100 XP
  // Level 3: 282 XP
  // Level 4: 519 XP
  // Level 5: 800 XP
  return Math.floor(100 * Math.pow(level - 1, 1.5));
}

export function getLevelFromXp(xp: number): number {
  if (xp <= 0) return 1;
  let level = 1;
  while (getXpForLevel(level + 1) <= xp) {
    level++;
  }
  return level;
}

export interface LevelProgress {
  level: number;
  currentXp: number;
  xpForCurrentLevel: number;
  xpForNextLevel: number;
  progressInLevel: number;
  neededForNextLevel: number;
  percentage: number;
}

export function getLevelProgress(xp: number): LevelProgress {
  const level = getLevelFromXp(xp);
  const xpForCurrentLevel = getXpForLevel(level);
  const xpForNextLevel = getXpForLevel(level + 1);
  const progressInLevel = xp - xpForCurrentLevel;
  const neededForNextLevel = xpForNextLevel - xpForCurrentLevel;
  const percentage = neededForNextLevel > 0
    ? Math.min(100, Math.max(0, Math.floor((progressInLevel / neededForNextLevel) * 100)))
    : 0;

  return {
    level,
    currentXp: xp,
    xpForCurrentLevel,
    xpForNextLevel,
    progressInLevel,
    neededForNextLevel,
    percentage,
  };
}
