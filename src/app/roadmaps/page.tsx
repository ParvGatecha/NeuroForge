import { Header } from "@/shared/components/header";
import { RoadmapsView } from "@/modules/roadmaps/components/roadmaps-view";

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
