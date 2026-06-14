# TensorTrack MVP - AI Engineer Upskilling Platform

Welcome to **TensorTrack**, a production-ready, roadmap-driven learning and interview preparation platform designed specifically for AI and Machine Learning Engineers.

This platform launches with **100 pre-loaded, first-principles questions** categorized across 8 core tracks.

---

## 🚀 Key Features

- **Linear Learning Roadmap**: Tracks progress sequentially using course prerequisites (`Python Concurrency` ➔ `Math Stats` ➔ `Classical ML` ➔ `Deep Learning` ➔ `LLM` ➔ `RAG` ➔ `AI Agents` ➔ `AI System Design`).
- **Interactive Code Playground**: Full split-screen workspace with multi-tab description panels,progressive hints, literature references, and an interactive mock Python execution sandbox with console output logging.
- **Zod Content Validator**: Runs automatically during code builds to validate all 100 question files under `content/questions/` against strict schema rules.
- **Gamified Progress Engines**:
  - **XP Engine**: Computes RPG-like exponential leveling progression.
  - **Streak Engine**: Tracks daily question completion and tracks consecutive activity.
  - **Achievement Auto-Unlocker**: Awards XP bonuses and badge unlocks for hitting milestone targets.
- **Hybrid Storage Provider**: Seamlessly uses **Prisma/PostgreSQL** in production, but automatically falls back to a **local file-based JSON database (`content/local_mock_db.json`)** if the database server is not reachable. This guarantees the app is functional out-of-the-box in local development.
- **High-Performance Client Search**: Leverages `Fuse.js` client-side fuzzy queries on a compiled build-time search index for instant filtering.

---

## 🛠️ Technology Stack

- **Framework**: Next.js 16 (App Router, TypeScript, Tailwind CSS v4)
- **Database ORM**: Prisma ORM (targeting PostgreSQL for production, with SQLite and JSON-file fallback capability)
- **Authentication**: Better Auth (configured with Prisma adapter)
- **State Management**: Zustand (for unified client state synchronization)
- **Styling**: Vanilla CSS with custom scrollbars, animations, and premium glassmorphic/neon utility classes

---

## 📂 Project Architecture

The codebase follows **Clean Architecture** patterns, separating modules and shared concerns:

```
src/
├── app/                  # Next.js App Router (pages and API route controllers)
├── modules/              # Clean Architecture Feature Modules
│   ├── auth/             # Login, signup, password reset flow components
│   ├── dashboard/        # Dashboard layout, streaks, XP progress panels
│   ├── questions/        # Questions Explorer, split-screen workspace UI
│   ├── roadmaps/         # Learning path vertical sequence graphs
│   ├── achievements/     # Milestone checker, rewards, and badge descriptors
│   ├── admin/            # Control panel, infra metrics, index re-builder
│   └── progress/         # XP levels and active streak computation engines
└── shared/               # Shared cross-cutting components & utilities
    ├── components/       # Global Header, theme provider, UI wrappers
    ├── lib/              # Prisma client, Better Auth config, DB services
    └── hooks/            # Shared state stores (Zustand)
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Node.js `v20.x` or `v22.x`
- npm (installed automatically with Node)

### 2. Installation
Clone this repository and install dependencies:
```bash
npm install
```

### 3. Environment Setup
A default local `.env` is already provided:
```env
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/tensortrack?schema=public"
BETTER_AUTH_SECRET="some-secret-key-at-least-32-chars-long-tensortrack"
BETTER_AUTH_URL="http://localhost:3000"
```

### 4. Running the Development Server
Start the local server:
```bash
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) to view the application. The system will automatically detect if PostgreSQL is not running and fall back to the local file DB mock in `content/local_mock_db.json`.

---

## 🧪 Testing and Building

### Run Unit Tests
Executes test assertions for the XP progression calculations and recommended question sequencing:
```bash
npm run test
```

### Build for Production
Runs the Zod question verification, builds the Fuse.js search index, and compiles the Next.js production build:
```bash
npm run build
```
The build process will fail if any question file does not comply with the Zod schema.

---

## 📊 Database Models

Defined in `prisma/schema.prisma`:
- `User`: Handles active stats (XP, Level, Role).
- `Session`, `Account`, `Verification`: Standard Better Auth schema models.
- `QuestionProgress`: Logs completed challenges and XP rewards.
- `Bookmark`: Tracks bookmarked questions.
- `Streak`: Tracks daily active streak counts and records.
- `Achievement`, `UserAchievement`: Custom gamification badges and unlock timestamps.
- `UserSettings`: Layout theme preferences and notification flags.
