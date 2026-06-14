import fs from "fs";
import path from "path";

function getFilesRecursively(dir: string): string[] {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = entries.map((entry) => {
    const res = path.resolve(dir, entry.name);
    return entry.isDirectory() ? getFilesRecursively(res) : res;
  });
  return Array.prototype.concat(...files);
}

function main() {
  console.log("Building TensorTrack search index...");
  const contentDir = path.join(__dirname, "../content");
  const outputFile = path.join(__dirname, "../content/search_index.json");

  if (!fs.existsSync(contentDir)) {
    console.error(`Error: Content directory does not exist at ${contentDir}`);
    process.exit(1);
  }

  const allFiles = getFilesRecursively(contentDir);
  const jsonFiles = allFiles.filter(
    (f) =>
      f.endsWith(".json") &&
      !f.includes("index.json") &&
      !f.includes("roadmap.json") &&
      !f.includes("search_index.json") &&
      !f.includes("local_mock_db.json")
  );

  console.log(`Found ${jsonFiles.length} learning item files to index.`);

  const searchIndex: any[] = [];

  jsonFiles.forEach((filePath) => {
    try {
      const fileContent = fs.readFileSync(filePath, "utf-8");
      const q = JSON.parse(fileContent);

      searchIndex.push({
        id: q.id,
        slug: q.slug,
        title: q.title,
        section: q.section,
        difficulty: q.difficulty,
        theory_resource: q.theory_resource,
        practice_resource: q.practice_resource,
        estimated_time_minutes: q.estimated_time_minutes,
        tags: q.tags,
        learning_objectives: q.learning_objectives,
        description: q.description,
        prerequisites: q.prerequisites
      });
    } catch (e) {
      console.error(`Error indexing file: ${filePath}`, e);
    }
  });

  searchIndex.sort((a, b) => a.id - b.id);

  fs.writeFileSync(outputFile, JSON.stringify(searchIndex, null, 2), "utf-8");
  console.log(`Search index successfully built with ${searchIndex.length} items at: ${outputFile}`);
}

main();
