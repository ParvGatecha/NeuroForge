import { Header } from "@/shared/components/header";
import { AdminView } from "@/modules/admin/components/admin-view";

export default function AdminPage() {
  return (
    <>
      <Header />
      <main className="flex-1 bg-background text-foreground py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <AdminView />
      </main>
    </>
  );
}
