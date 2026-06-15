import React from "react";
import Link from "next/link";
import { Metadata } from "next";
import {
  GraduationCap,
  ArrowRight,
  Flame,
  Terminal,
  Trophy,
  ShieldCheck,
  Cpu,
  Binary,
  Layers,
  Bot,
  Sparkles,
} from "lucide-react";

export const metadata: Metadata = {
  title: 'TensorTrack — AI Engineer Roadmap & Learning Platform',
  description: 'Go from Python basics to building AI agents. TensorTrack gives you a structured, first-principles curriculum for becoming an AI engineer — with XP tracking and curated resources.',
  alternates: {
    canonical: 'https://tensor-track.vercel.app',
  },
  verification: {
    google: '4K9KQwXmaycyqJ8k5XFxwk_4H1k2PQytG7UPj0jCDp8',
  },
};

export default function Home() {
  const tracks = [
    { name: "Python Concurrency", count: "10 Items", icon: Binary, desc: "GIL, asyncio, generators, decorators" },
    { name: "Mathematical Stats", count: "15 Items", icon: Cpu, desc: "MLE, Bayesian, Hypothesis testing, MCMC" },
    { name: "Classical ML", count: "20 Items", icon: Layers, desc: "Gradient descent, SVMs, trees, expectations" },
    { name: "Deep Learning", count: "15 Items", icon: Cpu, desc: "Backprop, Adam, CNNs, LSTMs, Transformers" },
    { name: "Large Language Models", count: "15 Items", icon: Bot, desc: "Tokenizers, RLHF, Quantization, MoE, FlashAttention" },
    { name: "RAG Engineering", count: "10 Items", icon: Layers, desc: "Chunking, Vector search, Hybrid, Reranking, GraphRAG" },
    { name: "AI Agent Systems", count: "10 Items", icon: Bot, desc: "ReAct loop, function calling, stateful graphs" },
    { name: "AI System Design", count: "5 Items", icon: ShieldCheck, desc: "Scalability, serving, caching, distributed training" },
  ];

  return (
    <div className="flex flex-col min-h-screen bg-background text-foreground bg-grid-pattern">
      {/* Landing Navigation Header */}
      <header className="w-full border-b border-border/40 bg-background/80 backdrop-blur-md sticky top-0 z-50">
        <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
          <div className="flex items-center gap-2">
            <GraduationCap className="h-6 w-6 text-primary" />
            <span className="bg-gradient-to-r from-primary to-cyan-400 bg-clip-text text-xl font-extrabold tracking-tight text-transparent">
              TensorTrack
            </span>
          </div>
          <div className="flex items-center gap-4">
            <Link
              href="/learning-items"
              className="text-sm font-semibold text-muted-foreground hover:text-foreground transition-colors"
            >
              Explore Tracks
            </Link>
            <Link
              href="/dashboard"
              className="rounded-xl bg-primary px-4 py-2 text-xs font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/20"
            >
              Enter Dashboard
            </Link>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-1">
        <section className="relative overflow-hidden py-24 sm:py-32">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center space-y-8 relative z-10 animate-fade-in-up">
            <div className="mx-auto max-w-3xl space-y-4">
              <div className="inline-flex items-center gap-1.5 rounded-full bg-primary/10 px-3 py-1 text-xs font-semibold text-primary dark:text-blue-400 border border-primary/20">
                <Sparkles className="h-3.5 w-3.5" />
                100 Curated Resources Pre-loaded
              </div>
              <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[1.1] text-foreground">
                Master AI Engineering.
                <span className="block bg-gradient-to-r from-primary via-indigo-400 to-cyan-400 bg-clip-text text-transparent mt-1">
                  Step-by-Step.
                </span>
              </h1>
              <p className="mx-auto mt-4 max-w-xl text-base sm:text-lg text-muted-foreground leading-relaxed">
                TensorTrack curates the best educational resources on the internet and organizes them into a guided learning path. Track your progress, build streaks, and verify objectives.
              </p>
            </div>

            {/* Hero CTAs */}
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link
                href="/dashboard"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl bg-primary px-6 py-3.5 text-sm font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-lg shadow-primary/25"
              >
                Get Started Free
                <ArrowRight className="h-4 w-4" />
              </Link>
              <Link
                href="/learning-items"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl border border-border bg-background/50 hover:bg-secondary px-6 py-3.5 text-sm font-bold text-muted-foreground hover:text-foreground transition-all"
              >
                Browse Curriculum
              </Link>
            </div>
          </div>

          {/* Decorative glowing backdrops */}
          <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-primary/10 rounded-full blur-3xl pointer-events-none -z-10" />
          <div className="absolute right-0 top-0 w-96 h-96 bg-cyan-400/5 rounded-full blur-3xl pointer-events-none -z-10" />
        </section>

        {/* Feature Cards Grid Section */}
        <section className="py-16 sm:py-20 border-t border-border/40 bg-muted/10">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 space-y-12">
            <div className="text-center space-y-2 max-w-xl mx-auto">
              <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">Structured for Retention</h2>
              <p className="text-sm text-muted-foreground">
                Move past copy-pasting API keys. Learn the internal mathematical and systems foundations of AI.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {/* Feature 1 */}
              <div className="glass-card rounded-2xl border border-border/40 p-6 bg-card space-y-4">
                <div className="h-10 w-10 rounded-xl bg-primary/10 flex items-center justify-center text-primary dark:text-blue-400 border border-primary/20">
                  <Terminal className="h-5 w-5" />
                </div>
                <h3 className="font-bold text-base">Curated Learning Hub</h3>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Access top tutorials, documentation, papers, and exercises across the web from a single dashboard.
                </p>
              </div>

              {/* Feature 2 */}
              <div className="glass-card rounded-2xl border border-border/40 p-6 bg-card space-y-4">
                <div className="h-10 w-10 rounded-xl bg-primary/10 flex items-center justify-center text-primary dark:text-blue-400 border border-primary/20">
                  <Flame className="h-5 w-5" />
                </div>
                <h3 className="font-bold text-base">Gamified Streaks & XP</h3>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Track your learning consistency with daily streaks, earn XP for completions, level up, and unlock prestigious achievements.
                </p>
              </div>

              {/* Feature 3 */}
              <div className="glass-card rounded-2xl border border-border/40 p-6 bg-card space-y-4">
                <div className="h-10 w-10 rounded-xl bg-primary/10 flex items-center justify-center text-primary dark:text-blue-400 border border-primary/20">
                  <Trophy className="h-5 w-5" />
                </div>
                <h3 className="font-bold text-base">First-Principles Curriculum</h3>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Carefully structured tracks covering Math, stats, Classical ML, deep learning foundations, and advanced LLM Agent architectures.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Tracks / Curriculum Grid */}
        <section className="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
          <div className="text-center space-y-2 max-w-xl mx-auto">
            <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">Curriculum Map</h2>
            <p className="text-sm text-muted-foreground">
              Explore 8 dedicated disciplines structured linearly to mirror industry expectations.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {tracks.map((track, i) => {
              const Icon = track.icon;
              return (
                <div
                  key={i}
                  className="glass-card rounded-xl border border-border/40 p-5 bg-card flex flex-col justify-between h-44 hover:border-primary/40"
                >
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <div className="p-2 rounded-lg bg-secondary text-muted-foreground">
                        <Icon className="h-4.5 w-4.5" />
                      </div>
                      <span className="text-[10px] font-bold text-primary dark:text-blue-400 bg-primary/10 px-2 py-0.5 rounded">
                        {track.count}
                      </span>
                    </div>
                    <h3 className="font-bold text-sm text-foreground mt-2">{track.name}</h3>
                    <p className="text-xs text-muted-foreground leading-normal">{track.desc}</p>
                  </div>
                  <Link
                    href={`/learning-items?section=${track.name.toLowerCase().replace(/\s+/g, "-")}`}
                    className="text-xs font-bold text-primary dark:text-blue-400 inline-flex items-center gap-1 hover:underline pt-2"
                  >
                    Explore Track
                    <ArrowRight className="h-3 w-3" />
                  </Link>
                </div>
              );
            })}
          </div>
        </section>
      </main>

      {/* Landing Footer */}
      <footer className="border-t border-border/40 bg-muted/20 py-8 px-4 sm:px-6 lg:px-8 text-center text-xs text-muted-foreground">
        <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
          <span className="font-semibold">© 2026 TensorTrack. All rights reserved.</span>
          <div className="flex items-center gap-4">
            <Link href="/learning-items" className="hover:underline">Learning Items</Link>
            <Link href="/dashboard" className="hover:underline">Dashboard</Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
