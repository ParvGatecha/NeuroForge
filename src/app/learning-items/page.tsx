import { Header } from "@/shared/components/header";
import { LearningItemsExplorer } from "@/modules/questions/components/questions-explorer";
import fs from "fs";
import path from "path";

export default async function LearningItemsPage(props: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  await props.searchParams;

  const indexPath = path.join(process.cwd(), "content/search_index.json");
  const indexContent = fs.readFileSync(indexPath, "utf-8");
  const items = JSON.parse(indexContent);

  return (
    <>
      <Header />
      <main className="flex-1 bg-background text-foreground py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <LearningItemsExplorer items={items} />
      </main>
    </>
  );
}
