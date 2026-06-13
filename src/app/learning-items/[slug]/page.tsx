import { Header } from "@/shared/components/header";
import { LearningItemWorkspace } from "@/modules/questions/components/question-workspace";
import { getLearningItemBySlug } from "@/modules/questions/questions";
import { notFound } from "next/navigation";
import fs from "fs";
import path from "path";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  try {
    const indexPath = path.join(process.cwd(), "content/search_index.json");
    if (fs.existsSync(indexPath)) {
      const indexContent = fs.readFileSync(indexPath, "utf-8");
      const items = JSON.parse(indexContent);
      return items.map((item: any) => ({
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

  return (
    <>
      <Header />
      <main className="flex-1 bg-background text-foreground py-6 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <LearningItemWorkspace item={item} />
      </main>
    </>
  );
}
