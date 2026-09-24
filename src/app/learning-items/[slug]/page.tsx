import { Header } from "@/shared/components/header";
import { LearningItemWorkspace } from "@/modules/questions/components/question-workspace";
import { getLearningItemBySlug } from "@/modules/questions/questions";
import { JsonLd } from "@/shared/components/json-ld";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import fs from "fs";
import path from "path";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const item = getLearningItemBySlug(slug);
  if (!item) {
    return {
      title: "Learning Item Not Found",
    };
  }

  const cleanTitle = `${item.title} — ${item.section.charAt(0).toUpperCase() + item.section.slice(1)} Track`;
  const cleanDescription = item.description || `Study ${item.title} as part of the TensorTrack AI Engineer curriculum.`;

  return {
    title: cleanTitle,
    description: cleanDescription,
    keywords: [...item.tags, item.section, item.difficulty, "AI engineering", "interview prep"],
    alternates: {
      canonical: `https://tensor-track.vercel.app/learning-items/${slug}`,
    },
    openGraph: {
      title: `${item.title} | TensorTrack`,
      description: cleanDescription,
      url: `https://tensor-track.vercel.app/learning-items/${slug}`,
      type: "article",
    },
    twitter: {
      card: "summary_large_image",
      title: `${item.title} | TensorTrack`,
      description: cleanDescription,
    },
  };
}

export async function generateStaticParams() {
  try {
    const indexPath = path.join(process.cwd(), "content/search_index.json");
    if (fs.existsSync(indexPath)) {
      const indexContent = fs.readFileSync(indexPath, "utf-8");
      const items = JSON.parse(indexContent) as Array<{ slug: string }>;
      return items.map((item) => ({
        slug: item.slug,
      }));
    }
  } catch (e) {
    console.error("Failed to generate static params for learning items", e);
  }
  return [];
}

export default async function LearningItemPage({ params }: PageProps) {
  const { slug } = await params;

  const item = getLearningItemBySlug(slug);
  if (!item) {
    notFound();
  }

  const learningResourceSchema = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": item.title,
    "description": item.description,
    "educationalLevel": item.difficulty,
    "timeRequired": `PT${item.estimated_time_minutes}M`,
    "keywords": item.tags.join(", "),
    "learningResourceType": "Tutorial",
    "provider": {
      "@type": "Organization",
      "name": "TensorTrack",
      "url": "https://tensor-track.vercel.app"
    }
  };

  return (
    <>
      <JsonLd data={learningResourceSchema} />
      <Header />
      <main className="flex-1 bg-background text-foreground py-6 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <LearningItemWorkspace item={item} />
      </main>
    </>
  );
}
