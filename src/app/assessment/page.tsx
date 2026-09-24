import { Header } from "@/shared/components/header";
import { AssessmentView } from "@/modules/assessment/components/assessment-view";
import { JsonLd } from "@/shared/components/json-ld";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "AI Engineer Readiness Assessment — TensorTrack",
  description:
    "Find out how AI-engineer-ready you are in 10 minutes. Test first-principles knowledge across Python, ML, Deep Learning, LLMs, RAG, and AI Agents — and get your personalized learning path.",
  alternates: {
    canonical: "https://tensor-track.vercel.app/assessment",
  },
  openGraph: {
    title: "How AI Engineer Ready Are You? | TensorTrack Assessment",
    description:
      "Take the free 10-minute diagnostic. Discover your proficiency across 8 AI engineering tracks and unlock your recommended learning blueprint.",
    url: "https://tensor-track.vercel.app/assessment",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "How AI Engineer Ready Are You? | TensorTrack",
    description: "Take the free 10-minute diagnostic. Discover your proficiency across 8 AI engineering tracks.",
  },
};

const assessmentSchema = {
  "@context": "https://schema.org",
  "@type": "Quiz",
  "name": "TensorTrack AI Engineer Readiness Assessment",
  "description": "Comprehensive 10-minute first-principles diagnostic assessment for AI and Machine Learning Engineers.",
  "educationalLevel": "Intermediate to Advanced",
  "about": [
    "Python Concurrency",
    "Mathematical Statistics",
    "Machine Learning",
    "Deep Learning",
    "Large Language Models",
    "RAG Engineering",
    "AI Agents",
    "AI System Design"
  ],
  "provider": {
    "@type": "Organization",
    "name": "TensorTrack",
    "url": "https://tensor-track.vercel.app"
  }
};

export default function AssessmentPage() {
  return (
    <>
      <JsonLd data={assessmentSchema} />
      <Header />
      <main className="flex-1 bg-background text-foreground py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <AssessmentView />
      </main>
    </>
  );
}
