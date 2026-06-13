import { Header } from "@/shared/components/header";
import { SettingsView } from "@/modules/settings/components/settings-view";

export default function SettingsPage() {
  return (
    <>
      <Header />
      <main className="flex-1 bg-background text-foreground py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <SettingsView />
      </main>
    </>
  );
}
