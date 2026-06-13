"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { useUserStore } from "@/shared/hooks/use-user-store";
import { getAllLearningItems, LearningItemMetadata } from "@/modules/roadmaps/roadmap";
import roadmapData from "../../../../content/roadmap.json";
import {
  Lock,
  Unlock,
  CheckCircle,
  Play,
  Layers,
  ChevronDown,
  ChevronUp,
  Clock,
  BookOpen,
} from "lucide-react";

interface SectionDetails {
  key: string;
  title: string;
  description: string;
  items: LearningItemMetadata[];
  completedCount: number;
  totalCount: number;
  remainingCount: number;
  estimatedMinutesRemaining: number;
  isLocked: boolean;
  prereqs: string[];
}

export function RoadmapsView() {
  const { completedLearningItems, fetchUserData } = useUserStore();
  const [expandedSection, setExpandedSection] = useState<string | null>("python");

  useEffect(() => {
    fetchUserData();
  }, [fetchUserData]);

  const allItems = getAllLearningItems();
  const sectionOrder = roadmapData.section_order;
  const prerequisites = roadmapData.prerequisites as Record<string, string[]>;

  const sectionMetadata: Record<string, { title: string; desc: string }> = {
    python: { title: "Python Concurrency", desc: "Master memory benchmarking, GIL, async await, decorators, and context managers." },
    statistics: { title: "Mathematical Stats", desc: "Learn MLE, Bayes theorem, PDF integrations, hypothesis testing, and Metropolis-Hastings MCMC." },
    "machine-learning": { title: "Classical ML", desc: "Understand loss functions, Normal Equation, SVM kernels, PCA projection, and Expectation Maximization." },
    "deep-learning": { title: "Deep Learning Foundations", desc: "Derive backpropagation gradients, build Adam updates, CNNs, LSTMs, and scaled dot-product attention." },
    llm: { title: "Large Language Models", desc: "Build BPE tokenizers, LoRA layers, DPO losses, speculative decoding, and Rotary Embeddings." },
    rag: { title: "RAG Engineering", desc: "Write chunkers, hybrid searches, candidate rerankers, multi-query decomposers, and GraphRAG databases." },
    agents: { title: "AI Agent Systems", desc: "Program ReAct loops, function call validators, stateful graph routers, supervisor networks, and code executors." },
    "system-design": { title: "AI System Design", desc: "Analyze distributed training memory, speculative serving, KV cache optimization, and training workloads." },
  };

  // 1. Calculate completion status for all sections
  const getSectionCompletionMap = (): Record<string, boolean> => {
    const map: Record<string, boolean> = {};
    for (const key of sectionOrder) {
      const qList = allItems.filter(
        (item) => item.section.toLowerCase().replace(/\s+/g, "-") === key
      );
      const completedCount = qList.filter((item) => completedLearningItems.includes(item.id)).length;
      map[key] = qList.length > 0 && completedCount === qList.length;
    }
    return map;
  };

  const completionMap = getSectionCompletionMap();

  // 2. Build full section details list
  const sections: SectionDetails[] = sectionOrder.map((key) => {
    const qList = allItems.filter(
      (item) => item.section.toLowerCase().replace(/\s+/g, "-") === key
    );
    const completedCount = qList.filter((item) => completedLearningItems.includes(item.id)).length;
    const remainingCount = qList.length - completedCount;
    
    const uncompletedItems = qList.filter((item) => !completedLearningItems.includes(item.id));
    const estimatedMinutesRemaining = uncompletedItems.reduce((acc, item) => acc + item.estimated_time_minutes, 0);

    const prereqs = prerequisites[key] || [];

    // Lock condition: any prerequisite section is not 100% completed
    const isLocked = prereqs.some((preKey) => !completionMap[preKey]);

    const meta = sectionMetadata[key] || { title: key, desc: "" };

    return {
      key,
      title: meta.title,
      description: meta.desc,
      items: qList,
      completedCount,
      totalCount: qList.length,
      remainingCount,
      estimatedMinutesRemaining,
      isLocked,
      prereqs,
    };
  });

  const handleToggle = (key: string) => {
    setExpandedSection(expandedSection === key ? null : key);
  };

  const getPlatformLabel = (platform?: string) => {
    if (!platform) return "Link";
    const labels: Record<string, string> = {
      DEEP_ML: "Deep-ML",
      KAGGLE: "Kaggle",
      HUGGING_FACE: "HuggingFace",
      GITHUB: "GitHub",
      LANGCHAIN: "LangChain",
      LANGGRAPH: "LangGraph",
      LLAMAINDEX: "LlamaIndex",
      CUSTOM: "Custom",
      EXTERNAL: "External",
    };
    return labels[platform] || "Link";
  };

  return (
    <div className="max-w-3xl mx-auto space-y-8 animate-fade-in-up">
      {/* Page Header */}
      <div className="flex items-center gap-3 border-b border-border/40 pb-4">
        <div className="p-2 rounded-xl bg-primary/10 text-primary dark:text-blue-400 border border-primary/20">
          <Layers className="h-6 w-6" />
        </div>
        <div>
          <h1 className="text-2xl font-black tracking-tight">AI Engineer Roadmap</h1>
          <p className="text-xs text-muted-foreground mt-0.5">
            Complete tracks sequentially to unlock advanced machine learning and system design sections.
          </p>
        </div>
      </div>

      {/* Vertical Graph Map */}
      <div className="relative pl-8 sm:pl-12 space-y-8">
        {/* Continuous timeline line */}
        <div className="absolute left-[29px] sm:left-[45px] top-6 bottom-6 w-[2px] bg-border dark:bg-border/30 z-0" />

        {sections.map((sec, idx) => {
          const isExpanded = expandedSection === sec.key;
          const isFullySolved = sec.totalCount > 0 && sec.completedCount === sec.totalCount;
          const percentage = sec.totalCount > 0 ? Math.round((sec.completedCount / sec.totalCount) * 100) : 0;

          return (
            <div key={sec.key} className="relative z-10 space-y-3">
              {/* Timeline dot bubble */}
              <div className="absolute -left-[37px] sm:-left-[53px] top-1">
                <button
                  onClick={() => !sec.isLocked && handleToggle(sec.key)}
                  disabled={sec.isLocked}
                  className={`h-8 w-8 sm:h-10 sm:w-10 rounded-full flex items-center justify-center border transition-all ${
                    sec.isLocked
                      ? "bg-secondary text-muted-foreground/44 border-border cursor-not-allowed"
                      : isFullySolved
                      ? "bg-emerald-500/10 border-emerald-500 text-emerald-500 shadow-md shadow-emerald-500/10"
                      : sec.completedCount > 0
                      ? "bg-primary/10 border-primary text-primary shadow-md shadow-primary/10"
                      : "bg-background border-border text-muted-foreground hover:border-primary"
                  }`}
                >
                  {sec.isLocked ? (
                    <Lock className="h-4 w-4" />
                  ) : isFullySolved ? (
                    <CheckCircle className="h-4.5 w-4.5" />
                  ) : (
                    <Unlock className="h-4 w-4" />
                  )}
                </button>
              </div>

              {/* Card Container */}
              <div
                className={`glass-card rounded-2xl border transition-all duration-200 overflow-hidden ${
                  sec.isLocked
                    ? "opacity-50 hover:translate-y-0"
                    : isExpanded
                    ? "border-primary/50 shadow-lg"
                    : "border-border/40"
                }`}
              >
                {/* Node Summary header */}
                <div
                  onClick={() => !sec.isLocked && handleToggle(sec.key)}
                  className={`p-4 sm:p-5 flex items-center justify-between gap-4 select-none ${
                    sec.isLocked ? "cursor-not-allowed" : "cursor-pointer"
                  }`}
                >
                  <div className="space-y-1.5 flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] font-bold text-muted-foreground uppercase tracking-widest">
                        Track 0{idx + 1}
                      </span>
                      {sec.prereqs.length > 0 && sec.isLocked && (
                        <span className="text-[9px] font-semibold text-rose-500 bg-rose-500/10 px-1.5 py-0.5 rounded border border-rose-500/20">
                          Prerequisites Locked
                        </span>
                      )}
                    </div>
                    <h3 className="font-extrabold text-base sm:text-lg text-foreground flex items-center gap-2">
                      {sec.title}
                    </h3>
                    <p className="text-xs text-muted-foreground leading-normal max-w-xl">
                      {sec.description}
                    </p>

                    {/* Progress Bar & Stats */}
                    {!sec.isLocked && (
                      <div className="flex items-center gap-3 pt-2 max-w-sm">
                        <div className="h-1.5 w-32 overflow-hidden rounded-full bg-secondary border border-border/10">
                          <div
                            className="h-full bg-gradient-to-r from-primary to-cyan-400 transition-all duration-500"
                            style={{ width: `${percentage}%` }}
                          />
                        </div>
                        <span className="text-[10px] text-muted-foreground font-semibold">
                          {percentage}% Done
                        </span>
                      </div>
                    )}
                  </div>

                  <div className="flex items-center gap-4 shrink-0">
                    <div className="text-right text-xs">
                      <div className="font-bold text-foreground">
                        {sec.completedCount}/{sec.totalCount} Completed
                      </div>
                      {!sec.isLocked && sec.remainingCount > 0 && (
                        <div className="text-[10px] text-muted-foreground flex items-center justify-end gap-1 mt-0.5">
                          <Clock className="h-3 w-3" />
                          <span>{(sec.estimatedMinutesRemaining / 60).toFixed(1)} hrs left</span>
                        </div>
                      )}
                    </div>

                    {!sec.isLocked && (
                      <div className="text-muted-foreground">
                        {isExpanded ? <ChevronUp className="h-5 w-5" /> : <ChevronDown className="h-5 w-5" />}
                      </div>
                    )}
                  </div>
                </div>

                {/* Node Expanded list of learning items */}
                {isExpanded && !sec.isLocked && (
                  <div className="border-t border-border/30 bg-secondary/10 p-4 sm:p-5 space-y-2.5">
                    <h4 className="text-xs font-bold uppercase tracking-wider text-muted-foreground mb-3">
                      Section Resources
                    </h4>
                    <div className="grid grid-cols-1 gap-2">
                      {sec.items.map((item) => {
                        const solved = completedLearningItems.includes(item.id);
                        return (
                          <div
                            key={item.id}
                            className="flex items-center justify-between p-3 rounded-xl border border-border/40 bg-background/50 hover:bg-background transition-all text-xs sm:text-sm group"
                          >
                            <div className="flex items-center gap-3 flex-1 min-w-0">
                              <CheckCircle
                                className={`h-4.5 w-4.5 shrink-0 ${
                                  solved ? "text-emerald-500" : "text-muted-foreground/20"
                                }`}
                              />
                              <Link
                                href={`/learning-items/${item.slug}`}
                                className="font-bold text-foreground hover:text-primary hover:underline truncate"
                              >
                                {item.title}
                              </Link>
                              <span className="bg-secondary px-1.5 py-0.5 rounded text-[9px] font-semibold text-muted-foreground border border-border/10 shrink-0">
                                {getPlatformLabel(item.practice_resource?.platform)}
                              </span>
                            </div>

                            <Link
                              href={`/learning-items/${item.slug}`}
                              className="rounded-lg bg-primary/10 text-primary dark:text-blue-400 px-3 py-1.5 text-xs font-bold hover:bg-primary/20 transition-all flex items-center gap-1 shrink-0"
                            >
                              <Play className="h-3 w-3" />
                              Study
                            </Link>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
