"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/shared/lib/supabase/client";
import {
  GraduationCap,
  Mail,
  Lock,
  ArrowRight,
  User,
  ShieldAlert,
  CheckCircle,
} from "lucide-react";
import Link from "next/link";

export default function LoginPage() {
  const router = useRouter();
  const supabase = createClient();

  const [isSignUp, setIsSignUp] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const [successMsg, setSuccessMsg] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAuth = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg("");
    setSuccessMsg("");
    setLoading(true);

    try {
      if (isSignUp) {
        // Sign up
        const { data, error } = await supabase.auth.signUp({
          email,
          password,
          options: {
            data: {
              name: name || email.split("@")[0],
            },
          },
        });

        if (error) {
          setErrorMsg(error.message);
        } else {
          setSuccessMsg("Account created! Check your email for verification link or sign in.");
          setEmail("");
          setPassword("");
          setName("");
        }
      } else {
        // Sign in
        const { data, error } = await supabase.auth.signInWithPassword({
          email,
          password,
        });

        if (error) {
          setErrorMsg(error.message);
        } else {
          // Success
          const params = new URLSearchParams(window.location.search);
          const next = params.get("next") || "/dashboard";
          router.push(next);
          router.refresh();
        }
      }
    } catch (err: any) {
      setErrorMsg(err.message || "An unexpected error occurred.");
    } finally {
      setLoading(false);
    }
  };

  const handleOAuth = async (provider: "google" | "github") => {
    setErrorMsg("");
    try {
      const { error } = await supabase.auth.signInWithOAuth({
        provider,
        options: {
          redirectTo: `${window.location.origin}/auth/callback`,
        },
      });
      if (error) setErrorMsg(error.message);
    } catch (err: any) {
      setErrorMsg(err.message || "OAuth redirection failed.");
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-4 bg-grid-pattern relative overflow-hidden">
      {/* Glow Effects */}
      <div className="absolute left-1/3 top-1/4 h-96 w-96 rounded-full bg-primary/10 blur-[120px] pointer-events-none -z-10" />
      <div className="absolute right-1/3 bottom-1/4 h-96 w-96 rounded-full bg-cyan-400/5 blur-[120px] pointer-events-none -z-10" />

      {/* Main card */}
      <div className="w-full max-w-md glass-panel rounded-3xl border border-border/40 p-8 shadow-2xl relative z-10 animate-fade-in-up">
        {/* Brand */}
        <div className="flex flex-col items-center text-center mb-8">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-primary/10 border border-primary/20 text-primary mb-3 shadow-md shadow-primary/10">
            <GraduationCap className="h-6 w-6" />
          </div>
          <h1 className="text-2xl font-black tracking-tight text-foreground bg-gradient-to-r from-primary to-cyan-400 bg-clip-text text-transparent">
            TensorTrack
          </h1>
          <p className="mt-1.5 text-xs text-muted-foreground max-w-[280px]">
            Master AI Engineering step-by-step with structured analytics.
          </p>
        </div>

        {/* Error / Success Notifications */}
        {errorMsg && (
          <div className="mb-5 flex items-start gap-2.5 rounded-xl bg-destructive/10 border border-destructive/20 p-3 text-xs text-destructive font-medium">
            <ShieldAlert className="h-4 w-4 shrink-0 mt-0.5" />
            <span>{errorMsg}</span>
          </div>
        )}

        {successMsg && (
          <div className="mb-5 flex items-start gap-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 p-3 text-xs text-emerald-500 font-medium">
            <CheckCircle className="h-4 w-4 shrink-0 mt-0.5" />
            <span>{successMsg}</span>
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleAuth} className="space-y-4">
          {isSignUp && (
            <div className="space-y-1.5">
              <label htmlFor="name" className="text-xs font-bold text-muted-foreground uppercase tracking-wider pl-1">
                Full Name
              </label>
              <div className="relative">
                <User className="absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground/50" />
                <input
                  id="name"
                  type="text"
                  placeholder="Alex AI"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="w-full h-11 pl-10 pr-4 rounded-xl border border-border bg-background/50 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-all text-sm"
                  required
                />
              </div>
            </div>
          )}

          <div className="space-y-1.5">
            <label htmlFor="email" className="text-xs font-bold text-muted-foreground uppercase tracking-wider pl-1">
              Email Address
            </label>
            <div className="relative">
              <Mail className="absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground/50" />
              <input
                id="email"
                type="email"
                placeholder="alex@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full h-11 pl-10 pr-4 rounded-xl border border-border bg-background/50 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-all text-sm"
                required
              />
            </div>
          </div>

          <div className="space-y-1.5">
            <div className="flex justify-between items-center px-1">
              <label htmlFor="password" className="text-xs font-bold text-muted-foreground uppercase tracking-wider">
                Password
              </label>
              {!isSignUp && (
                <Link
                  href="/login/reset"
                  className="text-xs text-primary dark:text-blue-400 hover:underline font-semibold"
                >
                  Forgot Password?
                </Link>
              )}
            </div>
            <div className="relative">
              <Lock className="absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground/50" />
              <input
                id="password"
                type="password"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full h-11 pl-10 pr-4 rounded-xl border border-border bg-background/50 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-all text-sm"
                required
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full h-11 bg-primary text-primary-foreground font-bold rounded-xl flex items-center justify-center gap-1.5 hover:bg-primary/95 transition-all shadow-md shadow-primary/25 disabled:opacity-50 disabled:cursor-not-allowed mt-2 cursor-pointer"
          >
            <span>{loading ? "Please wait..." : isSignUp ? "Create Account" : "Sign In"}</span>
            {!loading && <ArrowRight className="h-4 w-4" />}
          </button>
        </form>

        {/* Separator */}
        <div className="relative flex items-center my-6">
          <div className="flex-grow border-t border-border/40"></div>
          <span className="flex-shrink mx-4 text-[10px] text-muted-foreground font-bold uppercase tracking-widest">
            Or Continue With
          </span>
          <div className="flex-grow border-t border-border/40"></div>
        </div>

        {/* OAuth Buttons */}
        <div className="grid grid-cols-2 gap-3 mb-6">
          <button
            onClick={() => handleOAuth("google")}
            className="flex items-center justify-center h-11 border border-border hover:bg-secondary rounded-xl text-xs font-bold transition-all cursor-pointer"
          >
            <svg className="h-4 w-4 mr-2" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                fill="#4285F4"
              />
              <path
                d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                fill="#34A853"
              />
              <path
                d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"
                fill="#FBBC05"
              />
              <path
                d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                fill="#EA4335"
              />
            </svg>
            Google
          </button>
          <button
            onClick={() => handleOAuth("github")}
            className="flex items-center justify-center h-11 border border-border hover:bg-secondary rounded-xl text-xs font-bold transition-all cursor-pointer"
          >
            <svg className="h-4 w-4 mr-2" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
            </svg>
            GitHub
          </button>
        </div>

        {/* Toggler */}
        <div className="text-center text-xs">
          <span className="text-muted-foreground">
            {isSignUp ? "Already have an account? " : "Don't have an account yet? "}
          </span>
          <button
            onClick={() => {
              setIsSignUp(!isSignUp);
              setErrorMsg("");
              setSuccessMsg("");
            }}
            className="text-primary dark:text-blue-400 font-extrabold hover:underline"
          >
            {isSignUp ? "Sign In" : "Create one now"}
          </button>
        </div>
      </div>
    </div>
  );
}
