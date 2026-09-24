"use client";

import React, { useState } from "react";
import Link from "next/link";
import { AssessmentResult } from "../assessment-data";
import { getAllLearningItems, LearningItemMetadata } from "@/modules/roadmaps/roadmap";
import {
  Share2,
  Copy,
  Check,
  RotateCcw,
  Sparkles,
  ArrowRight,
  Target,
  Zap,
} from "lucide-react";

function LinkedInIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" {...props}>
      <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.45a1.62 1.62 0 0 0-1.63 1.63c0 .9.73 1.63 1.63 1.63.9 0 1.63-.73 1.63-1.63 0-.9-.73-1.63-1.63-1.63Z" />
    </svg>
  );
}

function TwitterXIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" {...props}>
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
    </svg>
  );
}

interface AssessmentResultsProps {
  result: AssessmentResult;
  onRetake: () => void;
}

export function AssessmentResults({ result, onRetake }: AssessmentResultsProps) {
  const [copied, setCopied] = useState(false);

  const allItems = getAllLearningItems();

  // Find 3 recommended learning items addressing the user's weakest tracks
  const recommendedItems: LearningItemMetadata[] = [];
  const weakestKeys = result.trackScores
    .sort((a, b) => a.score - b.score)
    .map((t) => t.key);

  for (const trackKey of weakestKeys) {
    const matching = allItems.filter(
      (item) => item.section.toLowerCase().replace(/\s+/g, "-") === trackKey
    );
    if (matching.length > 0) {
      // Pick 1-2 representative items
      const pick = matching[Math.min(1, matching.length - 1)];
      if (pick && !recommendedItems.some((r) => r.id === pick.id)) {
        recommendedItems.push(pick);
      }
    }
    if (recommendedItems.length >= 4) break;
  }

  // Format ASCII score card
  const generateShareableAscii = () => {
    const bar = (pct: number) => {
      const filled = Math.round(pct / 10);
      const empty = 10 - filled;
      return "█".repeat(filled) + "░".repeat(empty);
    };

    const lines = result.trackScores.map(
      (t) => `${t.title.padEnd(20, " ")} ${bar(t.score)} ${t.score}%`
    );

    return `My TensorTrack AI Engineer Score: ${result.overallScore}% (${result.readinessLevel})\n\n${lines.join("\n")}\n\nFind out how AI-engineer-ready you are:\nhttps://tensor-track.vercel.app/assessment`;
  };

  const handleCopyCard = async () => {
    try {
      await navigator.clipboard.writeText(generateShareableAscii());
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch (e) {
      console.error("Failed to copy card", e);
    }
  };

  const lowestTrack = result.trackScores.reduce((prev, curr) => (prev.score < curr.score ? prev : curr));

  const shareTextLinkedIn = `Apparently I'm only ${lowestTrack.score}% ready for ${lowestTrack.title} 😂\n\nI just took the TensorTrack AI Engineer Assessment and scored ${result.overallScore}% overall (${result.readinessLevel}).\n\nCheck how AI-engineer-ready you are:`;
  const linkedInShareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent("https://tensor-track.vercel.app/assessment")}&text=${encodeURIComponent(shareTextLinkedIn)}`;

  const tweetText = `Apparently I'm only ${lowestTrack.score}% ready for ${lowestTrack.title} 😂\n\nTook the free TensorTrack AI Engineer Readiness Assessment (Overall: ${result.overallScore}% - ${result.readinessLevel}).\n\nCheck your score:`;
  const twitterShareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(tweetText)}&url=${encodeURIComponent("https://tensor-track.vercel.app/assessment")}`;

  return (
    <div className="max-w-4xl mx-auto space-y-8 animate-fade-in-up">
      {/* Top Banner / Hero Profile Card */}
      <div className="glass-panel relative overflow-hidden rounded-3xl p-8 sm:p-10 border border-primary/30 bg-card/90 backdrop-blur-xl shadow-2xl">
        <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="space-y-3 text-center md:text-left">
            <div className="inline-flex items-center gap-2 rounded-full bg-primary/10 px-3.5 py-1 text-xs font-extrabold text-primary dark:text-blue-400 border border-primary/20">
              <Sparkles className="h-3.5 w-3.5" />
              YOUR AI ENGINEERING PROFILE
            </div>

            <h1 className="text-3xl sm:text-4xl font-black tracking-tight text-foreground">
              {result.readinessLevel}
            </h1>

            <p className="max-w-xl text-sm sm:text-base text-muted-foreground leading-relaxed">
              {result.readinessSummary}
            </p>

            <div className="flex flex-wrap items-center justify-center md:justify-start gap-4 pt-2 text-xs font-semibold">
              <div className="flex items-center gap-1.5 text-emerald-400">
                <Check className="h-4 w-4" />
                <span>Strongest: {result.strongestTracks.join(", ")}</span>
              </div>
              <div className="flex items-center gap-1.5 text-rose-400">
                <Target className="h-4 w-4" />
                <span>Priority Gaps: {result.weakestTracks.join(", ")}</span>
              </div>
            </div>
          </div>

          {/* Radial / Score Badge */}
          <div className="flex flex-col items-center justify-center shrink-0">
            <div className="relative flex h-36 w-36 items-center justify-center rounded-full bg-gradient-to-tr from-primary/20 via-indigo-500/20 to-cyan-500/20 p-2 shadow-inner border border-primary/30">
              <div className="flex h-full w-full flex-col items-center justify-center rounded-full bg-card/90 border border-border/40 shadow-xl">
                <span className="text-4xl font-black text-transparent bg-clip-text bg-gradient-to-r from-primary to-cyan-400">
                  {result.overallScore}%
                </span>
                <span className="text-[10px] font-extrabold uppercase tracking-widest text-muted-foreground mt-0.5">
                  Readiness
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Ambient glow */}
        <div className="absolute right-0 top-0 -mr-20 -mt-20 h-64 w-64 rounded-full bg-primary/15 blur-3xl" />
        <div className="absolute left-0 bottom-0 -ml-20 -mb-20 h-64 w-64 rounded-full bg-cyan-400/10 blur-3xl" />
      </div>

      {/* TRACK BY TRACK BREAKDOWN */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border border-border/50 bg-card space-y-6 shadow-xl">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-black tracking-tight text-foreground">
              Track Proficiency Breakdown
            </h2>
            <p className="text-xs text-muted-foreground mt-0.5">
              Calibrated against production AI Engineering requirements
            </p>
          </div>
          <span className="text-xs font-bold text-primary">8 Core Tracks</span>
        </div>

        <div className="space-y-4">
          {result.trackScores.map((track) => {
            return (
              <div key={track.key} className="space-y-1.5">
                <div className="flex items-center justify-between text-xs font-bold">
                  <div className="flex items-center gap-2">
                    <span className="text-foreground">{track.title}</span>
                    <span
                      className={`text-[10px] px-2 py-0.5 rounded-full border ${
                        track.score >= 80
                          ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                          : track.score >= 50
                          ? "bg-blue-500/10 text-blue-400 border-blue-500/20"
                          : track.score >= 25
                          ? "bg-amber-500/10 text-amber-400 border-amber-500/20"
                          : "bg-rose-500/10 text-rose-400 border-rose-500/20"
                      }`}
                    >
                      {track.status}
                    </span>
                  </div>
                  <span className="font-mono text-sm font-black text-foreground">
                    {track.score}%
                  </span>
                </div>

                {/* Progress Track */}
                <div className="h-3 w-full overflow-hidden rounded-full bg-secondary/80 border border-border/40">
                  <div
                    className={`h-full bg-gradient-to-r ${track.color} transition-all duration-700`}
                    style={{ width: `${Math.max(5, track.score)}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* VIRAL SHARE SECTION */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border border-primary/30 bg-gradient-to-b from-primary/5 via-card to-card space-y-5 shadow-xl">
        <div className="text-center sm:text-left space-y-1">
          <h3 className="text-lg font-black text-foreground flex items-center justify-center sm:justify-start gap-2">
            <Share2 className="h-5 w-5 text-primary" />
            Share Your Assessment Score
          </h3>
          <p className="text-xs text-muted-foreground">
            Compare your score with peers on LinkedIn, Twitter, or engineering Discords.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          {/* LinkedIn */}
          <a
            href={linkedInShareUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="flex-1 min-w-[180px] inline-flex items-center justify-center gap-2 rounded-xl bg-[#0A66C2] px-5 py-3 text-xs font-bold text-white hover:bg-[#0A66C2]/90 transition-all shadow-md shadow-[#0A66C2]/20"
          >
            <LinkedInIcon className="h-4 w-4" />
            Share on LinkedIn
          </a>

          {/* Twitter / X */}
          <a
            href={twitterShareUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="flex-1 min-w-[180px] inline-flex items-center justify-center gap-2 rounded-xl bg-black dark:bg-zinc-800 px-5 py-3 text-xs font-bold text-white hover:bg-zinc-900 transition-all border border-border/40 shadow-md"
          >
            <TwitterXIcon className="h-4 w-4" />
            Share on X (Twitter)
          </a>

          {/* Copy ASCII Card */}
          <button
            onClick={handleCopyCard}
            className="flex-1 min-w-[180px] inline-flex items-center justify-center gap-2 rounded-xl border border-border bg-background/80 hover:bg-secondary px-5 py-3 text-xs font-bold text-foreground transition-all"
          >
            {copied ? (
              <>
                <Check className="h-4 w-4 text-emerald-400" />
                Copied Card!
              </>
            ) : (
              <>
                <Copy className="h-4 w-4 text-muted-foreground" />
                Copy Score Card
              </>
            )}
          </button>
        </div>
      </div>

      {/* RECOMMENDED TENSORTRACK PATH */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border border-border/50 bg-card space-y-6 shadow-xl">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
          <div>
            <div className="inline-flex items-center gap-1.5 text-xs font-extrabold text-primary mb-1">
              <Zap className="h-3.5 w-3.5" />
              RECOMMENDED TENSORTRACK PATH
            </div>
            <h2 className="text-xl font-black text-foreground">
              Your Personalized Learning Blueprint
            </h2>
          </div>
          <Link
            href="/learning-items"
            className="text-xs font-bold text-primary hover:underline inline-flex items-center gap-1"
          >
            Browse All 200 Items
            <ArrowRight className="h-3.5 w-3.5" />
          </Link>
        </div>

        <p className="text-xs text-muted-foreground">
          Based on your lowest-scoring tracks, here are the top curated resources from the TensorTrack curriculum to eliminate your architectural blindspots:
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {recommendedItems.map((item) => (
            <div
              key={item.id}
              className="group rounded-2xl border border-border/60 bg-secondary/30 hover:bg-secondary/60 p-5 transition-all hover:border-primary/40 flex flex-col justify-between space-y-4"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[10px] font-extrabold uppercase tracking-wider text-primary">
                    {item.section}
                  </span>
                  <span
                    className={`text-[10px] px-2 py-0.5 rounded-full font-bold border ${
                      item.difficulty === "Easy"
                        ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                        : item.difficulty === "Hard"
                        ? "bg-rose-500/10 text-rose-400 border-rose-500/20"
                        : "bg-amber-500/10 text-amber-400 border-amber-500/20"
                    }`}
                  >
                    {item.difficulty}
                  </span>
                </div>

                <h4 className="text-sm font-bold text-foreground group-hover:text-primary transition-colors line-clamp-1">
                  {item.title}
                </h4>

                <p className="text-xs text-muted-foreground line-clamp-2 leading-relaxed">
                  {item.description}
                </p>
              </div>

              <div className="flex items-center justify-between pt-2 border-t border-border/40 text-xs">
                <span className="text-muted-foreground text-[11px]">
                  ~{item.estimated_time_minutes} mins
                </span>
                <Link
                  href={`/learning-items/${item.slug}`}
                  className="font-bold text-primary group-hover:underline inline-flex items-center gap-1"
                >
                  Start Item
                  <ArrowRight className="h-3.5 w-3.5" />
                </Link>
              </div>
            </div>
          ))}
        </div>

        {/* Start Roadmap CTA */}
        <div className="pt-4 flex flex-col sm:flex-row items-center justify-between gap-4 border-t border-border/40">
          <div className="text-xs text-muted-foreground text-center sm:text-left">
            Ready to track your progress and level up with XP?
          </div>
          <div className="flex items-center gap-3">
            <button
              onClick={onRetake}
              className="inline-flex items-center gap-1.5 rounded-xl border border-border bg-background px-4 py-2.5 text-xs font-bold text-muted-foreground hover:text-foreground hover:bg-secondary transition-all"
            >
              <RotateCcw className="h-3.5 w-3.5" />
              Retake Assessment
            </button>
            <Link
              href="/dashboard"
              className="inline-flex items-center gap-1.5 rounded-xl bg-primary px-5 py-2.5 text-xs font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/20"
            >
              Go to Dashboard
              <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
