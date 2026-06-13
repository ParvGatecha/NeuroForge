"use client";

import React, { useMemo } from "react";
import Link from "next/link";
import { useUserStore } from "@/shared/hooks/use-user-store";
import { getAllLearningItems } from "@/modules/roadmaps/roadmap";
import {
  Star,
  BookOpen,
  ChevronRight,
  Zap,
  Sparkles,
  Layers,
  FileCode,
  Code,
  Compass,
  ArrowUpRight,
  Clock,
  CheckCircle,
  FolderHeart,
  ExternalLink,
} from "lucide-react";

export default function SavedItemsPage() {
  const {
    bookmarks,
    completedLearningItems,
    toggleBookmark,
    completeLearningItem,
    uncompleteLearningItem,
  } = useUserStore();
  const allItems = useMemo(() => getAllLearningItems(), []);

  const bookmarkedItems = useMemo(() => {
    return allItems.filter((item) => bookmarks.includes(item.id));
  }, [bookmarks, allItems]);

  const platformQuickLinks = [
    {
      name: "Deep-ML",
      url: "https://deep-ml.com",
      desc: "Solve interactive machine learning problems.",
      color: "text-blue-400 border-blue-500/20 bg-blue-500/5 hover:border-blue-500/40",
      icon: Zap,
    },
    {
      name: "Kaggle",
      url: "https://www.kaggle.com",
      desc: "Workbooks, datasets, and ML competitions.",
      color: "text-cyan-400 border-cyan-500/20 bg-cyan-500/5 hover:border-cyan-500/40",
      icon: Sparkles,
    },
    {
      name: "Hugging Face",
      url: "https://huggingface.co",
      desc: "Models, datasets, and NLP courses.",
      color: "text-amber-400 border-amber-500/20 bg-amber-500/5 hover:border-amber-500/40",
      icon: Star,
    },
    {
      name: "LangChain",
      url: "https://github.com/langchain-ai/langchain",
      desc: "Build context-aware reasoning applications.",
      color: "text-emerald-400 border-emerald-500/20 bg-emerald-500/5 hover:border-emerald-500/40",
      icon: Compass,
    },
    {
      name: "LangGraph",
      url: "https://github.com/langchain-ai/langgraph",
      desc: "Create multi-agent stateful graph flows.",
      color: "text-purple-400 border-purple-500/20 bg-purple-500/5 hover:border-purple-500/40",
      icon: Layers,
    },
    {
      name: "LlamaIndex",
      url: "https://github.com/run-llama/llama_index",
      desc: "Data framework for LLM search indexing.",
      color: "text-indigo-400 border-indigo-500/20 bg-indigo-500/5 hover:border-indigo-500/40",
      icon: FileCode,
    },
  ];

  const getPlatformDetails = (platform: string) => {
    switch (platform) {
      case "DEEP_ML":
        return { label: "Deep-ML", color: "bg-blue-500/10 text-blue-400 border-blue-500/20", icon: Zap };
      case "KAGGLE":
        return { label: "Kaggle", color: "bg-cyan-500/10 text-cyan-400 border-cyan-500/20", icon: Sparkles };
      case "HUGGING_FACE":
        return { label: "Hugging Face", color: "bg-amber-500/10 text-amber-400 border-amber-500/20", icon: Star };
      case "GITHUB":
        return { label: "GitHub", color: "bg-zinc-500/10 text-zinc-400 border-zinc-500/20", icon: Code };
      case "LANGCHAIN":
        return { label: "LangChain", color: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", icon: Compass };
      case "LANGGRAPH":
        return { label: "LangGraph", color: "bg-purple-500/10 text-purple-400 border-purple-500/20", icon: Layers };
      case "LLAMAINDEX":
        return { label: "LlamaIndex", color: "bg-indigo-500/10 text-indigo-400 border-indigo-500/20", icon: FileCode };
      case "CUSTOM":
      case "EXTERNAL":
      default:
        return { label: "External Link", color: "bg-secondary text-muted-foreground", icon: ExternalLink };
    }
  };

  const difficultyColors = (difficulty: string) => {
    switch (difficulty) {
      case "Easy":
        return "bg-emerald-500/10 text-emerald-500 border-emerald-500/20";
      case "Medium":
        return "bg-amber-500/10 text-amber-500 border-amber-500/20";
      case "Hard":
        return "bg-rose-500/10 text-rose-500 border-rose-500/20";
      default:
        return "bg-secondary text-secondary-foreground";
    }
  };

  return (
    <div className="space-y-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 animate-fade-in-up">
      {/* Page Header */}
      <div className="flex items-center gap-3 border-b border-border/40 pb-4">
        <div className="p-2 rounded-xl bg-amber-500/10 text-amber-500 border border-amber-500/20">
          <Star className="h-6 w-6 fill-amber-500/15" />
        </div>
        <div>
          <h1 className="text-2xl font-black tracking-tight">Saved Items & Quick Access</h1>
          <p className="text-xs text-muted-foreground mt-0.5">
            Keep track of bookmarks and quickly access major external practice platforms.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column: Bookmarks */}
        <div className="lg:col-span-2 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-bold text-foreground flex items-center gap-2">
              <FolderHeart className="h-5 w-5 text-primary" />
              Your Bookmarked Resources
            </h2>
            <span className="text-xs font-semibold text-muted-foreground bg-secondary/80 px-2.5 py-1 rounded-full border border-border/30">
              {bookmarkedItems.length} saved
            </span>
          </div>

          <div className="space-y-3">
            {bookmarkedItems.length > 0 ? (
              bookmarkedItems.map((item) => {
                const isCompleted = completedLearningItems.includes(item.id);
                const platformDetails = getPlatformDetails(item.practice_resource?.platform || "EXTERNAL");
                const PlatformIcon = platformDetails.icon;

                return (
                  <div
                    key={item.id}
                    className="glass-card relative overflow-hidden rounded-xl border border-border/40 p-4 transition-all duration-200 hover:border-primary/45 hover:shadow-md flex flex-col md:flex-row md:items-center justify-between gap-4"
                  >
                    <div className="flex items-start gap-4 flex-1">
                      {/* Status Checkbox */}
                      <button
                        onClick={async (e) => {
                          e.preventDefault();
                          e.stopPropagation();
                          if (isCompleted) {
                            try {
                              await uncompleteLearningItem(item.id);
                            } catch (err) {
                              console.error("Failed to uncomplete item", err);
                            }
                          } else {
                            try {
                              const xpReward = (item.estimated_time_minutes || 15) * 10;
                              await completeLearningItem(item.id, xpReward);
                            } catch (err) {
                              console.error("Failed to complete item", err);
                            }
                          }
                        }}
                        className={`mt-0.5 rounded-full p-0.5 transition-all focus:outline-none focus:ring-2 focus:ring-primary/50 cursor-pointer ${
                          isCompleted
                            ? "text-emerald-500 hover:text-rose-500 hover:scale-105"
                            : "text-muted-foreground/30 hover:text-primary hover:scale-105"
                        }`}
                        title={isCompleted ? "Mark as In Progress (Uncheck)" : "Mark as Completed"}
                        aria-label={isCompleted ? "Mark as In Progress" : "Mark as Completed"}
                      >
                        <CheckCircle className={`h-5 w-5 transition-transform duration-200 ${isCompleted ? "fill-emerald-500/10" : ""}`} />
                      </button>

                      <div className="space-y-1.5 min-w-0">
                        <div className="flex flex-wrap items-center gap-2">
                          <span className="text-xs font-bold text-muted-foreground">#{item.id}</span>
                          <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground/80">
                            {item.section}
                          </span>
                          <span className="text-muted-foreground/40">•</span>
                          <span className="inline-flex items-center gap-1 text-[10px] font-semibold text-primary dark:text-blue-400">
                            <Clock className="h-3 w-3" />
                            {item.estimated_time_minutes} min
                          </span>
                        </div>

                        <Link
                          href={`/learning-items/${item.slug}`}
                          className="block text-base font-bold leading-snug hover:text-primary hover:underline transition-all text-foreground truncate"
                        >
                          {item.title}
                        </Link>
                      </div>
                    </div>

                    <div className="flex items-center justify-between md:justify-end gap-3 border-t border-border/20 pt-3 md:border-none md:pt-0">
                      <div className="flex items-center gap-2">
                        <span className={`inline-flex items-center gap-1 rounded-md border px-2 py-0.5 text-[10px] font-bold ${platformDetails.color}`}>
                          <PlatformIcon className="h-3.5 w-3.5" />
                          {platformDetails.label}
                        </span>
                        <span className={`inline-flex items-center rounded-md border px-2 py-0.5 text-[10px] font-bold ${difficultyColors(item.difficulty)}`}>
                          {item.difficulty}
                        </span>
                      </div>

                      <div className="flex items-center gap-1.5 pl-3 border-l border-border/40">
                        <button
                          onClick={() => toggleBookmark(item.id)}
                          className="rounded-lg p-2 text-amber-500 hover:text-amber-600 transition-colors hover:bg-secondary"
                          aria-label="Remove Bookmark"
                        >
                          <Star className="h-4.5 w-4.5 fill-amber-500" />
                        </button>
                        <Link
                          href={`/learning-items/${item.slug}`}
                          className="rounded-lg bg-primary/10 hover:bg-primary/20 text-primary dark:text-blue-400 p-2 transition-colors"
                        >
                          <ChevronRight className="h-4.5 w-4.5" />
                        </Link>
                      </div>
                    </div>
                  </div>
                );
              })
            ) : (
              <div className="glass-panel rounded-2xl py-12 px-4 text-center border border-border/40 bg-card/50">
                <Star className="mx-auto h-12 w-12 text-muted-foreground/30 animate-pulse" />
                <h3 className="mt-4 text-base font-bold">No bookmarks saved yet</h3>
                <p className="mt-1 text-sm text-muted-foreground max-w-xs mx-auto">
                  Bookmark items from the Learning Hub to save them here for quick access.
                </p>
                <Link
                  href="/learning-items"
                  className="mt-5 inline-flex items-center gap-1.5 rounded-xl bg-primary px-4 py-2.5 text-xs font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/25"
                >
                  Browse Roadmap Items
                </Link>
              </div>
            )}
          </div>
        </div>

        {/* Right Column: Platform Quick Links */}
        <div className="space-y-4">
          <h2 className="text-lg font-bold text-foreground flex items-center gap-2">
            <Compass className="h-5 w-5 text-primary" />
            Quick Launcher
          </h2>
          <div className="grid grid-cols-1 gap-3">
            {platformQuickLinks.map((plat) => {
              const Icon = plat.icon;
              return (
                <a
                  key={plat.name}
                  href={plat.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={`glass-panel border rounded-2xl p-4 flex items-start gap-3.5 transition-all duration-200 hover:translate-y-[-2px] group ${plat.color}`}
                >
                  <div className="p-2 rounded-xl bg-background/50 border border-border/20 group-hover:scale-105 transition-all">
                    <Icon className="h-5 w-5" />
                  </div>
                  <div className="min-w-0 space-y-0.5 flex-1">
                    <h3 className="font-bold text-sm text-foreground flex items-center gap-1">
                      {plat.name}
                      <ArrowUpRight className="h-3 w-3 opacity-0 group-hover:opacity-100 transition-opacity" />
                    </h3>
                    <p className="text-[11px] text-muted-foreground leading-normal">
                      {plat.desc}
                    </p>
                  </div>
                </a>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
