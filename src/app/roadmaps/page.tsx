import { Header } from "@/shared/components/header";
import { RoadmapsView } from "@/modules/roadmaps/components/roadmaps-view";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: 'AI Engineer Roadmap 2025 — Step-by-Step Learning Path',
  description: 'The complete roadmap to become an AI engineer in 2025. Covers every skill from Python fundamentals to production LLM systems.',
  alternates: {
    canonical: 'https://tensor-track.vercel.app/roadmaps',
  },
};

export default function RoadmapsPage() {
  return (
    <>
      <Header />
      <main className="flex-1 bg-background text-foreground py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <RoadmapsView />
      </main>
    </>
  );
}
