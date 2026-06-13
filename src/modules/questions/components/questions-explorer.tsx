"use client";

import React, { useState, useEffect, useMemo } from "react";
import Link from "next/link";
import { useRouter, useSearchParams, usePathname } from "next/navigation";
import { useUserStore } from "@/shared/hooks/use-user-store";
import { LearningItemMetadata } from "@/modules/roadmaps/roadmap";
import Fuse from "fuse.js";
import {
  Search,
  CheckCircle,
  Clock,
  ChevronRight,
  Star,
  Layers,
  Filter,
  Sparkles,
  BookOpen,
  Play,
  FileCode,
  Code,
  Award,
  ExternalLink,
  Compass,
  Zap,
} from "lucide-react";

interface ExplorerProps {
  items: LearningItemMetadata[];
}

export function LearningItemsExplorer({ items }: ExplorerProps) {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const {
    completedLearningItems,
    bookmarks,
    toggleBookmark,
    completeLearningItem,
    uncompleteLearningItem,
  } = useUserStore();

  // Read URL query params
  const initialSearch = searchParams.get("search") || "";
  const initialSection = searchParams.get("section") || "all";
  const initialDifficulty = searchParams.get("difficulty") || "all";
  const initialResourceType = searchParams.get("resource_type") || "all";
  const initialBookmarked = searchParams.get("bookmarked") === "true";
  const initialCompleted = searchParams.get("completed") || "all";

  // State
  const [searchQuery, setSearchQuery] = useState(initialSearch);
  const [sectionFilter, setSectionFilter] = useState(initialSection);
  const [difficultyFilter, setDifficultyFilter] = useState(initialDifficulty);
  const [resourceTypeFilter, setResourceTypeFilter] = useState(initialResourceType);
  const [bookmarkedFilter, setBookmarkedFilter] = useState(initialBookmarked);
  const [completedFilter, setCompletedFilter] = useState(initialCompleted);
  const [currentPage, setCurrentPage] = useState(1);

  const itemsPerPage = 15;

  // Sync state to URL params when filters change (client-side only, no reload)
  useEffect(() => {
    const params = new URLSearchParams();
    if (searchQuery) params.set("search", searchQuery);
    if (sectionFilter !== "all") params.set("section", sectionFilter);
    if (difficultyFilter !== "all") params.set("difficulty", difficultyFilter);
    if (resourceTypeFilter !== "all") params.set("resource_type", resourceTypeFilter);
    if (bookmarkedFilter) params.set("bookmarked", "true");
    if (completedFilter !== "all") params.set("completed", completedFilter);

    const newUrl = `${pathname}?${params.toString()}`;
    window.history.replaceState(null, "", newUrl);
    setCurrentPage(1); // Reset page on filter change
  }, [
    searchQuery,
    sectionFilter,
    difficultyFilter,
    resourceTypeFilter,
    bookmarkedFilter,
    completedFilter,
    pathname,
  ]);

  // Fuse.js setup for searching
  const fuse = useMemo(() => {
    return new Fuse(items, {
      keys: ["title", "description", "tags", "section", "theory_resource.title", "practice_resource.title", "practice_resource.platform"],
      threshold: 0.3,
    });
  }, [items]);

  // Filter & Search Logic
  const filteredItems = useMemo(() => {
    let result = items;

    // Apply Fuse search if query exists
    if (searchQuery.trim()) {
      const searchResults = fuse.search(searchQuery);
      result = searchResults.map((r) => r.item);
    }

    // Filter by section (slug-based matching to resolve python, ml tab bug)
    if (sectionFilter !== "all") {
      result = result.filter(
        (q) => q.section.toLowerCase().replace(/\s+/g, "-") === sectionFilter
      );
    }

    // Filter by difficulty
    if (difficultyFilter !== "all") {
      result = result.filter((q) => q.difficulty === difficultyFilter);
    }

    // Filter by practice platform
    if (resourceTypeFilter !== "all") {
      result = result.filter((q) => q.practice_resource?.platform === resourceTypeFilter);
    }

    // Filter by bookmarks
    if (bookmarkedFilter) {
      result = result.filter((q) => bookmarks.includes(q.id));
    }

    // Filter by completion status
    if (completedFilter !== "all") {
      const showCompleted = completedFilter === "completed";
      result = result.filter((q) => completedLearningItems.includes(q.id) === showCompleted);
    }

    return result;
  }, [
    items,
    searchQuery,
    sectionFilter,
    difficultyFilter,
    resourceTypeFilter,
    bookmarkedFilter,
    completedFilter,
    bookmarks,
    completedLearningItems,
    fuse,
  ]);

  // Pagination
  const totalPages = Math.ceil(filteredItems.length / itemsPerPage);
  const paginatedItems = useMemo(() => {
    const start = (currentPage - 1) * itemsPerPage;
    return filteredItems.slice(start, start + itemsPerPage);
  }, [filteredItems, currentPage]);

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
        return { label: "Custom", color: "bg-teal-500/10 text-teal-400 border-teal-500/20", icon: BookOpen };
      case "EXTERNAL":
      default:
        return { label: "External", color: "bg-secondary text-muted-foreground", icon: ExternalLink };
    }
  };

  const formatSectionName = (sec: string) => {
    return sec
      .split("-")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ");
  };

  const sectionsList = [
    "all",
    "python",
    "statistics",
    "machine-learning",
    "deep-learning",
    "llm",
    "rag",
    "agents",
    "system-design",
  ];

  const resourceTypes = [
    { value: "all", label: "Platform: All" },
    { value: "DEEP_ML", label: "Deep-ML" },
    { value: "KAGGLE", label: "Kaggle" },
    { value: "HUGGING_FACE", label: "Hugging Face" },
    { value: "GITHUB", label: "GitHub" },
    { value: "LANGCHAIN", label: "LangChain" },
    { value: "LANGGRAPH", label: "LangGraph" },
    { value: "LLAMAINDEX", label: "LlamaIndex" },
    { value: "CUSTOM", label: "Custom" },
    { value: "EXTERNAL", label: "External" },
  ];

  return (
    <div className="space-y-6">
      {/* Top Banner Solved Count */}
      <div className="glass-panel relative overflow-hidden rounded-2xl p-6 sm:p-8 neon-glow-cyan animate-fade-in-up">
        <div className="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">Curriculum Learning Hub</h1>
            <p className="mt-1 text-sm text-muted-foreground">
              Structured study resources, deep tutorials, and hands-on exercises for AI Engineers.
            </p>
          </div>
          <div className="flex items-center gap-4 bg-background/40 dark:bg-background/20 rounded-xl p-4 border border-border/40">
            <div className="text-center">
              <span className="block text-2xl font-bold text-primary dark:text-blue-400">
                {completedLearningItems.length}
              </span>
              <span className="text-[10px] uppercase tracking-wider text-muted-foreground font-semibold">
                Completed
              </span>
            </div>
            <div className="h-8 w-[1px] bg-border/40" />
            <div className="text-center">
              <span className="block text-2xl font-bold">{items.length}</span>
              <span className="text-[10px] uppercase tracking-wider text-muted-foreground font-semibold">
                Total
              </span>
            </div>
            <div className="h-8 w-[1px] bg-border/40" />
            <div className="text-center">
              <span className="block text-2xl font-bold text-cyan-400">
                {items.length > 0
                  ? Math.round((completedLearningItems.length / items.length) * 100)
                  : 0}
                %
              </span>
              <span className="text-[10px] uppercase tracking-wider text-muted-foreground font-semibold">
                Progress
              </span>
            </div>
          </div>
        </div>
        <div className="absolute right-0 top-0 -mr-16 -mt-16 h-48 w-48 rounded-full bg-primary/10 blur-3xl" />
      </div>

      {/* Filter & Search Bar */}
      <div className="grid grid-cols-1 gap-4 lg:grid-cols-4 animate-fade-in-up [animation-delay:100ms]">
        {/* Search */}
        <div className="relative lg:col-span-2">
          <Search className="absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
          <input
            type="text"
            placeholder="Search learning resources by title, tag, or description..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full h-11 pl-10 pr-4 rounded-xl border border-border bg-background/50 backdrop-blur-sm focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-all text-sm"
          />
        </div>

        {/* Filters Selects */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 lg:col-span-2">
          {/* Difficulty */}
          <select
            value={difficultyFilter}
            onChange={(e) => setDifficultyFilter(e.target.value)}
            className="h-11 rounded-xl border border-border bg-background/50 backdrop-blur-sm px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
          >
            <option value="all">Difficulty: All</option>
            <option value="Easy">Easy</option>
            <option value="Medium">Medium</option>
            <option value="Hard">Hard</option>
          </select>

          {/* Resource Type */}
          <select
            value={resourceTypeFilter}
            onChange={(e) => setResourceTypeFilter(e.target.value)}
            className="h-11 rounded-xl border border-border bg-background/50 backdrop-blur-sm px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
          >
            {resourceTypes.map((t) => (
              <option key={t.value} value={t.value}>
                {t.label}
              </option>
            ))}
          </select>

          {/* Completion */}
          <select
            value={completedFilter}
            onChange={(e) => setCompletedFilter(e.target.value)}
            className="h-11 rounded-xl border border-border bg-background/50 backdrop-blur-sm px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary"
          >
            <option value="all">Status: All</option>
            <option value="completed">Completed</option>
            <option value="uncompleted">In Progress</option>
          </select>

          {/* Bookmark toggle */}
          <button
            onClick={() => setBookmarkedFilter(!bookmarkedFilter)}
            className={`flex items-center justify-center gap-1.5 h-11 rounded-xl border px-3 text-sm font-medium transition-all ${
              bookmarkedFilter
                ? "bg-amber-500/10 border-amber-500/30 text-amber-500"
                : "border-border bg-background/50 hover:bg-secondary text-muted-foreground hover:text-foreground"
            }`}
          >
            <Star className={`h-4 w-4 ${bookmarkedFilter ? "fill-amber-500" : ""}`} />
            <span>Bookmarked</span>
          </button>
        </div>
      </div>

      {/* Section Filter Tags list */}
      <div className="flex flex-wrap gap-1.5 pb-2 border-b border-border/40 overflow-x-auto scrollbar-none animate-fade-in-up [animation-delay:150ms]">
        {sectionsList.map((sec) => (
          <button
            key={sec}
            onClick={() => setSectionFilter(sec)}
            className={`whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-semibold border transition-all ${
              sectionFilter === sec
                ? "bg-primary border-primary text-primary-foreground shadow-lg shadow-primary/25"
                : "border-border bg-background/40 hover:bg-secondary text-muted-foreground hover:text-foreground"
            }`}
          >
            {sec === "all" ? "All Tracks" : formatSectionName(sec)}
          </button>
        ))}
      </div>

      {/* Learning Items List */}
      <div className="space-y-3 animate-fade-in-up [animation-delay:200ms]">
        {paginatedItems.length > 0 ? (
          paginatedItems.map((q) => {
            const isCompleted = completedLearningItems.includes(q.id);
            const isBookmarked = bookmarks.includes(q.id);
            const platformDetails = getPlatformDetails(q.practice_resource?.platform || "EXTERNAL");
            const PlatformIcon = platformDetails.icon;

            return (
              <div
                key={q.id}
                className="glass-card relative overflow-hidden rounded-xl border border-border/40 p-4 transition-all duration-200 hover:border-primary/45 hover:shadow-lg dark:hover:shadow-primary/5 flex flex-col md:flex-row md:items-center justify-between gap-4"
              >
                <div className="flex items-start gap-4 flex-1">
                  {/* Status Checkbox */}
                  <button
                    onClick={async (e) => {
                      e.preventDefault();
                      e.stopPropagation();
                      if (isCompleted) {
                        try {
                          await uncompleteLearningItem(q.id);
                        } catch (err) {
                          console.error("Failed to uncomplete item", err);
                        }
                      } else {
                        try {
                          const xpReward = (q.estimated_time_minutes || 15) * 10;
                          await completeLearningItem(q.id, xpReward);
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
                      <span className="text-xs font-bold text-muted-foreground">#{q.id}</span>
                      <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground/80">
                        {q.section}
                      </span>
                      <span className="text-muted-foreground/40">•</span>
                      <span className="inline-flex items-center gap-1 text-[10px] font-semibold text-primary dark:text-blue-400">
                        <Clock className="h-3 w-3" />
                        {q.estimated_time_minutes} min
                      </span>
                    </div>

                    <Link
                      href={`/learning-items/${q.slug}`}
                      className="block text-base font-bold leading-snug hover:text-primary hover:underline transition-all text-foreground truncate"
                    >
                      {q.title}
                    </Link>
                  </div>
                </div>

                {/* Right Side Badges & actions */}
                <div className="flex items-center justify-between md:justify-end gap-3 border-t border-border/20 pt-3 md:border-none md:pt-0">
                  <div className="flex items-center gap-2">
                    {/* Platform Badge */}
                    <span
                      className={`inline-flex items-center gap-1.5 rounded-md border px-2 py-0.5 text-xs font-bold ${platformDetails.color}`}
                    >
                      <PlatformIcon className="h-3.5 w-3.5" />
                      {platformDetails.label}
                    </span>

                    {/* Difficulty Badge */}
                    <span
                      className={`inline-flex items-center rounded-md border px-2 py-0.5 text-xs font-bold ${difficultyColors(
                        q.difficulty
                      )}`}
                    >
                      {q.difficulty}
                    </span>
                  </div>

                  {/* Bookmark Button */}
                  <div className="flex items-center gap-1.5 pl-3 border-l border-border/40">
                    <button
                      onClick={() => toggleBookmark(q.id)}
                      className={`rounded-lg p-2 transition-colors hover:bg-secondary ${
                        isBookmarked
                          ? "text-amber-500 hover:text-amber-600"
                          : "text-muted-foreground/40 hover:text-foreground"
                      }`}
                      aria-label="Toggle Bookmark"
                    >
                      <Star className={`h-4.5 w-4.5 ${isBookmarked ? "fill-amber-500" : ""}`} />
                    </button>

                    <Link
                      href={`/learning-items/${q.slug}`}
                      className="rounded-lg bg-primary/10 hover:bg-primary/20 text-primary dark:text-blue-400 p-2 transition-colors"
                      title="View Details"
                    >
                      <ChevronRight className="h-4.5 w-4.5" />
                    </Link>
                  </div>
                </div>
              </div>
            );
          })
        ) : (
          <div className="glass-panel rounded-xl py-12 px-4 text-center border border-border/40">
            <Layers className="mx-auto h-12 w-12 text-muted-foreground/45" />
            <h3 className="mt-4 text-lg font-bold">No resources found</h3>
            <p className="mt-1 text-sm text-muted-foreground">
              Try adjusting your search query or reset filters.
            </p>
            <button
              onClick={() => {
                setSearchQuery("");
                setSectionFilter("all");
                setDifficultyFilter("all");
                setResourceTypeFilter("all");
                setBookmarkedFilter(false);
                setCompletedFilter("all");
              }}
              className="mt-4 inline-flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2 text-xs font-semibold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/25"
            >
              Reset Filters
            </button>
          </div>
        )}
      </div>

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-1.5 pt-4 border-t border-border/30 animate-fade-in-up [animation-delay:250ms]">
          <button
            onClick={() => setCurrentPage((p) => Math.max(1, p - 1))}
            disabled={currentPage === 1}
            className="h-9 rounded-lg px-3 border border-border bg-background/50 text-sm font-semibold disabled:opacity-40 disabled:cursor-not-allowed hover:bg-secondary transition-all"
          >
            Previous
          </button>
          {Array.from({ length: totalPages }, (_, i) => i + 1).map((page) => (
            <button
              key={page}
              onClick={() => setCurrentPage(page)}
              className={`h-9 w-9 rounded-lg text-sm font-semibold transition-all ${
                currentPage === page
                  ? "bg-primary text-primary-foreground"
                  : "border border-border bg-background/50 hover:bg-secondary text-muted-foreground hover:text-foreground"
              }`}
            >
              {page}
            </button>
          ))}
          <button
            onClick={() => setCurrentPage((p) => Math.min(totalPages, p + 1))}
            disabled={currentPage === totalPages}
            className="h-9 rounded-lg px-3 border border-border bg-background/50 text-sm font-semibold disabled:opacity-40 disabled:cursor-not-allowed hover:bg-secondary transition-all"
          >
            Next
          </button>
        </div>
      )}
    </div>
  );
}
