import { getXpForLevel, getLevelFromXp, getLevelProgress } from "../src/modules/progress/xp";
import { getRecommendedNextLearningItem, getAllLearningItems } from "../src/modules/roadmaps/roadmap";

function assert(condition: boolean, message: string) {
  if (!condition) {
    console.error(`❌ Assertion Failed: ${message}`);
    process.exit(1);
  }
}

function testXpEngine() {
  console.log("Testing XP Engine...");

  assert(getXpForLevel(1) === 0, "Level 1 should require 0 XP");
  assert(getXpForLevel(2) === 100, "Level 2 should require 100 XP");
  assert(getXpForLevel(3) === 282, "Level 3 should require 282 XP");

  assert(getLevelFromXp(0) === 1, "0 XP should be Level 1");
  assert(getLevelFromXp(50) === 1, "50 XP should be Level 1");
  assert(getLevelFromXp(100) === 2, "100 XP should be Level 2");
  assert(getLevelFromXp(282) === 3, "282 XP should be Level 3");
  assert(getLevelFromXp(1000) === 5, "1000 XP should be Level 5");

  const p = getLevelProgress(150);
  assert(p.level === 2, "150 XP should be Level 2");
  assert(p.progressInLevel === 50, "150 XP progress should be 50 XP into level");
  assert(p.percentage === 27, "Percentage should be 27%");

  console.log("✅ XP Engine tests passed!");
}

function testRoadmapEngine() {
  console.log("Testing Roadmap Sequencing Engine...");

  const all = getAllLearningItems();
  assert(all.length === 100, `Expected 100 learning items, got ${all.length}`);

  const next1 = getRecommendedNextLearningItem([]);
  assert(next1 !== null && next1.id === 1, `Recommended first item should be ID 1, got ${next1?.id}`);

  const completedPython = Array.from({ length: 10 }, (_, i) => i + 1);
  const next2 = getRecommendedNextLearningItem(completedPython);
  assert(
    next2 !== null && next2.id === 11,
    `Recommended after Python should be statistics (ID 11), got ${next2?.id}`
  );

  const completedAll = Array.from({ length: 100 }, (_, i) => i + 1);
  const next3 = getRecommendedNextLearningItem(completedAll);
  assert(next3 === null, `Recommended when all completed should be null, got ${next3}`);

  console.log("✅ Roadmap Engine tests passed!");
}

function runAllTests() {
  console.log("Starting NeuroForge unit tests...");
  testXpEngine();
  testRoadmapEngine();
  console.log("\n🎉 All tests completed successfully!");
}

runAllTests();
