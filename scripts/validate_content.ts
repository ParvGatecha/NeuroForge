import fs from "fs";
import path from "path";
import { z } from "zod";

const TheoryResourceTypeEnum = z.enum(["article", "blog", "documentation", "youtube", "research-paper", "github", "course"]);
const PracticePlatformEnum = z.enum(["DEEP_ML", "KAGGLE", "HUGGING_FACE", "GITHUB", "LANGCHAIN", "LANGGRAPH", "LLAMAINDEX", "CUSTOM", "EXTERNAL"]);

const LearningItemSchema = z.object({
  id: z.number().int().positive(),
  slug: z.string().min(1),
  title: z.string().min(1),
  section: z.string().min(1),
  difficulty: z.enum(["Easy", "Medium", "Hard"]),
  theory_resource: z.object({
    title: z.string().min(1),
    url: z.string().url(),
    type: TheoryResourceTypeEnum
  }),
  practice_resource: z.object({
    platform: PracticePlatformEnum,
    title: z.string().min(1),
    url: z.string().url()
  }),
  estimated_time_minutes: z.number().positive(),
  tags: z.array(z.string().min(1)),
  learning_objectives: z.array(z.string().min(1)),
  description: z.string().min(1),
  prerequisites: z.array(z.number().int())
});

type LearningItem = z.infer<typeof LearningItemSchema>;

function getFilesRecursively(dir: string): string[] {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = entries.map((entry) => {
    const res = path.resolve(dir, entry.name);
    return entry.isDirectory() ? getFilesRecursively(res) : res;
  });
  return Array.prototype.concat(...files);
}

function main() {
  console.log("Starting NeuroForge content validation...");
  const contentDir = path.join(__dirname, "../content");
  
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

  console.log(`Found ${jsonFiles.length} learning item files to validate.`);
  
  if (jsonFiles.length !== 100) {
    console.warn(`Warning: Expected exactly 100 learning items, found ${jsonFiles.length}.`);
  }

  let errorsCount = 0;
  
  jsonFiles.forEach((filePath) => {
    const relativePath = path.relative(path.join(__dirname, ".."), filePath);
    try {
      const fileContent = fs.readFileSync(filePath, "utf-8");
      const jsonData = JSON.parse(fileContent);
      
      const result = LearningItemSchema.safeParse(jsonData);
      if (!result.success) {
        errorsCount++;
        console.error(`\nValidation failed for: ${relativePath}`);
        console.error(JSON.stringify(result.error.format(), null, 2));
      }
    } catch (e) {
      errorsCount++;
      console.error(`\nError parsing file: ${relativePath}`);
      console.error(e);
    }
  });

  if (errorsCount > 0) {
    console.error(`\nValidation complete: FAILED with ${errorsCount} errors.`);
    process.exit(1);
  } else {
    console.log("\nValidation complete: SUCCESS. All files are schema compliant!");
    process.exit(0);
  }
}

main();
