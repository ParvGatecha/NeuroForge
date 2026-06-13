"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useUserStore } from "@/shared/hooks/use-user-store";
import { getLevelProgress } from "@/modules/progress/xp";
import { getRecommendedNextLearningItem, getAllLearningItems } from "@/modules/roadmaps/roadmap";
import { getDetailedProgressAction, getUserAchievementsAction } from "@/app/actions";
import {
  Flame,
  Trophy,
  CheckCircle,
  TrendingUp,
  Map,
  BookOpen,
  ArrowRight,
  Sparkles,
  Star,
  Award,
  Layers,
  Clock,
  ExternalLink,
  Calendar,
  Hourglass,
  Check
} from "lucide-react";

interface TrackProgress {
  key: string;
  title: string;
  count: number;
  total: number;
  completed: boolean;
  percentage: number;
  color: string;
}

export function DashboardView() {
  const { user, streak, completedLearningItems, fetchUserData } = useUserStore();
  const [achievements, setAchievements] = useState<any[]>([]);
  const [loadingAchievements, setLoadingAchievements] = useState(true);
  const [detailedProgress, setDetailedProgress] = useState<any[]>([]);
  const [loadingProgress, setLoadingProgress] = useState(true);

  useEffect(() => {
    fetchUserData();
  }, [fetchUserData]);

  // Fetch unlocked achievements & detailed progress
  useEffect(() => {
    async function loadStats() {
      if (user?.id) {
        try {
          const [achList, progList] = await Promise.all([
            getUserAchievementsAction(user.id),
            getDetailedProgressAction(user.id)
          ]);
          setAchievements(achList);
          setDetailedProgress(progList);
        } catch (e) {
          console.error("Failed to load dashboard statistics", e);
        } finally {
          setLoadingAchievements(false);
          setLoadingProgress(false);
        }
      }
    }
    loadStats();
  }, [user?.id, completedLearningItems]);

  const allItems = getAllLearningItems();

  // Track configs
  const tracks = [
    { key: "python", title: "Python Concurrency", color: "from-blue-500 to-indigo-500" },
    { key: "statistics", title: "Mathematical Stats", color: "from-purple-500 to-pink-500" },
    { key: "machine-learning", title: "Classical ML", color: "from-emerald-500 to-teal-500" },
    { key: "deep-learning", title: "Deep Learning Architecture", color: "from-rose-500 to-orange-500" },
    { key: "llm", title: "Large Language Models", color: "from-violet-500 to-purple-600" },
    { key: "rag", title: "RAG Engineering", color: "from-cyan-500 to-blue-500" },
    { key: "agents", title: "AI Agent Systems", color: "from-indigo-600 to-violet-500" },
    { key: "system-design", title: "AI System Design", color: "from-teal-500 to-emerald-600" },
  ];

  // Calculate track progress
  const tracksWithProgress: TrackProgress[] = tracks.map((track) => {
    const trackItems = allItems.filter(
      (item) => item.section.toLowerCase().replace(/\s+/g, "-") === track.key
    );
    const solved = trackItems.filter((item) => completedLearningItems.includes(item.id)).length;
    const percentage = trackItems.length > 0 ? Math.round((solved / trackItems.length) * 100) : 0;
    return {
      ...track,
      count: solved,
      total: trackItems.length,
      percentage,
      completed: solved === trackItems.length && trackItems.length > 0,
    };
  });

  // Calculate recommended next item
  const nextItem = getRecommendedNextLearningItem(completedLearningItems);

  // Calculate XP Level Info
  const xpInfo = user ? getLevelProgress(user.xp) : null;

  // Streak Week Checklist
  const streakDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  const isTodayActive = () => {
    if (!streak?.lastActive) return false;
    const lastActiveDate = new Date(streak.lastActive);
    const today = new Date();
    return (
      lastActiveDate.getDate() === today.getDate() &&
      lastActiveDate.getMonth() === today.getMonth() &&
      lastActiveDate.getFullYear() === today.getFullYear()
    );
  };

  const getDayCompletion = (dayIndex: number) => {
    const todayIndex = (new Date().getDay() + 6) % 7; // Mon is 0, Sun is 6
    if (isTodayActive() && dayIndex === todayIndex) return true;
    if (streak && streak.currentCount > 1 && dayIndex < todayIndex && dayIndex >= todayIndex - streak.currentCount + 1) {
      return true;
    }
    return false;
  };

  // Calculate hours completed & remaining
  const completedMinutes = allItems
    .filter((item) => completedLearningItems.includes(item.id))
    .reduce((acc, item) => acc + item.estimated_time_minutes, 0);

  const remainingMinutes = allItems
    .filter((item) => !completedLearningItems.includes(item.id))
    .reduce((acc, item) => acc + item.estimated_time_minutes, 0);

  const learningHoursCompleted = (completedMinutes / 60).toFixed(1);
  const estimatedHoursRemaining = (remainingMinutes / 60).toFixed(1);

  // Completed Today list
  const completedTodayItems = detailedProgress.filter((prog) => {
    const compDate = new Date(prog.completedAt);
    const today = new Date();
    return (
      compDate.getDate() === today.getDate() &&
      compDate.getMonth() === today.getMonth() &&
      compDate.getFullYear() === today.getFullYear()
    );
  });

  // Recently Completed Items (detailed list limit to 5)
  const recentCompletionsList = detailedProgress.slice(0, 5).map((prog) => {
    const itemDetails = allItems.find((idxItem) => idxItem.id === prog.learningItemId);
    return {
      id: prog.learningItemId,
      title: itemDetails?.title || `Resource #${prog.learningItemId}`,
      slug: itemDetails?.slug || "",
      section: itemDetails?.section || "Course",
      completedAt: new Date(prog.completedAt).toLocaleDateString(undefined, {
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit"
      }),
      xp: prog.xpEarned
    };
  });

  return (
    <div className="space-y-6 animate-fade-in-up">
      {/* 1. WELCOME BACK HERO BANNER */}
      {user && xpInfo && (
        <div className="glass-panel relative overflow-hidden rounded-2xl p-6 sm:p-8 neon-glow">
          <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <span className="inline-flex h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
                <span className="text-xs font-semibold text-muted-foreground uppercase tracking-widest">
                  AI Engineer Path
                </span>
              </div>
              <h1 className="text-2xl sm:text-3xl font-black tracking-tight">
                Welcome back, {user.name || "Alex"}
              </h1>
              <p className="text-sm text-muted-foreground max-w-md">
                Build your skills step-by-step. You have completed {completedLearningItems.length} of{" "}
                {allItems.length} roadmap items.
              </p>
            </div>

            {/* XP progress circle or bar display */}
            <div className="flex flex-col gap-2 min-w-[200px]">
              <div className="flex items-center justify-between text-xs font-bold">
                <span className="bg-primary/10 text-primary dark:text-blue-400 px-2 py-0.5 rounded">
                  LEVEL {xpInfo.level}
                </span>
                <span className="text-muted-foreground">
                  {xpInfo.progressInLevel} / {xpInfo.neededForNextLevel} XP
                </span>
              </div>
              <div className="h-3 overflow-hidden rounded-full bg-secondary border border-border/40">
                <div
                  className="h-full bg-gradient-to-r from-primary via-indigo-500 to-cyan-400 transition-all duration-500"
                  style={{ width: `${xpInfo.percentage}%` }}
                />
              </div>
              <span className="text-[10px] text-muted-foreground text-right font-medium">
                {100 - xpInfo.percentage}% XP needed for Level {xpInfo.level + 1}
              </span>
            </div>
          </div>
          <div className="absolute left-0 top-0 -ml-16 -mt-16 h-48 w-48 rounded-full bg-primary/10 blur-3xl" />
        </div>
      )}

      {/* 2. STATS OVERVIEW CARDS */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {/* Progress % */}
        <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card space-y-1">
          <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground">
            Total Progress
          </span>
          <div className="flex items-baseline gap-2">
            <span className="text-2xl sm:text-3xl font-black text-foreground">
              {allItems.length > 0
                ? Math.round((completedLearningItems.length / allItems.length) * 100)
                : 0}
              %
            </span>
            <span className="text-xs text-muted-foreground font-semibold">
              ({completedLearningItems.length}/{allItems.length})
            </span>
          </div>
        </div>

        {/* Study Hours Completed */}
        <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card space-y-1">
          <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground flex items-center gap-1">
            <Clock className="h-3.5 w-3.5 text-primary" />
            Hours Completed
          </span>
          <div className="flex items-baseline gap-1">
            <span className="text-2xl sm:text-3xl font-black text-foreground">
              {learningHoursCompleted}
            </span>
            <span className="text-xs text-muted-foreground font-semibold">hrs</span>
          </div>
        </div>

        {/* Study Hours Remaining */}
        <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card space-y-1">
          <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground flex items-center gap-1">
            <Hourglass className="h-3.5 w-3.5 text-cyan-400" />
            Remaining Hours
          </span>
          <div className="flex items-baseline gap-1">
            <span className="text-2xl sm:text-3xl font-black text-foreground">
              {estimatedHoursRemaining}
            </span>
            <span className="text-xs text-muted-foreground font-semibold">hrs</span>
          </div>
        </div>

        {/* Completed Today */}
        <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card space-y-1">
          <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground flex items-center gap-1">
            <Calendar className="h-3.5 w-3.5 text-emerald-500" />
            Completed Today
          </span>
          <div className="flex items-baseline gap-2">
            <span className="text-2xl sm:text-3xl font-black text-foreground">
              {completedTodayItems.length}
            </span>
            <span className="text-xs text-muted-foreground font-semibold">items</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* LEFT COLUMN: Track breakdown (spans 2) */}
        <div className="lg:col-span-2 space-y-6">
          {/* TRACK PROGRESS LIST */}
          <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
            <h2 className="text-lg font-bold flex items-center gap-2">
              <Layers className="h-5 w-5 text-primary" />
              Curriculum Tracks
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {tracksWithProgress.map((track) => (
                <div
                  key={track.key}
                  className="p-4 rounded-xl border border-border/40 bg-background/50 hover:bg-background/80 transition-all flex flex-col justify-between gap-3 group relative overflow-hidden"
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <h3 className="font-bold text-sm text-foreground">{track.title}</h3>
                      <span className="text-xs text-muted-foreground">
                        {track.count} / {track.total} Completed
                      </span>
                    </div>
                    {track.completed ? (
                      <span className="bg-emerald-500/10 text-emerald-500 border border-emerald-500/20 rounded-full p-1 text-xs">
                        <CheckCircle className="h-4 w-4" />
                      </span>
                    ) : (
                      <span className="text-xs font-bold text-muted-foreground/60">
                        {track.percentage}%
                      </span>
                    )}
                  </div>

                  <div className="h-1.5 w-full bg-secondary rounded-full overflow-hidden border border-border/10">
                    <div
                      className={`h-full bg-gradient-to-r ${track.color} transition-all duration-500`}
                      style={{ width: `${track.percentage}%` }}
                    />
                  </div>

                  <Link
                    href={`/learning-items?section=${track.key}`}
                    className="absolute inset-0 z-10"
                    aria-label={`View ${track.title} track`}
                  />
                </div>
              ))}
            </div>
          </div>

          {/* RECENTLY COMPLETED ITEMS */}
          <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
            <h2 className="text-lg font-bold flex items-center gap-2">
              <CheckCircle className="h-5 w-5 text-emerald-500" />
              Recently Completed
            </h2>

            {loadingProgress ? (
              <span className="text-xs text-muted-foreground">Loading completions...</span>
            ) : recentCompletionsList.length > 0 ? (
              <div className="space-y-2">
                {recentCompletionsList.map((rec) => (
                  <div
                    key={rec.id}
                    className="p-3.5 rounded-xl border border-border/30 bg-background/40 flex items-center justify-between gap-4 text-xs sm:text-sm"
                  >
                    <div className="min-w-0">
                      <span className="text-[9px] font-bold text-muted-foreground uppercase">
                        {rec.section}
                      </span>
                      <Link
                        href={`/learning-items/${rec.slug}`}
                        className="font-bold text-foreground hover:text-primary hover:underline truncate block"
                      >
                        {rec.title}
                      </Link>
                    </div>

                    <div className="text-right shrink-0">
                      <span className="text-[10px] text-muted-foreground block">
                        {rec.completedAt}
                      </span>
                      <span className="text-[10px] font-bold text-primary dark:text-blue-400">
                        +{rec.xp} XP
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="py-6 text-center text-xs text-muted-foreground border border-dashed border-border/40 rounded-xl">
                No items completed yet. Select a learning track and mark items completed to see them here!
              </div>
            )}
          </div>
        </div>

        {/* RIGHT COLUMN: Streaks, Recommendations & Badges */}
        <div className="space-y-6">
          {/* 1. RECOMMENDATION SECTION */}
          <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4 relative overflow-hidden">
            <h2 className="text-lg font-bold flex items-center gap-2">
              <Sparkles className="h-5 w-5 text-cyan-400 animate-pulse" />
              Recommended Next
            </h2>

            {nextItem ? (
              <div className="p-4 rounded-xl border border-primary/20 bg-primary/5 space-y-3">
                <div>
                  <span className="text-[10px] font-bold uppercase tracking-wider text-primary dark:text-blue-400 bg-primary/10 px-2 py-0.5 rounded">
                    {nextItem.section.toUpperCase()}
                  </span>
                  <h3 className="font-bold text-sm text-foreground leading-snug mt-1.5 truncate">
                    {nextItem.title}
                  </h3>
                  <p className="text-xs text-muted-foreground mt-1">
                    Est. time: {nextItem.estimated_time_minutes} min • {nextItem.difficulty}
                  </p>
                </div>

                <Link
                  href={`/learning-items/${nextItem.slug}`}
                  className="w-full inline-flex items-center justify-center gap-1.5 rounded-lg bg-primary py-2 text-xs font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/20"
                >
                  Start Studying
                  <ArrowRight className="h-3.5 w-3.5" />
                </Link>
              </div>
            ) : (
              <div className="p-4 rounded-xl border border-emerald-500/20 bg-emerald-500/5 text-center space-y-2">
                <Trophy className="h-8 w-8 text-amber-500 mx-auto" />
                <h3 className="font-bold text-sm">Roadmap Completed!</h3>
                <p className="text-xs text-muted-foreground">
                  You've successfully completed all learning items in the roadmap. You are an expert AI Engineer!
                </p>
              </div>
            )}
          </div>

          {/* 2. STREAKS PANEL */}
          <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-bold flex items-center gap-2">
                <Flame className="h-5 w-5 text-orange-500" />
                Daily Streak
              </h2>
              <span className="text-xs text-muted-foreground font-semibold">
                Longest: {streak?.longestCount ?? 0} days
              </span>
            </div>

            <div className="flex items-center gap-4 bg-secondary/35 p-4 rounded-xl border border-border/30">
              <div className="bg-orange-500/10 border border-orange-500/20 text-orange-500 rounded-full p-2.5">
                <Flame className="h-7 w-7 animate-pulse" />
              </div>
              <div>
                <span className="block text-2xl font-black text-foreground">
                  {streak?.currentCount ?? 0} Days
                </span>
                <span className="text-xs text-muted-foreground">
                  {isTodayActive() ? "Active today! Keep it up." : "Mark an item completed today to extend!"}
                </span>
              </div>
            </div>

            {/* Streak Week Tracker visual */}
            <div className="flex justify-between items-center pt-2">
              {streakDays.map((day, idx) => {
                const completed = getDayCompletion(idx);
                return (
                  <div key={day} className="flex flex-col items-center gap-1.5 text-center">
                    <span className="text-[10px] text-muted-foreground font-semibold">{day}</span>
                    <div
                      className={`h-7 w-7 rounded-lg flex items-center justify-center text-xs font-black border transition-all ${
                        completed
                          ? "bg-orange-500/20 border-orange-500/40 text-orange-500 shadow shadow-orange-500/10"
                          : "border-border bg-background/55 text-muted-foreground"
                      }`}
                    >
                      {completed ? "🔥" : "•"}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* 3. ACHIEVEMENTS LIST */}
          <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
            <h2 className="text-lg font-bold flex items-center gap-2">
              <Award className="h-5 w-5 text-amber-500" />
              Recent Badges
            </h2>

            {loadingAchievements ? (
              <span className="text-xs text-muted-foreground">Loading achievements...</span>
            ) : achievements.length > 0 ? (
              <div className="grid grid-cols-1 gap-2.5 max-h-[220px] overflow-y-auto pr-1">
                {achievements.map((ach) => (
                  <div
                    key={ach.code}
                    className="p-3 rounded-xl border border-border/40 bg-background/40 flex items-center gap-3"
                  >
                    <div className="flex h-9 w-9 items-center justify-center rounded-full bg-amber-500/10 text-amber-500 border border-amber-500/20">
                      <Award className="h-4.5 w-4.5" />
                    </div>
                    <div>
                      <h4 className="font-bold text-xs text-foreground leading-tight">
                        {ach.code.split("_").map((w: string) => w.charAt(0) + w.slice(1).toLowerCase()).join(" ")}
                      </h4>
                      <span className="text-[10px] text-muted-foreground">
                        Unlocked {new Date(ach.unlockedAt).toLocaleDateString()}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="py-6 text-center text-xs text-muted-foreground border border-dashed border-border/40 rounded-xl">
                No achievements unlocked yet. Mark resources completed to earn badges!
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
