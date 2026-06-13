"use client";

import React, { useState, useEffect } from "react";
import { LearningItem } from "@/modules/questions/questions";
import { useUserStore } from "@/shared/hooks/use-user-store";
import { getLevelProgress } from "@/modules/progress/xp";
import searchIndex from "../../../../content/search_index.json";
import {
  Star,
  Check,
  Award,
  ChevronLeft,
  BookOpen,
  Trophy,
  ExternalLink,
  Clock,
  Sparkles,
  Lock,
  Compass,
  Flame,
  CheckCircle,
  HelpCircle,
  Play,
  FileCode,
  Code,
  Layers,
  Zap,
  XCircle,
} from "lucide-react";
import Link from "next/link";

interface WorkspaceProps {
  item: LearningItem;
}

export function LearningItemWorkspace({ item }: WorkspaceProps) {
  const {
    user,
    streak,
    completedLearningItems,
    bookmarks,
    toggleBookmark,
    completeLearningItem,
    uncompleteLearningItem,
    fetchUserData,
  } = useUserStore();

  const isCompleted = completedLearningItems.includes(item.id);
  const isBookmarked = bookmarks.includes(item.id);

  // States
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showUnlockModal, setShowUnlockModal] = useState(false);
  const [unlockedBadges, setUnlockedBadges] = useState<any[]>([]);
  const [isBtnHovered, setIsBtnHovered] = useState(false);

  useEffect(() => {
    fetchUserData();
  }, [fetchUserData]);

  // Handle completion toggle
  const handleToggleCompletion = async () => {
    setIsSubmitting(true);
    try {
      if (isCompleted) {
        await uncompleteLearningItem(item.id);
      } else {
        const xpReward = item.estimated_time_minutes * 10;
        const result = await completeLearningItem(item.id, xpReward);

        if (result && result.newAchievements && result.newAchievements.length > 0) {
          setUnlockedBadges(result.newAchievements);
          setShowUnlockModal(true);
        }
      }
    } catch (e) {
      console.error("Completion update failed", e);
    } finally {
      setIsSubmitting(false);
    }
  };

  const getDifficultyColor = (diff: string) => {
    switch (diff) {
      case "Easy":
        return "text-emerald-500 bg-emerald-500/10 border-emerald-500/20";
      case "Medium":
        return "text-amber-500 bg-amber-500/10 border-amber-500/20";
      case "Hard":
        return "text-rose-500 bg-rose-500/10 border-rose-500/20";
      default:
        return "text-muted-foreground bg-secondary";
    }
  };

  const getTheoryTypeDetails = (type: string) => {
    switch (type) {
      case "youtube":
        return { label: "YouTube Video", color: "bg-rose-500/10 text-rose-400 border-rose-500/20", icon: Play };
      case "research-paper":
        return { label: "Research Paper", color: "bg-indigo-500/10 text-indigo-400 border-indigo-500/20", icon: FileCode };
      case "github":
        return { label: "GitHub Code", color: "bg-zinc-500/10 text-zinc-400 border-zinc-500/20", icon: Code };
      case "course":
        return { label: "Course / Tutorial", color: "bg-blue-500/10 text-blue-400 border-blue-500/20", icon: Zap };
      case "documentation":
        return { label: "Documentation", color: "bg-teal-500/10 text-teal-400 border-teal-500/20", icon: Layers };
      case "blog":
        return { label: "Blog Article", color: "bg-pink-500/10 text-pink-400 border-pink-500/20", icon: BookOpen };
      case "article":
      default:
        return { label: "Theory Article", color: "bg-purple-500/10 text-purple-400 border-purple-500/20", icon: BookOpen };
    }
  };

  const getPlatformDetails = (platform: string) => {
    switch (platform) {
      case "DEEP_ML":
        return { label: "Deep-ML Challenge", color: "bg-blue-500/10 text-blue-400 border-blue-500/20", icon: Zap };
      case "KAGGLE":
        return { label: "Kaggle Workbook", color: "bg-cyan-500/10 text-cyan-400 border-cyan-500/20", icon: Sparkles };
      case "HUGGING_FACE":
        return { label: "Hugging Face Section", color: "bg-amber-500/10 text-amber-400 border-amber-500/20", icon: Star };
      case "GITHUB":
        return { label: "GitHub Repository", color: "bg-zinc-500/10 text-zinc-400 border-zinc-500/20", icon: Code };
      case "LANGCHAIN":
        return { label: "LangChain Exercise", color: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", icon: Compass };
      case "LANGGRAPH":
        return { label: "LangGraph Exercise", color: "bg-purple-500/10 text-purple-400 border-purple-500/20", icon: Layers };
      case "LLAMAINDEX":
        return { label: "LlamaIndex Exercise", color: "bg-indigo-500/10 text-indigo-400 border-indigo-500/20", icon: FileCode };
      case "CUSTOM":
        return { label: "Custom Exercise", color: "bg-teal-500/10 text-teal-400 border-teal-500/20", icon: BookOpen };
      case "EXTERNAL":
      default:
        return { label: "External Platform", color: "bg-secondary text-muted-foreground", icon: ExternalLink };
    }
  };

  // Find prerequisite details
  const prereqItems = (item.prerequisites || []).map((pId) => {
    const match = searchIndex.find((idxItem) => idxItem.id === pId);
    return match
      ? { id: pId, title: match.title, slug: match.slug, completed: completedLearningItems.includes(pId) }
      : { id: pId, title: `Resource #${pId}`, slug: "", completed: completedLearningItems.includes(pId) };
  });

  const xpProgress = user ? getLevelProgress(user.xp) : null;
  const xpReward = item.estimated_time_minutes * 10;

  const theoryDetails = getTheoryTypeDetails(item.theory_resource?.type || "article");
  const TheoryIcon = theoryDetails.icon;

  const practiceDetails = getPlatformDetails(item.practice_resource?.platform || "EXTERNAL");
  const PracticeIcon = practiceDetails.icon;

  return (
    <div className="space-y-6 max-w-6xl mx-auto animate-fade-in-up">
      {/* Top Header Row */}
      <div className="flex items-center justify-between border-b border-border/40 pb-4">
        <div className="flex items-center gap-3">
          <Link
            href="/learning-items"
            className="rounded-lg p-2 hover:bg-secondary text-muted-foreground hover:text-foreground transition-colors border border-border/40"
          >
            <ChevronLeft className="h-4.5 w-4.5" />
          </Link>
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold text-muted-foreground">
              <span>Section: {item.section}</span>
              <span>•</span>
              <span>ID #{item.id}</span>
            </div>
            <h1 className="text-xl sm:text-2xl font-black text-foreground mt-0.5">
              {item.title}
            </h1>
          </div>
        </div>

        <button
          onClick={() => toggleBookmark(item.id)}
          className={`rounded-lg p-2.5 transition-colors border border-border/40 hover:bg-secondary ${
            isBookmarked ? "text-amber-500 border-amber-500/20 bg-amber-500/5" : "text-muted-foreground/45 hover:text-foreground"
          }`}
          aria-label="Bookmark"
        >
          <Star className={`h-5 w-5 ${isBookmarked ? "fill-amber-500" : ""}`} />
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* LEFT COLUMN: Resource Details (Spans 2) */}
        <div className="lg:col-span-2 space-y-6">
          {/* Dual Resource Cards Row */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {/* Theory Resource Card */}
            <div className="glass-panel relative overflow-hidden rounded-2xl border border-border/40 bg-card p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition-all gap-4">
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold text-muted-foreground uppercase tracking-wider">Step 1: Theory</span>
                  <span className={`border px-2 py-0.5 rounded-md text-[10px] font-bold ${theoryDetails.color} flex items-center gap-1`}>
                    <TheoryIcon className="h-3.5 w-3.5" />
                    {theoryDetails.label}
                  </span>
                </div>
                <h3 className="text-base font-bold text-foreground leading-snug">
                  {item.theory_resource?.title || `Theory for ${item.title}`}
                </h3>
                <p className="text-xs text-muted-foreground leading-relaxed">
                  Study the core concepts and background material for this learning item.
                </p>
              </div>
              <button
                onClick={() => window.open(item.theory_resource?.url, "_blank")}
                className="w-full flex items-center justify-center gap-1.5 rounded-xl bg-primary/10 hover:bg-primary/20 text-primary dark:text-blue-400 py-3 text-xs font-bold transition-all border border-primary/20 hover:border-primary/30 mt-2"
              >
                <span>Open Theory Link</span>
                <ExternalLink className="h-3.5 w-3.5" />
              </button>
            </div>

            {/* Practice Resource Card */}
            <div className="glass-panel relative overflow-hidden rounded-2xl border border-border/40 bg-card p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition-all gap-4">
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold text-muted-foreground uppercase tracking-wider">Step 2: Practice</span>
                  <span className={`border px-2 py-0.5 rounded-md text-[10px] font-bold ${practiceDetails.color} flex items-center gap-1`}>
                    <PracticeIcon className="h-3.5 w-3.5" />
                    {practiceDetails.label}
                  </span>
                </div>
                <h3 className="text-base font-bold text-foreground leading-snug">
                  {item.practice_resource?.title || "Practice Exercise"}
                </h3>
                <p className="text-xs text-muted-foreground leading-relaxed">
                  Solve the challenges and apply your knowledge interactively.
                </p>
              </div>
              <button
                onClick={() => window.open(item.practice_resource?.url, "_blank")}
                className="w-full flex items-center justify-center gap-1.5 rounded-xl bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-500 py-3 text-xs font-bold transition-all border border-cyan-500/20 hover:border-cyan-500/30 mt-2"
              >
                <span>Open Practice Link</span>
                <ExternalLink className="h-3.5 w-3.5" />
              </button>
            </div>
          </div>

          {/* Overview & Summary Card */}
          <div className="glass-panel rounded-2xl border border-border/40 bg-card p-6 space-y-5">
            {/* Metadata Badges */}
            <div className="flex flex-wrap items-center gap-3">
              <span className={`border px-2.5 py-0.5 rounded-md text-xs font-bold ${getDifficultyColor(item.difficulty)}`}>
                {item.difficulty}
              </span>
              <span className="flex items-center gap-1.5 text-xs text-muted-foreground font-semibold">
                <Clock className="h-3.5 w-3.5 text-primary" />
                {item.estimated_time_minutes} min estimated study
              </span>
            </div>

            {/* Description / Summary */}
            <div className="space-y-2">
              <h3 className="text-base font-bold text-foreground flex items-center gap-2">
                <BookOpen className="h-4.5 w-4.5 text-primary" />
                Overview
              </h3>
              <p className="text-sm leading-relaxed text-muted-foreground whitespace-pre-wrap pl-6">
                {item.description}
              </p>
            </div>

            {/* Learning Objectives */}
            <div className="space-y-3 pt-2">
              <h3 className="text-base font-bold text-foreground flex items-center gap-2">
                <Trophy className="h-4.5 w-4.5 text-primary" />
                Learning Objectives
              </h3>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 pl-6 list-disc text-sm text-muted-foreground">
                {item.learning_objectives.map((obj, i) => (
                  <li key={i} className="leading-relaxed">
                    {obj}
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Prerequisites Card */}
          {prereqItems.length > 0 && (
            <div className="glass-panel rounded-2xl border border-border/40 bg-card p-6 space-y-3">
              <h3 className="text-base font-bold text-foreground flex items-center gap-2">
                <Lock className="h-4.5 w-4.5 text-primary" />
                Prerequisites
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pl-6">
                {prereqItems.map((pre) => (
                  <div
                    key={pre.id}
                    className={`p-3 rounded-xl border flex items-center justify-between gap-3 text-xs sm:text-sm ${
                      pre.completed
                        ? "border-emerald-500/20 bg-emerald-500/5 text-emerald-500"
                        : "border-border/40 bg-secondary/20 text-muted-foreground"
                    }`}
                  >
                    <div className="min-w-0">
                      <span className="text-[10px] font-bold block opacity-60 uppercase">
                        Item #{pre.id}
                      </span>
                      {pre.slug ? (
                        <Link
                          href={`/learning-items/${pre.slug}`}
                          className="font-bold hover:underline truncate block text-foreground"
                        >
                          {pre.title}
                        </Link>
                      ) : (
                        <span className="font-bold truncate block">{pre.title}</span>
                      )}
                    </div>
                    {pre.completed ? (
                      <span className="bg-emerald-500/10 text-emerald-500 rounded-full p-0.5 shrink-0">
                        <Check className="h-3.5 w-3.5" />
                      </span>
                    ) : (
                      <span className="bg-secondary text-muted-foreground/60 rounded px-1.5 py-0.5 text-[10px] font-bold shrink-0">
                        Locked
                      </span>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* RIGHT COLUMN: Interactive Completion Card */}
        <div className="space-y-6">
          {/* Action Completion Box */}
          <div className="glass-panel rounded-2xl border border-border/40 bg-card p-6 space-y-6 relative overflow-hidden">
            <h3 className="text-base font-bold text-foreground flex items-center gap-2">
              <Sparkles className="h-4.5 w-4.5 text-cyan-400 animate-pulse" />
              Tracking Control
            </h3>

            {/* Reward Summary */}
            <div className="bg-secondary/40 rounded-xl p-4 border border-border/30 text-center space-y-1">
              <span className="text-[10px] uppercase font-bold text-muted-foreground tracking-wider">
                Completion Reward
              </span>
              <span className="block text-3xl font-black text-primary dark:text-blue-400">
                +{xpReward} XP
              </span>
            </div>

            {/* Study Checklist */}
            <div className="space-y-3 pt-2">
              <span className="text-xs font-bold text-muted-foreground uppercase tracking-wider block">
                Study Checklist
              </span>
              <div className="space-y-2.5">
                <div className="flex items-start gap-2.5 text-sm">
                  <div className={`mt-0.5 rounded border p-0.5 shrink-0 ${isCompleted ? "bg-emerald-500/15 border-emerald-500/40 text-emerald-500" : "border-border text-transparent"}`}>
                    <Check className="h-3.5 w-3.5" />
                  </div>
                  <span className={isCompleted ? "text-muted-foreground line-through" : "text-foreground font-medium"}>
                    Studied theory resource
                  </span>
                </div>
                <div className="flex items-start gap-2.5 text-sm">
                  <div className={`mt-0.5 rounded border p-0.5 shrink-0 ${isCompleted ? "bg-emerald-500/15 border-emerald-500/40 text-emerald-500" : "border-border text-transparent"}`}>
                    <Check className="h-3.5 w-3.5" />
                  </div>
                  <span className={isCompleted ? "text-muted-foreground line-through" : "text-foreground font-medium"}>
                    Completed practice exercise
                  </span>
                </div>
              </div>
            </div>

            {/* Completion Toggle */}
            <div className="pt-2 border-t border-border/30">
              <button
                onClick={handleToggleCompletion}
                disabled={isSubmitting}
                onMouseEnter={() => setIsBtnHovered(true)}
                onMouseLeave={() => setIsBtnHovered(false)}
                className={`w-full flex items-center justify-center gap-2.5 rounded-xl py-3.5 text-sm font-black transition-all ${
                  isCompleted
                    ? "bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 hover:bg-rose-500/10 hover:text-rose-400 hover:border-rose-500/20 cursor-pointer"
                    : "bg-primary text-primary-foreground hover:bg-primary/95 shadow-lg shadow-primary/20 cursor-pointer"
                }`}
              >
                {isSubmitting ? (
                  <span>Saving Completion...</span>
                ) : isCompleted ? (
                  isBtnHovered ? (
                    <>
                      <XCircle className="h-5 w-5 text-rose-400 animate-pulse" />
                      <span>Unmark as Completed</span>
                    </>
                  ) : (
                    <>
                      <CheckCircle className="h-5 w-5 fill-emerald-500/10" />
                      <span>Resource Completed!</span>
                    </>
                  )
                ) : (
                  <>
                    <Check className="h-5 w-5" />
                    <span>Mark as Completed</span>
                  </>
                )}
              </button>
              {isCompleted && (
                <span className="block text-[10px] text-muted-foreground text-center mt-2.5 italic">
                  Progress is saved automatically. Click to toggle completion!
                </span>
              )}
            </div>
          </div>

          {/* Gamification Context panel */}
          {user && xpProgress && (
            <div className="glass-panel rounded-2xl border border-border/40 bg-card p-6 space-y-4">
              <div className="flex items-center justify-between text-xs font-bold">
                <span className="bg-primary/10 text-primary dark:text-blue-400 px-2 py-0.5 rounded">
                  LEVEL {xpProgress.level}
                </span>
                <span className="text-muted-foreground">
                  {xpProgress.progressInLevel} / {xpProgress.neededForNextLevel} XP
                </span>
              </div>
              <div className="h-2 overflow-hidden rounded-full bg-secondary border border-border/30">
                <div
                  className="h-full bg-gradient-to-r from-primary to-cyan-400 transition-all duration-500"
                  style={{ width: `${xpProgress.percentage}%` }}
                />
              </div>

              {streak && (
                <div className="flex items-center gap-3 pt-2 border-t border-border/20 text-xs text-muted-foreground">
                  <Flame className="h-4.5 w-4.5 text-orange-500 animate-pulse" />
                  <span>
                    Current Streak: <strong>{streak.currentCount} days</strong> (Longest: {streak.longestCount}d)
                  </span>
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      {/* ACHIEVEMENT UNLOCKED MODAL */}
      {showUnlockModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
          <div className="glass-panel rounded-2xl max-w-md w-full border border-primary/30 bg-card p-6 text-center shadow-2xl animate-fade-in-up">
            <Trophy className="h-16 w-16 text-amber-500 mx-auto animate-bounce mb-4" />
            <h3 className="text-xl font-black text-foreground">Milestone Unlocked!</h3>
            <p className="mt-1.5 text-sm text-muted-foreground">
              Incredible work! You've unlocked {unlockedBadges.length} new achievement
              {unlockedBadges.length > 1 ? "s" : ""}:
            </p>

            <div className="mt-4 space-y-2.5">
              {unlockedBadges.map((badge, i) => (
                <div
                  key={i}
                  className="bg-secondary/40 border border-border/40 rounded-xl p-3.5 flex items-center justify-between text-left"
                >
                  <div>
                    <h4 className="font-bold text-foreground text-sm">{badge.name}</h4>
                    <span className="text-xs text-muted-foreground">Achievement Code: {badge.code}</span>
                  </div>
                  <span className="bg-amber-500/15 border border-amber-500/20 text-amber-500 rounded px-2 py-0.5 text-xs font-bold">
                    +{badge.xpReward} XP
                  </span>
                </div>
              ))}
            </div>

            <button
              onClick={() => setShowUnlockModal(false)}
              className="mt-6 w-full rounded-xl bg-primary py-2.5 text-sm font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/20"
            >
              Collect Rewards
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
