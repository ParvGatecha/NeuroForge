"use client";

import React, { useState, useEffect } from "react";
import {
  ASSESSMENT_QUESTIONS,
  AssessmentQuestion,
  computeAssessmentResult,
  AssessmentResult,
} from "../assessment-data";
import {
  Sparkles,
  ChevronRight,
  ChevronLeft,
  CheckCircle2,
  Clock,
  Zap,
} from "lucide-react";

interface AssessmentQuizProps {
  onComplete: (result: AssessmentResult, answers: { [id: number]: string }) => void;
}

export function AssessmentQuiz({ onComplete }: AssessmentQuizProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<{ [questionId: number]: string }>({});
  const [showExplanation, setShowExplanation] = useState(false);
  const [timeSpentSeconds, setTimeSpentSeconds] = useState(0);

  // Timer
  useEffect(() => {
    const timer = setInterval(() => {
      setTimeSpentSeconds((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const currentQ: AssessmentQuestion = ASSESSMENT_QUESTIONS[currentIndex];
  const selectedOption = answers[currentQ.id];
  const isAnswered = selectedOption !== undefined;
  const answeredCount = Object.keys(answers).length;
  const totalQuestions = ASSESSMENT_QUESTIONS.length;
  const progressPercent = Math.round((answeredCount / totalQuestions) * 100);

  const handleSelectOption = (optionId: string) => {
    setAnswers((prev) => ({
      ...prev,
      [currentQ.id]: optionId,
    }));
  };

  const handleNext = () => {
    setShowExplanation(false);
    if (currentIndex < totalQuestions - 1) {
      setCurrentIndex((prev) => prev + 1);
    } else {
      finishAssessment();
    }
  };

  const handlePrev = () => {
    setShowExplanation(false);
    if (currentIndex > 0) {
      setCurrentIndex((prev) => prev - 1);
    }
  };

  const finishAssessment = () => {
    const result = computeAssessmentResult(answers);
    onComplete(result, answers);
  };

  const formatTime = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}:${s < 10 ? "0" : ""}${s}`;
  };

  const getDifficultyBadge = (diff: string) => {
    switch (diff) {
      case "Easy":
        return "bg-emerald-500/10 text-emerald-400 border-emerald-500/20";
      case "Hard":
        return "bg-rose-500/10 text-rose-400 border-rose-500/20";
      case "Medium":
      default:
        return "bg-amber-500/10 text-amber-400 border-amber-500/20";
    }
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 animate-fade-in-up">
      {/* Top Header / Progress Bar */}
      <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card/70 backdrop-blur-md shadow-xl">
        <div className="flex flex-wrap items-center justify-between gap-3 text-xs font-semibold">
          <div className="flex items-center gap-2">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-primary/10 text-primary dark:text-blue-400 border border-primary/20">
              <Zap className="h-3.5 w-3.5" />
              Question {currentIndex + 1} of {totalQuestions}
            </span>
            <span className="text-muted-foreground hidden sm:inline">
              Track: <strong className="text-foreground">{currentQ.trackTitle}</strong>
            </span>
          </div>

          <div className="flex items-center gap-3">
            <div className="flex items-center gap-1.5 text-muted-foreground">
              <Clock className="h-3.5 w-3.5" />
              <span>{formatTime(timeSpentSeconds)}</span>
            </div>
            <span className="text-primary font-bold">{progressPercent}% Completed</span>
          </div>
        </div>

        {/* Linear Progress Bar */}
        <div className="mt-3.5 h-2 w-full overflow-hidden rounded-full bg-secondary/80">
          <div
            className="h-full bg-gradient-to-r from-primary via-indigo-400 to-cyan-400 transition-all duration-300"
            style={{ width: `${((currentIndex + 1) / totalQuestions) * 100}%` }}
          />
        </div>
      </div>

      {/* Question Card */}
      <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-border/50 bg-card/90 backdrop-blur-md shadow-2xl relative overflow-hidden">
        <div className="flex items-center justify-between gap-2 mb-4">
          <span className="text-xs uppercase font-extrabold tracking-wider text-primary">
            {currentQ.trackTitle}
          </span>
          <span className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold border ${getDifficultyBadge(currentQ.difficulty)}`}>
            {currentQ.difficulty}
          </span>
        </div>

        <h2 className="text-lg sm:text-xl font-bold leading-snug text-foreground mb-6">
          {currentQ.question}
        </h2>

        {/* Code Snippet if present */}
        {currentQ.codeSnippet && (
          <div className="mb-6 rounded-xl bg-muted/60 p-4 font-mono text-xs overflow-x-auto border border-border/40">
            <pre>{currentQ.codeSnippet}</pre>
          </div>
        )}

        {/* Options Grid */}
        <div className="space-y-3">
          {currentQ.options.map((option) => {
            const isSelected = selectedOption === option.id;
            return (
              <button
                key={option.id}
                onClick={() => handleSelectOption(option.id)}
                className={`w-full text-left p-4 rounded-xl border transition-all flex items-start gap-3.5 ${
                  isSelected
                    ? "bg-primary/10 border-primary text-foreground shadow-md shadow-primary/10 ring-1 ring-primary/40"
                    : "border-border/60 bg-background/50 hover:bg-secondary/70 hover:border-border text-foreground/90"
                }`}
              >
                <span
                  className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-lg text-xs font-bold transition-colors ${
                    isSelected
                      ? "bg-primary text-primary-foreground shadow"
                      : "bg-secondary text-muted-foreground"
                  }`}
                >
                  {option.id}
                </span>
                <span className="text-sm font-medium leading-relaxed">{option.text}</span>
              </button>
            );
          })}
        </div>

        {/* Explanation Toggle */}
        {isAnswered && (
          <div className="mt-5 pt-4 border-t border-border/40">
            <button
              onClick={() => setShowExplanation(!showExplanation)}
              className="text-xs font-semibold text-primary dark:text-blue-400 hover:underline flex items-center gap-1.5"
            >
              <Sparkles className="h-3.5 w-3.5" />
              {showExplanation ? "Hide Explanation" : "Peek Explanation & Deep Dive"}
            </button>

            {showExplanation && (
              <div className="mt-3 p-4 rounded-xl bg-secondary/50 border border-border/40 text-xs leading-relaxed space-y-1.5 animate-fade-in-up">
                <div className="flex items-center gap-2 font-bold text-foreground">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>Correct Option: {currentQ.correctOptionId}</span>
                </div>
                <p className="text-muted-foreground">{currentQ.explanation}</p>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Navigation Buttons */}
      <div className="flex items-center justify-between gap-3 pt-2">
        <button
          onClick={handlePrev}
          disabled={currentIndex === 0}
          className="inline-flex items-center gap-2 rounded-xl border border-border/60 bg-background/60 px-5 py-3 text-sm font-bold text-muted-foreground hover:text-foreground hover:bg-secondary disabled:opacity-30 disabled:pointer-events-none transition-all"
        >
          <ChevronLeft className="h-4 w-4" />
          Previous
        </button>

        <div className="flex items-center gap-2">
          {currentIndex === totalQuestions - 1 ? (
            <button
              onClick={finishAssessment}
              disabled={answeredCount === 0}
              className="inline-flex items-center gap-2 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 px-7 py-3 text-sm font-bold text-white hover:opacity-95 shadow-lg shadow-emerald-500/20 transition-all disabled:opacity-40"
            >
              Generate AI Profile
              <CheckCircle2 className="h-4 w-4" />
            </button>
          ) : (
            <button
              onClick={handleNext}
              className="inline-flex items-center gap-2 rounded-xl bg-primary px-6 py-3 text-sm font-bold text-primary-foreground hover:bg-primary/95 shadow-lg shadow-primary/20 transition-all"
            >
              {isAnswered ? "Next Question" : "Skip / Next"}
              <ChevronRight className="h-4 w-4" />
            </button>
          )}
        </div>
      </div>

      {/* Question Quick Jump Pills */}
      <div className="glass-panel rounded-2xl p-4 border border-border/30 bg-card/40">
        <p className="text-[11px] uppercase font-bold tracking-wider text-muted-foreground mb-2 text-center">
          Jump to Question
        </p>
        <div className="flex flex-wrap items-center justify-center gap-1.5">
          {ASSESSMENT_QUESTIONS.map((q, idx) => {
            const answered = answers[q.id] !== undefined;
            const isCurrent = idx === currentIndex;
            return (
              <button
                key={q.id}
                onClick={() => {
                  setShowExplanation(false);
                  setCurrentIndex(idx);
                }}
                className={`h-8 w-8 rounded-lg text-xs font-bold transition-all flex items-center justify-center ${
                  isCurrent
                    ? "bg-primary text-primary-foreground shadow-md ring-2 ring-primary/40"
                    : answered
                    ? "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30"
                    : "bg-secondary/60 text-muted-foreground hover:bg-secondary"
                }`}
                title={`Q${idx + 1}: ${q.trackTitle}`}
              >
                {idx + 1}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
