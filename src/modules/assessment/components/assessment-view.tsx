"use client";

import React, { useState } from "react";
import { AssessmentQuiz } from "./assessment-quiz";
import { AssessmentResults } from "./assessment-results";
import { AssessmentResult, AssessmentQuestion, generateAssessmentSession } from "../assessment-data";
import {
  Sparkles,
  Clock,
  ArrowRight,
  BrainCircuit,
  BarChart3,
} from "lucide-react";

export function AssessmentView() {
  const [stage, setStage] = useState<"intro" | "quiz" | "results">("intro");
  const [result, setResult] = useState<AssessmentResult | null>(null);
  const [questions, setQuestions] = useState<AssessmentQuestion[]>([]);

  const handleStart = () => {
    setQuestions(generateAssessmentSession(2));
    setStage("quiz");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleComplete = (assessmentResult: AssessmentResult) => {
    setResult(assessmentResult);
    setStage("results");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleRetake = () => {
    setResult(null);
    setQuestions(generateAssessmentSession(2));
    setStage("quiz");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <div className="py-6">
      {stage === "intro" && (
        <div className="max-w-4xl mx-auto space-y-10 animate-fade-in-up">
          {/* Hero Section */}
          <div className="glass-panel relative overflow-hidden rounded-3xl p-8 sm:p-12 border border-primary/30 bg-card/90 backdrop-blur-xl text-center shadow-2xl space-y-6">
            <div className="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-1.5 text-xs font-bold text-primary dark:text-blue-400 border border-primary/20">
              <Sparkles className="h-4 w-4" />
              100% Free • First-Principles AI Readiness Diagnostic
            </div>

            <div className="space-y-3 max-w-2xl mx-auto">
              <h1 className="text-4xl sm:text-5xl font-black tracking-tight leading-[1.15] text-foreground">
                How AI Engineer Ready Are You?
              </h1>
              <p className="text-base sm:text-lg text-muted-foreground leading-relaxed">
                Take the free 10-minute assessment. Test your first-principles knowledge across 8 core tracks and get your personalized AI engineering profile.
              </p>
            </div>

            {/* Giant Assessment Button */}
            <div className="pt-2">
              <button
                onClick={handleStart}
                className="w-full sm:w-auto inline-flex items-center justify-center gap-3 rounded-2xl bg-gradient-to-r from-primary via-indigo-500 to-cyan-500 px-10 py-5 text-base sm:text-lg font-black text-white hover:opacity-95 shadow-xl shadow-primary/30 transition-all hover:scale-[1.02] cursor-pointer"
              >
                <span>Take the Free 10-Minute Assessment</span>
                <ArrowRight className="h-5 w-5" />
              </button>
            </div>

            <div className="flex flex-wrap items-center justify-center gap-6 text-xs text-muted-foreground pt-4 border-t border-border/40">
              <span className="flex items-center gap-1.5 font-semibold">
                <Clock className="h-4 w-4 text-primary" />
                16 Curated Questions (~10 mins)
              </span>
              <span className="flex items-center gap-1.5 font-semibold">
                <BrainCircuit className="h-4 w-4 text-cyan-400" />
                8 Core AI Engineering Tracks
              </span>
              <span className="flex items-center gap-1.5 font-semibold">
                <BarChart3 className="h-4 w-4 text-emerald-400" />
                Detailed Proficiency Profile
              </span>
            </div>

            {/* Background Ambience */}
            <div className="absolute right-0 top-0 -mr-24 -mt-24 h-64 w-64 rounded-full bg-primary/20 blur-3xl pointer-events-none" />
            <div className="absolute left-0 bottom-0 -ml-24 -mb-24 h-64 w-64 rounded-full bg-cyan-400/15 blur-3xl pointer-events-none" />
          </div>

          {/* 8 Track Evaluation Grid */}
          <div className="space-y-4">
            <div className="text-center space-y-1">
              <h2 className="text-xl font-bold tracking-tight text-foreground">
                What the Assessment Evaluates
              </h2>
              <p className="text-xs text-muted-foreground">
                Rigorous, non-trivial questions calibrated to actual senior AI engineer interviews
              </p>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
              {[
                { name: "Python Concurrency", desc: "GIL, multiprocessing, async event loops", color: "text-blue-400" },
                { name: "Mathematical Stats", desc: "MLE vs MAP, Bayes theorem, p-values", color: "text-purple-400" },
                { name: "Classical ML", desc: "Bias-variance, random forests, recall vs precision", color: "text-emerald-400" },
                { name: "Deep Learning", desc: "Residual backprop, scaled attention math", color: "text-rose-400" },
                { name: "Large Language Models", desc: "LoRA adapters, KV cache decoding", color: "text-violet-400" },
                { name: "RAG Engineering", desc: "Hybrid search, BM25, lost-in-the-middle", color: "text-cyan-400" },
                { name: "AI Agent Systems", desc: "ReAct loops, autonomous tool error recovery", color: "text-indigo-400" },
                { name: "AI System Design", desc: "vLLM PagedAttention, upstream guardrails", color: "text-teal-400" },
              ].map((t) => (
                <div
                  key={t.name}
                  className="rounded-2xl border border-border/50 bg-card p-4 space-y-1.5 transition-all hover:border-primary/30 shadow-sm"
                >
                  <span className={`text-xs font-bold block ${t.color}`}>{t.name}</span>
                  <p className="text-[11px] text-muted-foreground leading-snug">{t.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {stage === "quiz" && (
        <AssessmentQuiz
          key={questions.map((q) => q.id).join("-")}
          questions={questions}
          onComplete={handleComplete}
        />
      )}

      {stage === "results" && result && (
        <AssessmentResults result={result} onRetake={handleRetake} />
      )}
    </div>
  );
}
