"use client";

import React, { useState, useEffect } from "react";
import { useUserStore } from "@/shared/hooks/use-user-store";
import {
  rebuildSearchIndexAction,
  resetUserProgressAction,
  isDatabaseConnectedAction,
  saveLearningItemAction,
  deleteLearningItemAction,
  bulkImportAction,
} from "@/app/actions";
import {
  ShieldAlert,
  Database,
  RefreshCw,
  Trash2,
  CheckCircle,
  FileSearch,
  Terminal,
  PlusCircle,
  Edit,
  Upload,
  BookOpen,
  Settings,
  HelpCircle,
  ListOrdered
} from "lucide-react";
import searchIndex from "../../../../content/search_index.json";

export function AdminView() {
  const { user, fetchUserData } = useUserStore();
  const [activeTab, setActiveTab] = useState<"overview" | "edit" | "bulk" | "roadmap">("overview");
  const [dbConnected, setDbConnected] = useState<boolean | null>(null);

  // States for operations
  const [indexStatus, setIndexStatus] = useState<{ loading: boolean; success: boolean; count?: number }>({ loading: false, success: false });
  const [resetStatus, setResetStatus] = useState<{ loading: boolean; success: boolean; dbMode?: string }>({ loading: false, success: false });

  // Form State
  const [formId, setFormId] = useState("");
  const [formSlug, setFormSlug] = useState("");
  const [formTitle, setFormTitle] = useState("");
  const [formSection, setFormSection] = useState("Python");
  const [formDifficulty, setFormDifficulty] = useState("Easy");
  
  // v2 fields
  const [formTheoryTitle, setFormTheoryTitle] = useState("");
  const [formTheoryUrl, setFormTheoryUrl] = useState("");
  const [formTheoryType, setFormTheoryType] = useState("article");
  const [formPracticePlatform, setFormPracticePlatform] = useState("DEEP_ML");
  const [formPracticeTitle, setFormPracticeTitle] = useState("");
  const [formPracticeUrl, setFormPracticeUrl] = useState("");

  const [formEstimatedTime, setFormEstimatedTime] = useState("15");
  const [formTags, setFormTags] = useState("");
  const [formObjectives, setFormObjectives] = useState("");
  const [formDescription, setFormDescription] = useState("");
  const [formPrereqs, setFormPrereqs] = useState("");
  const [formMessage, setFormMessage] = useState<{ text: string; error: boolean } | null>(null);

  // Edit look-up ID
  const [lookupId, setLookupId] = useState("");

  // Bulk State
  const [bulkJson, setBulkJson] = useState("");
  const [bulkMessage, setBulkMessage] = useState<{ text: string; error: boolean } | null>(null);

  // Load connection status
  useEffect(() => {
    async function checkConn() {
      const conn = await isDatabaseConnectedAction();
      setDbConnected(conn);
    }
    checkConn();
  }, []);

  if (!user) return <div className="text-sm text-muted-foreground">Loading admin profile...</div>;

  if (user.role !== "ADMIN") {
    return (
      <div className="max-w-md mx-auto glass-panel rounded-2xl p-6 border border-rose-500/20 bg-card text-center space-y-4">
        <ShieldAlert className="h-12 w-12 text-rose-500 mx-auto animate-pulse" />
        <h2 className="text-lg font-bold">Access Denied</h2>
        <p className="text-xs text-muted-foreground">
          You do not have administrative privileges to access this panel.
        </p>
      </div>
    );
  }

  // Trigger search index rebuild
  const handleRebuildIndex = async () => {
    setIndexStatus({ loading: true, success: false });
    const result = await rebuildSearchIndexAction();
    if (result.success) {
      setIndexStatus({ loading: false, success: true, count: result.count });
      setTimeout(() => setIndexStatus({ loading: false, success: false }), 4000);
    } else {
      setIndexStatus({ loading: false, success: false });
    }
  };

  // Trigger user data reset
  const handleResetProgress = async () => {
    if (!confirm("Are you sure you want to reset all progress, levels, streaks, and achievements?")) {
      return;
    }
    setResetStatus({ loading: true, success: false });
    const result = await resetUserProgressAction(user.id);
    if (result.success) {
      setResetStatus({ loading: false, success: true, dbMode: result.dbMode });
      await fetchUserData();
      setTimeout(() => setResetStatus({ loading: false, success: false }), 4000);
    } else {
      setResetStatus({ loading: false, success: false });
    }
  };

  // Load item into form for editing
  const handleLookupItem = () => {
    const numericId = Number(lookupId);
    if (isNaN(numericId)) {
      setFormMessage({ text: "Please enter a valid numeric item ID", error: true });
      return;
    }

    const item = searchIndex.find((itm) => itm.id === numericId);
    if (!item) {
      setFormMessage({ text: `Learning item ID #${numericId} not found in index`, error: true });
      return;
    }

    setFormId(String(item.id));
    setFormSlug(item.slug);
    setFormTitle(item.title);
    setFormSection(item.section);
    setFormDifficulty(item.difficulty);
    setFormTheoryTitle(item.theory_resource?.title || "");
    setFormTheoryUrl(item.theory_resource?.url || "");
    setFormTheoryType(item.theory_resource?.type || "article");
    setFormPracticePlatform(item.practice_resource?.platform || "EXTERNAL");
    setFormPracticeTitle(item.practice_resource?.title || "");
    setFormPracticeUrl(item.practice_resource?.url || "");
    setFormEstimatedTime(String(item.estimated_time_minutes));
    setFormTags(item.tags.join(", "));
    setFormObjectives(item.learning_objectives.join(", "));
    setFormDescription(item.description);
    setFormPrereqs((item.prerequisites || []).join(", "));
    setFormMessage({ text: `Loaded item #${item.id} successfully`, error: false });
  };

  // Save/Create item handler
  const handleSaveItem = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormMessage(null);

    if (!formId || !formSlug || !formTitle || !formTheoryUrl || !formDescription) {
      setFormMessage({ text: "Please fill out all required fields", error: true });
      return;
    }

    const itemData = {
      id: Number(formId),
      slug: formSlug,
      title: formTitle,
      section: formSection,
      difficulty: formDifficulty,
      theory_resource: {
        title: formTheoryTitle || `Theory: ${formTitle}`,
        url: formTheoryUrl,
        type: formTheoryType
      },
      practice_resource: {
        platform: formPracticePlatform,
        title: formPracticeTitle || `Practice: ${formTitle}`,
        url: formPracticeUrl || formTheoryUrl
      },
      estimated_time_minutes: Number(formEstimatedTime),
      tags: formTags,
      learning_objectives: formObjectives,
      description: formDescription,
      prerequisites: formPrereqs
    };

    const res = await saveLearningItemAction(itemData);
    if (res.success) {
      setFormMessage({ text: `Learning item #${itemData.id} saved successfully! Re-indexing complete.`, error: false });
    } else {
      setFormMessage({ text: "Failed to save learning item json file.", error: true });
    }
  };

  // Delete item handler
  const handleDeleteItem = async () => {
    if (!formId) return;
    if (!confirm(`Are you sure you want to delete item #${formId}? This deletes the JSON file on disk.`)) {
      return;
    }

    setFormMessage(null);
    const res = await deleteLearningItemAction(Number(formId));
    if (res) {
      setFormMessage({ text: `Deleted learning item #${formId} successfully!`, error: false });
      // Reset form
      setFormId("");
      setFormSlug("");
      setFormTitle("");
      setFormTheoryTitle("");
      setFormTheoryUrl("");
      setFormTheoryType("article");
      setFormPracticePlatform("DEEP_ML");
      setFormPracticeTitle("");
      setFormPracticeUrl("");
      setFormTags("");
      setFormObjectives("");
      setFormDescription("");
      setFormPrereqs("");
    } else {
      setFormMessage({ text: `Failed to delete item #${formId}. Check if it exists.`, error: true });
    }
  };

  // Bulk import JSON
  const handleBulkImport = async () => {
    setBulkMessage(null);
    if (!bulkJson.trim()) return;

    const res = await bulkImportAction(bulkJson);
    if (res.success) {
      setBulkMessage({ text: `Bulk import completed! Successfully updated ${res.count} items.`, error: false });
      setBulkJson("");
    } else {
      setBulkMessage({ text: `Import failed: ${res.error}`, error: true });
    }
  };

  const sectionsList = ["Python", "Statistics", "Machine Learning", "Deep Learning", "LLM", "RAG", "Agents", "System Design"];


  return (
    <div className="max-w-4xl mx-auto space-y-6 animate-fade-in-up">
      {/* Page Header */}
      <div className="flex items-center gap-3 border-b border-border/40 pb-4">
        <div className="p-2 rounded-xl bg-primary/10 text-primary dark:text-blue-400 border border-primary/20">
          <Terminal className="h-6 w-6" />
        </div>
        <div>
          <h1 className="text-2xl font-black tracking-tight">Admin Console</h1>
          <p className="text-xs text-muted-foreground mt-0.5">
            Manage sections, curate learning resources, import JSON datasets, and monitor database infrastructure.
          </p>
        </div>
      </div>

      {/* Tabs list */}
      <div className="flex border-b border-border/30 bg-muted/10 text-xs sm:text-sm font-semibold rounded-lg overflow-hidden border">
        <button
          onClick={() => setActiveTab("overview")}
          className={`flex-1 py-3 text-center border-b-2 transition-all ${
            activeTab === "overview"
              ? "border-primary bg-secondary text-primary dark:text-blue-400"
              : "border-transparent text-muted-foreground hover:bg-secondary/40"
          }`}
        >
          Overview & Info
        </button>
        <button
          onClick={() => setActiveTab("edit")}
          className={`flex-1 py-3 text-center border-b-2 transition-all ${
            activeTab === "edit"
              ? "border-primary bg-secondary text-primary dark:text-blue-400"
              : "border-transparent text-muted-foreground hover:bg-secondary/40"
          }`}
        >
          Add / Edit Item
        </button>
        <button
          onClick={() => setActiveTab("bulk")}
          className={`flex-1 py-3 text-center border-b-2 transition-all ${
            activeTab === "bulk"
              ? "border-primary bg-secondary text-primary dark:text-blue-400"
              : "border-transparent text-muted-foreground hover:bg-secondary/40"
          }`}
        >
          Bulk JSON Import
        </button>
      </div>

      {/* Tab Contents */}
      {activeTab === "overview" && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card space-y-2">
              <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground">
                Roadmap Curriculum
              </span>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl font-black text-foreground">{searchIndex.length}</span>
                <span className="text-xs text-muted-foreground font-semibold">Learning Items</span>
              </div>
            </div>

            <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card space-y-2">
              <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground">
                Roadmap Tracks
              </span>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl font-black text-foreground">8</span>
                <span className="text-xs text-muted-foreground font-semibold">Structured Sections</span>
              </div>
            </div>

            <div className="glass-panel rounded-2xl p-5 border border-border/40 bg-card space-y-2">
              <span className="text-[10px] font-bold uppercase tracking-wider text-muted-foreground">
                Infrastructure Mode
              </span>
              <div className="flex items-center gap-2">
                {dbConnected === null ? (
                  <span className="text-xs text-muted-foreground font-medium">Probing...</span>
                ) : dbConnected ? (
                  <span className="text-xs font-bold text-emerald-500 bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded">
                    PostgreSQL Mode
                  </span>
                ) : (
                  <span className="text-xs font-bold text-amber-500 bg-amber-500/10 border border-amber-500/20 px-2 py-0.5 rounded">
                    Local File Mock
                  </span>
                )}
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Index Rebuilder */}
            <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
              <div className="flex items-center gap-3">
                <div className="p-2 rounded-lg bg-cyan-500/10 text-cyan-500">
                  <FileSearch className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-bold text-sm">Search Catalog Compiler</h3>
                  <p className="text-xs text-muted-foreground leading-relaxed">
                    Re-scan direct directory JSON items and compile a new search index files.
                  </p>
                </div>
              </div>

              <div className="pt-2">
                <button
                  onClick={handleRebuildIndex}
                  disabled={indexStatus.loading}
                  className="inline-flex items-center gap-1.5 rounded-lg bg-cyan-500 hover:bg-cyan-600 text-white px-4 py-2 text-xs font-bold transition-all shadow-md shadow-cyan-500/15 disabled:opacity-40"
                >
                  <RefreshCw className={`h-3.5 w-3.5 ${indexStatus.loading ? "animate-spin" : ""}`} />
                  {indexStatus.loading ? "Compiling..." : "Compile Index"}
                </button>
              </div>

              {indexStatus.success && (
                <div className="text-xs text-emerald-500 font-semibold flex items-center gap-1">
                  <CheckCircle className="h-4 w-4" />
                  Index generated! Compiled {indexStatus.count} learning items.
                </div>
              )}
            </div>

            {/* Developer Reset */}
            <div className="glass-panel rounded-2xl p-6 border border-border/40 bg-card space-y-4">
              <div className="flex items-center gap-3">
                <div className="p-2 rounded-lg bg-rose-500/10 text-rose-500">
                  <Trash2 className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-bold text-sm">Progress Reset (Developer Tool)</h3>
                  <p className="text-xs text-muted-foreground leading-relaxed">
                    Erase all completed learning items, levels, streaks, and unlocked badges.
                  </p>
                </div>
              </div>

              <div className="pt-2">
                <button
                  onClick={handleResetProgress}
                  disabled={resetStatus.loading}
                  className="inline-flex items-center gap-1.5 rounded-lg bg-rose-500 hover:bg-rose-600 text-white px-4 py-2 text-xs font-bold transition-all shadow-md shadow-rose-500/15 disabled:opacity-40"
                >
                  <Trash2 className="h-3.5 w-3.5" />
                  {resetStatus.loading ? "Resetting..." : "Reset All Progress"}
                </button>
              </div>

              {resetStatus.success && (
                <div className="text-xs text-emerald-500 font-semibold flex items-center gap-1">
                  <CheckCircle className="h-4 w-4" />
                  Progress successfully cleared! ({resetStatus.dbMode})
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {activeTab === "edit" && (
        <div className="glass-panel rounded-2xl border border-border/40 bg-card p-6 space-y-6">
          <div className="flex flex-col sm:flex-row items-end gap-3 pb-4 border-b border-border/30">
            <div className="flex-1 space-y-1">
              <label className="text-xs font-bold text-muted-foreground">Load Existing Learning Item (Look-up ID)</label>
              <input
                type="text"
                placeholder="Enter item ID (e.g. 61)"
                value={lookupId}
                onChange={(e) => setLookupId(e.target.value)}
                className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 text-sm focus:outline-none focus:ring-1 focus:ring-primary"
              />
            </div>
            <button
              onClick={handleLookupItem}
              className="bg-secondary hover:bg-secondary-hover border border-border px-5 h-10 rounded-lg text-xs font-bold transition-all"
            >
              Load Item
            </button>
          </div>

          <form onSubmit={handleSaveItem} className="space-y-4 text-xs sm:text-sm">
            {formMessage && (
              <div
                className={`p-3 rounded-lg border text-xs font-medium flex items-center gap-2 ${
                  formMessage.error
                    ? "bg-rose-500/10 border-rose-500/20 text-rose-500"
                    : "bg-emerald-500/10 border-emerald-500/20 text-emerald-500"
                }`}
              >
                <CheckCircle className="h-4 w-4 shrink-0" />
                <span>{formMessage.text}</span>
              </div>
            )}

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Item ID (Required)</label>
                <input
                  type="number"
                  placeholder="ID (e.g. 101)"
                  value={formId}
                  onChange={(e) => setFormId(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                  required
                />
              </div>
              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Slug (Required)</label>
                <input
                  type="text"
                  placeholder="tokenization-fundamentals"
                  value={formSlug}
                  onChange={(e) => setFormSlug(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                  required
                />
              </div>
            </div>

            <div className="space-y-1">
              <label className="text-xs font-bold text-muted-foreground block">Title (Required)</label>
              <input
                type="text"
                placeholder="Tokenization Fundamentals"
                value={formTitle}
                onChange={(e) => setFormTitle(e.target.value)}
                className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                required
              />
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Section</label>
                <select
                  value={formSection}
                  onChange={(e) => setFormSection(e.target.value)}
                  className="w-full h-10 px-2 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary text-xs"
                >
                  {sectionsList.map((sec) => (
                    <option key={sec} value={sec}>
                      {sec}
                    </option>
                  ))}
                </select>
              </div>

              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Difficulty</label>
                <select
                  value={formDifficulty}
                  onChange={(e) => setFormDifficulty(e.target.value)}
                  className="w-full h-10 px-2 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary text-xs"
                >
                  <option value="Easy">Easy</option>
                  <option value="Medium">Medium</option>
                  <option value="Hard">Hard</option>
                </select>
              </div>

              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Est. Time (Mins)</label>
                <input
                  type="number"
                  value={formEstimatedTime}
                  onChange={(e) => setFormEstimatedTime(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                  required
                />
              </div>
            </div>

            {/* Theory Resource Sub-section */}
            <div className="border border-border/30 rounded-xl p-4 space-y-4 bg-muted/5">
              <h4 className="text-xs font-black uppercase tracking-wider text-muted-foreground">Theory Resource</h4>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div className="space-y-1 sm:col-span-2">
                  <label className="text-xs font-bold text-muted-foreground block">Theory Title</label>
                  <input
                    type="text"
                    placeholder="Theory Resource Title"
                    value={formTheoryTitle}
                    onChange={(e) => setFormTheoryTitle(e.target.value)}
                    className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                  />
                </div>
                <div className="space-y-1">
                  <label className="text-xs font-bold text-muted-foreground block">Theory Type</label>
                  <select
                    value={formTheoryType}
                    onChange={(e) => setFormTheoryType(e.target.value)}
                    className="w-full h-10 px-2 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary text-xs"
                  >
                    <option value="article">Article</option>
                    <option value="blog">Blog</option>
                    <option value="documentation">Documentation</option>
                    <option value="youtube">YouTube</option>
                    <option value="research-paper">Research Paper</option>
                    <option value="github">GitHub</option>
                    <option value="course">Course</option>
                  </select>
                </div>
              </div>
              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Theory URL (Required)</label>
                <input
                  type="url"
                  placeholder="https://..."
                  value={formTheoryUrl}
                  onChange={(e) => setFormTheoryUrl(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                  required
                />
              </div>
            </div>

            {/* Practice Resource Sub-section */}
            <div className="border border-border/30 rounded-xl p-4 space-y-4 bg-muted/5">
              <h4 className="text-xs font-black uppercase tracking-wider text-muted-foreground">Practice Resource</h4>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div className="space-y-1 sm:col-span-2">
                  <label className="text-xs font-bold text-muted-foreground block">Practice Title</label>
                  <input
                    type="text"
                    placeholder="Practice Exercise Title"
                    value={formPracticeTitle}
                    onChange={(e) => setFormPracticeTitle(e.target.value)}
                    className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                  />
                </div>
                <div className="space-y-1">
                  <label className="text-xs font-bold text-muted-foreground block">Practice Platform</label>
                  <select
                    value={formPracticePlatform}
                    onChange={(e) => setFormPracticePlatform(e.target.value)}
                    className="w-full h-10 px-2 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary text-xs"
                  >
                    <option value="DEEP_ML">Deep-ML</option>
                    <option value="KAGGLE">Kaggle</option>
                    <option value="HUGGING_FACE">Hugging Face</option>
                    <option value="GITHUB">GitHub</option>
                    <option value="LANGCHAIN">LangChain</option>
                    <option value="LANGGRAPH">LangGraph</option>
                    <option value="LLAMAINDEX">LlamaIndex</option>
                    <option value="CUSTOM">Custom</option>
                    <option value="EXTERNAL">External</option>
                  </select>
                </div>
              </div>
              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Practice URL</label>
                <input
                  type="url"
                  placeholder="https://... (defaults to Theory URL if blank)"
                  value={formPracticeUrl}
                  onChange={(e) => setFormPracticeUrl(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                />
              </div>
            </div>

            <div className="space-y-1">
              <label className="text-xs font-bold text-muted-foreground block">Description (Required)</label>
              <textarea
                placeholder="Provide a brief summary of what the learner will gain from studying this resource."
                value={formDescription}
                onChange={(e) => setFormDescription(e.target.value)}
                className="w-full min-h-[80px] p-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                required
              />
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Tags (Comma-separated)</label>
                <input
                  type="text"
                  placeholder="tokenization, bpe, llm"
                  value={formTags}
                  onChange={(e) => setFormTags(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                />
              </div>

              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Objectives (Comma-separated)</label>
                <input
                  type="text"
                  placeholder="Understand byte-pair encoding, Compare algorithms"
                  value={formObjectives}
                  onChange={(e) => setFormObjectives(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                />
              </div>

              <div className="space-y-1">
                <label className="text-xs font-bold text-muted-foreground block">Prerequisites (IDs, Comma-separated)</label>
                <input
                  type="text"
                  placeholder="55, 56"
                  value={formPrereqs}
                  onChange={(e) => setFormPrereqs(e.target.value)}
                  className="w-full h-10 px-3 rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary"
                />
              </div>
            </div>

            <div className="flex items-center justify-between pt-4 gap-4">
              {formId ? (
                <button
                  type="button"
                  onClick={handleDeleteItem}
                  className="flex items-center gap-1.5 rounded-lg border border-rose-500 hover:bg-rose-500/10 text-rose-500 px-5 py-2.5 text-xs font-bold transition-all"
                >
                  <Trash2 className="h-3.5 w-3.5" />
                  Delete Item
                </button>
              ) : (
                <div />
              )}

              <button
                type="submit"
                className="flex items-center gap-1.5 rounded-lg bg-primary hover:bg-primary/95 text-primary-foreground px-6 py-2.5 text-xs font-bold transition-all shadow-md shadow-primary/20"
              >
                <PlusCircle className="h-3.5 w-3.5" />
                Save / Create Learning Item
              </button>
            </div>
          </form>
        </div>
      )}

      {activeTab === "bulk" && (
        <div className="glass-panel rounded-2xl border border-border/40 bg-card p-6 space-y-4">
          <div className="flex items-center gap-3 pb-3 border-b border-border/30">
            <div className="p-2 rounded-lg bg-amber-500/10 text-amber-500">
              <Upload className="h-5 w-5" />
            </div>
            <div>
              <h3 className="font-bold text-sm">Bulk JSON Import Dataset</h3>
              <p className="text-xs text-muted-foreground">
                Paste a single learning item JSON or an array of items to build content files sequentially.
              </p>
            </div>
          </div>

          {bulkMessage && (
            <div
              className={`p-3 rounded-lg border text-xs font-medium flex items-center gap-2 ${
                bulkMessage.error
                  ? "bg-rose-500/10 border-rose-500/20 text-rose-500"
                  : "bg-emerald-500/10 border-emerald-500/20 text-emerald-500"
              }`}
            >
              <CheckCircle className="h-4 w-4 shrink-0" />
              <span>{bulkMessage.text}</span>
            </div>
          )}

          <textarea
            placeholder='[
  {
    "id": 61,
    "slug": "tokenization-fundamentals",
    "title": "Tokenization Fundamentals",
    "section": "LLM",
    "difficulty": "Easy",
    "theory_resource": {
      "title": "Theory: Tokenization Fundamentals",
      "url": "https://huggingface.co/course/chapter6",
      "type": "course"
    },
    "practice_resource": {
      "platform": "HUGGING_FACE",
      "title": "Practice: Tokenization Fundamentals",
      "url": "https://huggingface.co/course/chapter6"
    },
    "estimated_time_minutes": 15,
    "tags": ["tokenization", "llm"],
    "learning_objectives": ["Understand tokenization"],
    "description": "Overview of what the learner gains",
    "prerequisites": [55, 56]
  }
]'
            value={bulkJson}
            onChange={(e) => setBulkJson(e.target.value)}
            className="w-full min-h-[250px] p-3 font-mono text-xs rounded-lg border border-border bg-background/50 focus:outline-none focus:ring-1 focus:ring-primary leading-relaxed"
          />

          <div className="pt-2 text-right">
            <button
              onClick={handleBulkImport}
              className="inline-flex items-center gap-1.5 rounded-lg bg-primary hover:bg-primary/95 text-primary-foreground px-6 py-2.5 text-xs font-bold transition-all shadow-md shadow-primary/20"
            >
              <Upload className="h-3.5 w-3.5" />
              Import JSON Data
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
