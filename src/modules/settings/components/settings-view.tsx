"use client";

import React, { useEffect, useState } from "react";
import { useUserStore } from "@/shared/hooks/use-user-store";
import { getSettingsAction, updateSettingsAction } from "@/app/actions";
import {
  Settings,
  User,
  Bell,
  Eye,
  Save,
  Check,
  Moon,
  Sun,
  Lock,
} from "lucide-react";
import { useTheme } from "next-themes";

export function SettingsView() {
  const { user, fetchUserData } = useUserStore();
  const { theme, setTheme } = useTheme();

  // Settings State
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [emailNotifications, setEmailNotifications] = useState(true);
  const [marketingEmails, setMarketingEmails] = useState(false);
  const [publicProfile, setPublicProfile] = useState(true);

  // Statuses
  const [isSaving, setIsSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);

  // Load settings
  useEffect(() => {
    async function loadSettings() {
      if (user) {
        setName(user.name || "");
        setEmail(user.email || "");
        try {
          const settings = await getSettingsAction(user.id);
          if (settings) {
            setEmailNotifications(settings.emailNotifications);
            setMarketingEmails(settings.marketingEmails);
            setPublicProfile(settings.publicProfile);
          }
        } catch (e) {
          console.error("Failed to load settings", e);
        }
      }
    }
    loadSettings();
  }, [user]);

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!user) return;

    setIsSaving(true);
    setSaveSuccess(false);

    try {
      await updateSettingsAction(
        {
          emailNotifications,
          marketingEmails,
          publicProfile,
          theme: theme || "system",
        },
        user.id
      );

      // Also trigger a user fetch to refresh any details if changed
      await fetchUserData();

      setSaveSuccess(true);
      setTimeout(() => setSaveSuccess(false), 3000);
    } catch (err) {
      console.error("Failed to save settings", err);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      {/* Page Header */}
      <div className="flex items-center gap-3 border-b border-border/40 pb-4">
        <div className="p-2 rounded-xl bg-primary/10 text-primary dark:text-blue-400 border border-primary/20">
          <Settings className="h-6 w-6" />
        </div>
        <div>
          <h1 className="text-2xl font-black tracking-tight">Settings</h1>
          <p className="text-xs text-muted-foreground mt-0.5">
            Manage your account preferences, themes, and notification profiles.
          </p>
        </div>
      </div>

      <form onSubmit={handleSave} className="space-y-6">
        {/* SECTION 1: PROFILE INFO */}
        <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
          <h2 className="text-base font-bold flex items-center gap-2 border-b border-border/20 pb-2">
            <User className="h-4.5 w-4.5 text-primary" />
            Profile Information
          </h2>

          <div className="grid grid-cols-1 gap-4">
            <div className="space-y-1">
              <label htmlFor="settings-name" className="text-xs font-semibold text-muted-foreground">
                Display Name
              </label>
              <input
                id="settings-name"
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                disabled // Mock user details are readonly in this MVP form
                className="w-full h-10 px-3 rounded-lg border border-border bg-muted/40 text-muted-foreground text-sm cursor-not-allowed focus:outline-none"
              />
              <span className="text-[10px] text-muted-foreground italic">
                Display names are synchronized with your active identity provider.
              </span>
            </div>

            <div className="space-y-1">
              <label htmlFor="settings-email" className="text-xs font-semibold text-muted-foreground">
                Email Address
              </label>
              <input
                id="settings-email"
                type="email"
                value={email}
                disabled
                className="w-full h-10 px-3 rounded-lg border border-border bg-muted/40 text-muted-foreground text-sm cursor-not-allowed focus:outline-none"
              />
            </div>
          </div>
        </div>

        {/* SECTION 2: APPEARANCE */}
        <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
          <h2 className="text-base font-bold flex items-center gap-2 border-b border-border/20 pb-2">
            {theme === "dark" ? (
              <Moon className="h-4.5 w-4.5 text-primary" />
            ) : (
              <Sun className="h-4.5 w-4.5 text-primary" />
            )}
            Appearance
          </h2>

          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-semibold">System Theme</h3>
              <p className="text-xs text-muted-foreground">
                Switch between Light and Dark mode preferences.
              </p>
            </div>
            <div className="flex rounded-lg bg-secondary p-1 border border-border">
              <button
                type="button"
                onClick={() => setTheme("light")}
                className={`px-3 py-1.5 rounded-md text-xs font-bold transition-all ${
                  theme === "light"
                    ? "bg-background text-foreground shadow"
                    : "text-muted-foreground hover:text-foreground"
                }`}
              >
                Light
              </button>
              <button
                type="button"
                onClick={() => setTheme("dark")}
                className={`px-3 py-1.5 rounded-md text-xs font-bold transition-all ${
                  theme === "dark"
                    ? "bg-background text-foreground shadow"
                    : "text-muted-foreground hover:text-foreground"
                }`}
              >
                Dark
              </button>
            </div>
          </div>
        </div>

        {/* SECTION 3: NOTIFICATIONS */}
        <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
          <h2 className="text-base font-bold flex items-center gap-2 border-b border-border/20 pb-2">
            <Bell className="h-4.5 w-4.5 text-primary" />
            Notification Settings
          </h2>

          <div className="space-y-4">
            <div className="flex items-start justify-between">
              <div className="space-y-0.5">
                <label htmlFor="settings-notify-email" className="text-sm font-semibold cursor-pointer">
                  Email Notifications
                </label>
                <p className="text-xs text-muted-foreground max-w-md">
                  Receive weekly summaries, completed tracks notifications, and milestones alerts.
                </p>
              </div>
              <input
                id="settings-notify-email"
                type="checkbox"
                checked={emailNotifications}
                onChange={(e) => setEmailNotifications(e.target.checked)}
                className="h-4 w-4 rounded border-border text-primary focus:ring-primary mt-1"
              />
            </div>

            <div className="flex items-start justify-between border-t border-border/20 pt-4">
              <div className="space-y-0.5">
                <label htmlFor="settings-notify-marketing" className="text-sm font-semibold cursor-pointer">
                  Marketing & Newsletter
                </label>
                <p className="text-xs text-muted-foreground max-w-md">
                  Receive promotional content, updates, and community highlights.
                </p>
              </div>
              <input
                id="settings-notify-marketing"
                type="checkbox"
                checked={marketingEmails}
                onChange={(e) => setMarketingEmails(e.target.checked)}
                className="h-4 w-4 rounded border-border text-primary focus:ring-primary mt-1"
              />
            </div>
          </div>
        </div>

        {/* SECTION 4: PRIVACY */}
        <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
          <h2 className="text-base font-bold flex items-center gap-2 border-b border-border/20 pb-2">
            <Eye className="h-4.5 w-4.5 text-primary" />
            Privacy Settings
          </h2>

          <div className="flex items-start justify-between">
            <div className="space-y-0.5">
              <label htmlFor="settings-privacy-public" className="text-sm font-semibold cursor-pointer">
                Public Leaderboard Profile
              </label>
              <p className="text-xs text-muted-foreground max-w-md">
                Make your level, achievements, and completed track progress visible on public leaderboards.
              </p>
            </div>
            <input
              id="settings-privacy-public"
              type="checkbox"
              checked={publicProfile}
              onChange={(e) => setPublicProfile(e.target.checked)}
              className="h-4 w-4 rounded border-border text-primary focus:ring-primary mt-1"
            />
          </div>
        </div>

        {/* SAVE BUTTONS */}
        <div className="flex items-center justify-end gap-3 pt-4 border-t border-border/20">
          {saveSuccess && (
            <span className="text-xs font-bold text-emerald-500 flex items-center gap-1.5">
              <Check className="h-4 w-4 animate-scale-up" />
              Settings saved successfully!
            </span>
          )}

          <button
            type="submit"
            disabled={isSaving}
            className="inline-flex items-center gap-1.5 rounded-xl bg-primary px-5 py-2.5 text-sm font-bold text-primary-foreground hover:bg-primary/95 transition-all shadow-md shadow-primary/20 disabled:opacity-40"
          >
            <Save className="h-4 w-4" />
            {isSaving ? "Saving..." : "Save Preferences"}
          </button>
        </div>
      </form>
    </div>
  );
}
