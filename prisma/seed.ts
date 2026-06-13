import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

const achievements = [
  {
    code: "FIRST_QUESTION",
    name: "First Step",
    description: "Complete your first challenge",
    xpReward: 50,
  },
  {
    code: "PYTHON_EXPLORER",
    name: "Python Explorer",
    description: "Complete all Python challenges",
    xpReward: 100,
  },
  {
    code: "STATS_GURU",
    name: "Statistics Guru",
    description: "Complete all Statistics challenges",
    xpReward: 150,
  },
  {
    code: "ML_MASTER",
    name: "Machine Learning Master",
    description: "Complete all Machine Learning challenges",
    xpReward: 200,
  },
  {
    code: "DL_WIZARD",
    name: "Deep Learning Wizard",
    description: "Complete all Deep Learning challenges",
    xpReward: 250,
  },
  {
    code: "LLM_EXPERT",
    name: "LLM Expert",
    description: "Complete all Large Language Model challenges",
    xpReward: 250,
  },
  {
    code: "RAG_CHAMP",
    name: "RAG Champion",
    description: "Complete all RAG challenges",
    xpReward: 200,
  },
  {
    code: "AGENT_COMMANDER",
    name: "Agent Commander",
    description: "Complete all AI Agent challenges",
    xpReward: 200,
  },
  {
    code: "ARCHITECT",
    name: "System Design Architect",
    description: "Complete all System Design challenges",
    xpReward: 250,
  },
  {
    code: "STREAK_3",
    name: "Consistent Learner",
    description: "Maintain a 3-day learning streak",
    xpReward: 100,
  },
  {
    code: "STREAK_7",
    name: "Unstoppable",
    description: "Maintain a 7-day learning streak",
    xpReward: 250,
  },
  {
    code: "LEVEL_5",
    name: "Rising Star",
    description: "Reach Level 5",
    xpReward: 200,
  },
  {
    code: "LEVEL_10",
    name: "Elite AI Engineer",
    description: "Reach Level 10",
    xpReward: 500,
  },
];

async function main() {
  console.log("Seeding achievements...");
  for (const ach of achievements) {
    await prisma.achievement.upsert({
      where: { code: ach.code },
      update: {
        name: ach.name,
        description: ach.description,
        xpReward: ach.xpReward,
      },
      create: {
        code: ach.code,
        name: ach.name,
        description: ach.description,
        xpReward: ach.xpReward,
      },
    });
  }
  console.log("Achievements seeded successfully!");
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
