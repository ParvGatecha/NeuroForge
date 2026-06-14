"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useTheme } from "next-themes";
import { useUserStore } from "@/shared/hooks/use-user-store";
import { getLevelProgress } from "@/modules/progress/xp";
import {
  Flame,
  Sun,
  Moon,
  Menu,
  X,
  Compass,
  LayoutDashboard,
  Map,
  Settings,
  Shield,
  User,
  GraduationCap,
  Star,
} from "lucide-react";

export function Header() {
  const pathname = usePathname();
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const { user, streak, fetchUserData } = useUserStore();

  useEffect(() => {
    setMounted(true);
    fetchUserData();
  }, [fetchUserData]);

  if (!mounted) return null;

  // Compute levels
  const xpProgress = user ? getLevelProgress(user.xp) : null;

  const navLinks = [
    { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
    { href: "/learning-items", label: "Learning Items", icon: Compass },
    { href: "/roadmaps", label: "Roadmaps", icon: Map },
    { href: "/saved-items", label: "Saved Items", icon: Star },
    { href: "/settings", label: "Settings", icon: Settings },
  ];

  if (user?.role === "ADMIN") {
    navLinks.push({ href: "/admin", label: "Admin", icon: Shield });
  }

  const isLinkActive = (href: string) => {
    if (href === "/dashboard") return pathname === "/dashboard" || pathname === "/";
    return pathname.startsWith(href);
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur-md dark:bg-background/80 supports-[backdrop-filter]:bg-background/60">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        {/* Brand Logo */}
        <div className="flex items-center gap-8">
          <Link href="/dashboard" className="flex items-center gap-2">
            <GraduationCap className="h-6 w-6 text-primary dark:text-blue-400" />
            <span className="bg-gradient-to-r from-primary to-cyan-400 bg-clip-text text-xl font-bold tracking-tight text-transparent">
              TensorTrack
            </span>
          </Link>

          {/* Desktop Nav Links */}
          <nav className="hidden md:flex items-center gap-6">
            {navLinks.map((link) => {
              const Icon = link.icon;
              const active = isLinkActive(link.href);
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  className={`flex items-center gap-1.5 text-sm font-medium transition-colors hover:text-primary ${
                    active
                      ? "text-primary dark:text-blue-400"
                      : "text-muted-foreground"
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  {link.label}
                </Link>
              );
            })}
          </nav>
        </div>

        {/* Right Side Stats & Actions */}
        <div className="flex items-center gap-4">
          {/* XP & Level Panel (Desktop) */}
          {user && xpProgress && (
            <div className="hidden sm:flex flex-col items-end gap-1 text-xs">
              <div className="flex items-center gap-2 font-medium">
                <span className="text-muted-foreground">LVL {xpProgress.level}</span>
                <span className="text-primary dark:text-blue-400">
                  {xpProgress.progressInLevel} / {xpProgress.neededForNextLevel} XP
                </span>
              </div>
              <div className="h-1.5 w-32 overflow-hidden rounded-full bg-secondary">
                <div
                  className="h-full bg-gradient-to-r from-primary to-cyan-400 transition-all duration-500"
                  style={{ width: `${xpProgress.percentage}%` }}
                />
              </div>
            </div>
          )}

          {/* Streak Indicator */}
          {streak && (
            <div
              className={`flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-semibold ${
                streak.currentCount > 0
                  ? "bg-amber-500/10 text-amber-500 neon-glow-cyan"
                  : "bg-muted text-muted-foreground"
              }`}
              title={`Streak: ${streak.currentCount} days active (Longest: ${streak.longestCount} days)`}
            >
              <Flame className={`h-4 w-4 ${streak.currentCount > 0 ? "animate-pulse" : ""}`} />
              <span>{streak.currentCount}d</span>
            </div>
          )}

          {/* Theme Switcher */}
          <button
            onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
            className="rounded-lg p-2 text-muted-foreground hover:bg-secondary hover:text-foreground"
            aria-label="Toggle theme"
          >
            {theme === "dark" ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </button>

          {/* User Profile (Desktop) */}
          {user ? (
            <div className="flex items-center gap-2 border-l border-border/40 pl-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary/10 text-primary dark:text-blue-400">
                <User className="h-4 w-4" />
              </div>
              <span className="hidden lg:inline text-sm font-medium">{user.name}</span>
              <button
                onClick={async () => {
                  const { createClient } = await import("@/shared/lib/supabase/client");
                  const supabase = createClient();
                  await supabase.auth.signOut();
                  window.location.reload();
                }}
                className="text-xs text-muted-foreground hover:text-foreground pl-2 font-bold cursor-pointer transition-colors"
              >
                Sign Out
              </button>
            </div>
          ) : (
            <div className="flex items-center gap-2 border-l border-border/40 pl-4">
              <Link
                href="/login"
                className="rounded-xl bg-primary px-3 py-1.5 text-xs font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/20"
              >
                Sign In
              </Link>
            </div>
          )}

          {/* Mobile Menu Button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="rounded-lg p-2 text-muted-foreground hover:bg-secondary hover:text-foreground md:hidden"
            aria-label="Toggle menu"
          >
            {mobileMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden border-t border-border/40 bg-background/95 backdrop-blur-md px-4 py-4 space-y-3">
          <nav className="flex flex-col gap-2">
            {navLinks.map((link) => {
              const Icon = link.icon;
              const active = isLinkActive(link.href);
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  onClick={() => setMobileMenuOpen(false)}
                  className={`flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium transition-colors hover:bg-secondary ${
                    active
                      ? "bg-secondary text-primary dark:text-blue-400"
                      : "text-muted-foreground hover:text-foreground"
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  {link.label}
                </Link>
              );
            })}
          </nav>

          {/* Mobile XP Progress */}
          {user && xpProgress && (
            <div className="border-t border-border/45 pt-3 flex flex-col gap-1.5 px-3">
              <div className="flex items-center justify-between text-xs font-medium">
                <span className="text-muted-foreground">LVL {xpProgress.level}</span>
                <span className="text-primary dark:text-blue-400">
                  {xpProgress.progressInLevel} / {xpProgress.neededForNextLevel} XP
                </span>
              </div>
              <div className="h-1.5 w-full overflow-hidden rounded-full bg-secondary">
                <div
                  className="h-full bg-gradient-to-r from-primary to-cyan-400"
                  style={{ width: `${xpProgress.percentage}%` }}
                />
              </div>
            </div>
          )}

          {/* Mobile Profile / Auth Button */}
          <div className="border-t border-border/45 pt-3 px-3">
            {user ? (
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <div className="flex h-7 w-7 items-center justify-center rounded-full bg-primary/10 text-primary dark:text-blue-400">
                    <User className="h-3.5 w-3.5" />
                  </div>
                  <span className="text-sm font-medium">{user.name}</span>
                </div>
                <button
                  onClick={async () => {
                    const { createClient } = await import("@/shared/lib/supabase/client");
                    const supabase = createClient();
                    await supabase.auth.signOut();
                    window.location.reload();
                  }}
                  className="text-xs text-muted-foreground hover:text-foreground font-bold cursor-pointer transition-colors"
                >
                  Sign Out
                </button>
              </div>
            ) : (
              <Link
                href="/login"
                onClick={() => setMobileMenuOpen(false)}
                className="w-full h-9 bg-primary text-primary-foreground font-bold rounded-xl flex items-center justify-center text-xs hover:bg-primary/95 transition-all shadow-md shadow-primary/20"
              >
                Sign In
              </Link>
            )}
          </div>
        </div>
      )}
    </header>
  );
}
