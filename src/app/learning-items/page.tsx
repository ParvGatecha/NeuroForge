import { Header } from "@/shared/components/header";
import { LearningItemsExplorer } from "@/modules/questions/components/questions-explorer";
import { JsonLd } from "@/shared/components/json-ld";
import { Metadata } from "next";
import fs from "fs";
import path from "path";

export const metadata: Metadata = {
  title: 'AI Engineering Curriculum — 100+ Curated Resources',
  description: "Browse TensorTrack's full AI engineering curriculum: Python, Statistics, Classical ML, Deep Learning, LLMs, RAG, AI Agents, and System Design. Structured, progressive, and free.",
  alternates: {
    canonical: 'https://tensor-track.vercel.app/learning-items',
  },
};

const courseSchema = {
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "AI Engineering Complete Curriculum",
  "description": "A structured, first-principles curriculum for becoming an AI engineer covering Python, Statistics, ML, Deep Learning, LLMs, RAG, AI Agents, and System Design.",
  "provider": {
    "@type": "Organization",
    "name": "TensorTrack",
    "url": "https://tensor-track.vercel.app"
  },
  "hasCourseInstance": [
    {
      "@type": "CourseInstance",
      "name": "Python for AI",
      "courseMode": "online"
    },
    {
      "@type": "CourseInstance", 
      "name": "Statistics & Math for ML",
      "courseMode": "online"
    },
    {
      "@type": "CourseInstance",
      "name": "Classical Machine Learning",
      "courseMode": "online"
    },
    {
      "@type": "CourseInstance",
      "name": "Deep Learning",
      "courseMode": "online"
    },
    {
      "@type": "CourseInstance",
      "name": "Large Language Models",
      "courseMode": "online"
    },
    {
      "@type": "CourseInstance",
      "name": "RAG Systems",
      "courseMode": "online"
    },
    {
      "@type": "CourseInstance",
      "name": "AI Agents",
      "courseMode": "online"
    },
    {
      "@type": "CourseInstance",
      "name": "System Design for AI",
      "courseMode": "online"
    }
  ],
  "educationalLevel": "Intermediate",
  "teaches": [
    "Machine Learning",
    "Deep Learning", 
    "Large Language Models",
    "RAG Systems",
    "AI Agents",
    "MLOps",
    "System Design"
  ],
  "isAccessibleForFree": true,
  "url": "https://tensor-track.vercel.app"
};

export default async function LearningItemsPage(props: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  await props.searchParams;

  const indexPath = path.join(process.cwd(), "content/search_index.json");
  const indexContent = fs.readFileSync(indexPath, "utf-8");
  const items = JSON.parse(indexContent);

  return (
    <>
      <JsonLd data={courseSchema} />
      <Header />
      <main className="flex-1 bg-background text-foreground py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <LearningItemsExplorer items={items} />
      </main>
    </>
  );
}
