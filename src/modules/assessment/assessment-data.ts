export interface AssessmentQuestion {
  id: number;
  trackKey: "python" | "statistics" | "machine-learning" | "deep-learning" | "llm" | "rag" | "agents" | "system-design";
  trackTitle: string;
  difficulty: "Easy" | "Medium" | "Hard";
  question: string;
  codeSnippet?: string;
  options: {
    id: string;
    text: string;
  }[];
  correctOptionId: string;
  explanation: string;
}

export interface TrackScore {
  key: string;
  title: string;
  score: number; // percentage 0-100
  correctCount: number;
  totalQuestions: number;
  status: "Strong" | "Competent" | "Needs Work" | "Critical Gap";
  color: string;
}

export interface AssessmentResult {
  overallScore: number;
  readinessLevel: string;
  readinessSummary: string;
  trackScores: TrackScore[];
  strongestTracks: string[];
  weakestTracks: string[];
  recommendedItemSlugs: string[];
}

export const ASSESSMENT_QUESTIONS: AssessmentQuestion[] = [
  // 1. PYTHON CONCURRENCY & ARCHITECTURE
  {
    id: 1,
    trackKey: "python",
    trackTitle: "Python Concurrency",
    difficulty: "Medium",
    question: "In standard CPython, why does spawning multiple threads fail to speed up CPU-bound array operations, and which approach provides true CPU parallelism?",
    options: [
      { id: "A", text: "The Global Interpreter Lock (GIL) limits execution to one native thread at a time; use multiprocessing or C-extensions." },
      { id: "B", text: "Python threads run in simulated user-space; use asyncio event loops instead." },
      { id: "C", text: "The cyclic garbage collector locks all threads during iterations; use daemon threads." },
      { id: "D", text: "CPython allocates memory sequentially; use concurrent.futures.ThreadPoolExecutor." }
    ],
    correctOptionId: "A",
    explanation: "CPython's Global Interpreter Lock (GIL) ensures only one thread executes Python bytecode at any given moment. For CPU-bound tasks, the multiprocessing module or C-extensions (like NumPy/PyTorch) must be used to bypass the GIL across multiple cores."
  },
  {
    id: 2,
    trackKey: "python",
    trackTitle: "Python Concurrency",
    difficulty: "Hard",
    question: "What happens if a developer calls time.sleep(5) or a synchronous database driver inside an async def FastAPI/asyncio endpoint?",
    options: [
      { id: "A", text: "Asyncio automatically offloads it to a background thread pool without any latency penalty." },
      { id: "B", text: "It blocks the entire OS process and event loop, freezing all concurrent requests for 5 seconds." },
      { id: "C", text: "Asyncio raises an unhandled AsyncBlockedException in strict mode." },
      { id: "D", text: "Only that specific coroutine is suspended while other coroutines continue uninterrupted." }
    ],
    correctOptionId: "B",
    explanation: "Because asyncio relies on cooperative multitasking on a single thread, any synchronous blocking call blocks the entire event loop, freezing all other pending and incoming client requests."
  },

  // 2. STATISTICS & MATH FOR ML
  {
    id: 3,
    trackKey: "statistics",
    trackTitle: "Mathematical Stats",
    difficulty: "Medium",
    question: "What is the fundamental difference between Maximum Likelihood Estimation (MLE) and Maximum A Posteriori (MAP) estimation?",
    options: [
      { id: "A", text: "MLE minimizes mean squared error while MAP optimizes cross-entropy." },
      { id: "B", text: "MAP incorporates a prior probability distribution P(θ) over parameters, acting as a Bayesian regularizer." },
      { id: "C", text: "MLE requires continuous variables whereas MAP only works on discrete distributions." },
      { id: "D", text: "MLE calculates the posterior distribution whereas MAP calculates the sample variance." }
    ],
    correctOptionId: "B",
    explanation: "MAP maximizes P(θ|X) ∝ P(X|θ) · P(θ). The prior P(θ) regularizes parameter estimation (e.g. a Gaussian prior on weights mathematically equates to L2 weight decay regularization)."
  },
  {
    id: 4,
    trackKey: "statistics",
    trackTitle: "Mathematical Stats",
    difficulty: "Medium",
    question: "In an A/B test between two LLM prompt strategies, your statistical test returns a p-value of 0.03. What is the precise interpretation?",
    options: [
      { id: "A", text: "There is a 97% probability that Prompt Strategy B is strictly better than Strategy A." },
      { id: "B", text: "If the null hypothesis of no difference were true, there is a 3% probability of observing an effect this extreme by random chance." },
      { id: "C", text: "There is a 3% chance that the experiment produced false measurements." },
      { id: "D", text: "The statistical power of the test is exactly 97%." }
    ],
    correctOptionId: "B",
    explanation: "The p-value is the probability of obtaining test results at least as extreme as the observed results, assuming that the null hypothesis is correct. It is not the probability that the hypothesis itself is true or false."
  },

  // 3. CLASSICAL MACHINE LEARNING
  {
    id: 5,
    trackKey: "machine-learning",
    trackTitle: "Classical ML",
    difficulty: "Medium",
    question: "Your Random Forest classifier achieves 99.4% accuracy on training data but drops to 71.2% on cross-validation data. Which diagnosis and mitigation is most accurate?",
    options: [
      { id: "A", text: "High bias (underfitting); increase tree depth and add polynomial interaction features." },
      { id: "B", text: "High variance (overfitting); restrict max_depth, increase min_samples_leaf, or use feature bagging." },
      { id: "C", text: "Data leakage; switch to an unregularized Logistic Regression model." },
      { id: "D", text: "Class imbalance; change the evaluation metric to Accuracy." }
    ],
    correctOptionId: "B",
    explanation: "A severe gap between training accuracy and cross-validation accuracy indicates high variance (overfitting). Restricting tree growth (max_depth, min_samples_leaf) and increasing random sampling reduces tree correlation and variance."
  },
  {
    id: 6,
    trackKey: "machine-learning",
    trackTitle: "Classical ML",
    difficulty: "Easy",
    question: "In a critical anomaly detection system where failing to detect a fraudulent transaction incurs massive financial loss, which metric should be prioritized?",
    options: [
      { id: "A", text: "Precision (minimizing false alarms)" },
      { id: "B", text: "Recall / Sensitivity (minimizing false negatives)" },
      { id: "C", text: "Raw Accuracy" },
      { id: "D", text: "Specificity alone" }
    ],
    correctOptionId: "B",
    explanation: "When false negatives have high costs (missing fraud, missing cancer), Recall must be maximized to ensure as few anomalies slip through as possible."
  },

  // 4. DEEP LEARNING ARCHITECTURES
  {
    id: 7,
    trackKey: "deep-learning",
    trackTitle: "Deep Learning",
    difficulty: "Hard",
    question: "How do Residual Connections (y = F(x) + x) in ResNets and Transformers fundamentally mitigate the vanishing gradient problem in deep models?",
    options: [
      { id: "A", text: "They eliminate non-linear activation functions completely across all hidden layers." },
      { id: "B", text: "During backprop, the gradient includes a constant +1 identity term (∂y/∂x = ∂F/∂x + 1), allowing gradients to flow back directly without vanishing." },
      { id: "C", text: "They normalize layer weights to zero mean and unit variance at every forward pass." },
      { id: "D", text: "They dynamically scale the learning rate based on weight eigenvalues." }
    ],
    correctOptionId: "B",
    explanation: "Because ∂(F(x) + x)/∂x = ∂F(x)/∂x + I, the gradient contains the identity matrix I. Even if ∂F(x)/∂x vanishes, the gradient can still propagate backwards unchanged through the residual path."
  },
  {
    id: 8,
    trackKey: "deep-learning",
    trackTitle: "Deep Learning",
    difficulty: "Medium",
    question: "In Scaled Dot-Product Attention: Attention(Q, K, V) = Softmax(QKᵀ / √d_k) · V, why is the term divided by √d_k?",
    options: [
      { id: "A", text: "To guarantee that the resulting attention matrix is strictly symmetric." },
      { id: "B", text: "For large dimensions d_k, dot products grow large, pushing Softmax into regions with near-zero gradients; √d_k scales variance back to 1." },
      { id: "C", text: "To reduce matrix multiplication time complexity from O(N²) to O(N)." },
      { id: "D", text: "To prevent queries and keys from becoming linearly dependent." }
    ],
    correctOptionId: "B",
    explanation: "If components of Q and K are independent random variables with zero mean and variance 1, their dot product has variance d_k. Dividing by √d_k scales the variance back to 1, preventing Softmax from saturating and killing backpropagation gradients."
  },

  // 5. LARGE LANGUAGE MODELS (LLMs)
  {
    id: 9,
    trackKey: "llm",
    trackTitle: "Large Language Models",
    difficulty: "Medium",
    question: "How does LoRA (Low-Rank Adaptation) enable parameter-efficient fine-tuning of large models like LLaMA without updating the full weight matrix W₀ ∈ ℝᵈˣᵏ?",
    options: [
      { id: "A", text: "It randomly prunes 90% of the weights in W₀ and updates only the surviving non-zero weights." },
      { id: "B", text: "It freezes W₀ and parameterizes the weight update as ΔW = B · A, where B ∈ ℝᵈˣʳ and A ∈ ℝʳˣᵏ with rank r ≪ min(d, k)." },
      { id: "C", text: "It quantizes W₀ into 4-bit NormalFloat (NF4) and disables backward passes on attention layers." },
      { id: "D", text: "It trains an external prompt embedding while keeping all transformer layers frozen." }
    ],
    correctOptionId: "B",
    explanation: "LoRA decomposes the weight update into two low-rank matrices B and A. For a matrix of 4096×4096 and rank r=8, trainable parameters drop from 16.7M down to just 65,536 (a 99.6% reduction in GPU VRAM and optimizer states)."
  },
  {
    id: 10,
    trackKey: "llm",
    trackTitle: "Large Language Models",
    difficulty: "Medium",
    question: "What is the primary function of the KV (Key-Value) Cache during autoregressive LLM text generation?",
    options: [
      { id: "A", text: "It caches prompts in Redis across different user sessions." },
      { id: "B", text: "It stores previously computed Key and Value vectors so past tokens do not need to be recomputed at each new token generation step." },
      { id: "C", text: "It compresses model weights from 16-bit to 4-bit precision inside GPU SRAM." },
      { id: "D", text: "It generates speculative draft tokens in parallel." }
    ],
    correctOptionId: "B",
    explanation: "During autoregressive decoding, each step only generates one token. By caching Key and Value tensors of previous tokens in GPU memory, generation scales as O(N) per step instead of quadratic O(N²) prompt recomputation."
  },

  // 6. RETRIEVAL-AUGMENTED GENERATION (RAG)
  {
    id: 11,
    trackKey: "rag",
    trackTitle: "RAG Engineering",
    difficulty: "Medium",
    question: "Why do production RAG systems deploy Hybrid Search combining Dense Vector embeddings with Sparse BM25 via Reciprocal Rank Fusion (RRF)?",
    options: [
      { id: "A", text: "Dense embeddings handle exact keyword matches (product codes, SKUs) while BM25 handles conceptual semantics." },
      { id: "B", text: "Dense embeddings excel at conceptual semantic queries, while BM25 handles exact entity names, acronyms, and rare tokens where embeddings often fail." },
      { id: "C", text: "BM25 serves as a GPU accelerator for vector indexing algorithms like HNSW." },
      { id: "D", text: "RRF automatically generates synthetic training data for re-ranker fine-tuning." }
    ],
    correctOptionId: "B",
    explanation: "Dense vectors capture paraphrasing and semantic nuance but can blur specific serial numbers, error codes, and technical acronyms. Sparse BM25 excels at exact keyword matching. Blending them with RRF gives the best of both worlds."
  },
  {
    id: 12,
    trackKey: "rag",
    trackTitle: "RAG Engineering",
    difficulty: "Easy",
    question: "What is the 'Lost in the Middle' phenomenon observed in long-context LLM retrieval?",
    options: [
      { id: "A", text: "Vector databases fail to traverse nodes in the middle of hierarchical HNSW graphs." },
      { id: "B", text: "LLMs recall information located at the beginning or end of their prompt context far better than information positioned in the middle." },
      { id: "C", text: "Recursive chunkers split sentences in half when sliding window stride is misconfigured." },
      { id: "D", text: "Tokenizers experience attention degradation when sequence length exceeds 4,096 tokens." }
    ],
    correctOptionId: "B",
    explanation: "Research shows that transformer attention exhibits a U-shaped accuracy curve: key facts placed near the very beginning or end of long input prompts are retrieved with high fidelity, while facts buried in the middle are frequently missed or hallucinated."
  },

  // 7. AI AGENTS & TOOL CALLING
  {
    id: 13,
    trackKey: "agents",
    trackTitle: "AI Agent Systems",
    difficulty: "Medium",
    question: "In the ReAct (Reason + Act) prompting framework, what is the core cycle executed by the LLM agent?",
    options: [
      { id: "A", text: "A React.js state hook cycle for streaming tokens to the browser." },
      { id: "B", text: "An interleaved cycle of Thought (reasoning trace) → Action (tool call) → Observation (environment output) until task resolution." },
      { id: "C", text: "A deterministic rule-based finite state machine with zero stochastic calls." },
      { id: "D", text: "A multi-threaded map-reduce execution across fine-tuned sub-models." }
    ],
    correctOptionId: "B",
    explanation: "ReAct combines reasoning and acting: the model verbalizes a 'Thought' about what to do next, emits an 'Action' to invoke an external tool/API, inspects the tool's 'Observation', and iterates toward the final answer."
  },
  {
    id: 14,
    trackKey: "agents",
    trackTitle: "AI Agent Systems",
    difficulty: "Hard",
    question: "When an autonomous AI agent executes a tool and encounters an API validation error or database exception, what is the robust architectural response?",
    options: [
      { id: "A", text: "Immediately terminate the agent process and alert the user." },
      { id: "B", text: "Inject the error payload directly back into the LLM context as an Observation, allowing the agent to self-correct its parameters on the next turn." },
      { id: "C", text: "Re-send the identical tool request in a loop until a 200 OK is received." },
      { id: "D", text: "Clear all previous chat history to prevent memory corruption." }
    ],
    correctOptionId: "B",
    explanation: "Autonomous agents leverage error messages as actionable environmental feedback. By presenting the error trace back to the LLM, the model can adjust invalid JSON types, fix SQL syntax, or choose alternative fallback tools."
  },

  // 8. AI SYSTEM DESIGN & SERVING
  {
    id: 15,
    trackKey: "system-design",
    trackTitle: "AI System Design",
    difficulty: "Hard",
    question: "How does PagedAttention (implemented in vLLM) achieve dramatic throughput gains in LLM serving compared to naive Hugging Face transformers?",
    options: [
      { id: "A", text: "By shifting all inference computation to CPU RAM via NVMe swap." },
      { id: "B", text: "By managing the KV cache in non-contiguous virtual memory blocks inspired by OS paging, virtually eliminating memory fragmentation and allowing dynamic batching." },
      { id: "C", text: "By compressing all weights down to 1-bit binary representations." },
      { id: "D", text: "By replacing Multi-Head Attention with Recurrent Neural Networks." }
    ],
    correctOptionId: "B",
    explanation: "In standard LLM serving, KV cache memory must be allocated contiguously for maximum sequence length, wasting up to 60-80% of VRAM due to internal and external fragmentation. PagedAttention stores KV tensors in non-contiguous blocks, allowing near-zero waste and boosting concurrency 2-4x."
  },
  {
    id: 16,
    trackKey: "system-design",
    trackTitle: "AI System Design",
    difficulty: "Medium",
    question: "Where should prompt safety guardrails (e.g. prompt injection filters, PII detection, jailbreak analyzers) be placed in an enterprise LLM architecture?",
    options: [
      { id: "A", text: "Directly in the client-side JavaScript bundle before HTTP dispatch." },
      { id: "B", text: "Upstream of the LLM inference gateway to intercept and reject malicious or non-compliant queries before expensive GPU resources are consumed." },
      { id: "C", text: "Inside the offline batch embedding pipeline." },
      { id: "D", text: "Only in the asynchronous audit logging database after response delivery." }
    ],
    correctOptionId: "B",
    explanation: "Guardrails must execute server-side upstream of the LLM. Intercepting attacks and PII before inference prevents prompt injection, protects downstream systems, and avoids wasting costly GPU compute cycles on malicious inputs."
  }
];

export const TRACK_CONFIGS: { [key: string]: { title: string; color: string; recommendedSlugs: string[] } } = {
  "python": {
    title: "Python Concurrency",
    color: "from-blue-500 to-indigo-500",
    recommendedSlugs: ["005-asyncio-concurrency", "011-multiprocessing-pool", "007-context-managers"]
  },
  "statistics": {
    title: "Mathematical Stats",
    color: "from-purple-500 to-pink-500",
    recommendedSlugs: ["025-mle-estimation", "027-hypothesis-testing", "029-bayes-theorem"]
  },
  "machine-learning": {
    title: "Classical ML",
    color: "from-emerald-500 to-teal-500",
    recommendedSlugs: ["052-bias-variance-tradeoff", "061-random-forest-depth", "074-roc-auc-metrics"]
  },
  "deep-learning": {
    title: "Deep Learning",
    color: "from-rose-500 to-orange-500",
    recommendedSlugs: ["092-residual-connections", "098-scaled-dot-product-attention", "095-adam-optimizer-math"]
  },
  "llm": {
    title: "Large Language Models",
    color: "from-violet-500 to-purple-600",
    recommendedSlugs: ["122-lora-fine-tuning", "125-kv-cache-optimization", "131-speculative-decoding"]
  },
  "rag": {
    title: "RAG Engineering",
    color: "from-cyan-500 to-blue-500",
    recommendedSlugs: ["152-hybrid-search-rrf", "155-lost-in-the-middle-mitigation", "159-reranking-cross-encoders"]
  },
  "agents": {
    title: "AI Agent Systems",
    color: "from-indigo-600 to-violet-500",
    recommendedSlugs: ["172-react-execution-loop", "175-tool-calling-schemas", "179-state-graph-agent-memory"]
  },
  "system-design": {
    title: "AI System Design",
    color: "from-teal-500 to-emerald-600",
    recommendedSlugs: ["192-vllm-paged-attention", "195-llm-serving-guardrails", "198-distributed-training-zero"]
  }
};

export function computeAssessmentResult(answers: { [questionId: number]: string }): AssessmentResult {
  const trackStats: { [trackKey: string]: { correct: number; total: number; title: string; color: string } } = {};

  Object.entries(TRACK_CONFIGS).forEach(([key, conf]) => {
    trackStats[key] = { correct: 0, total: 0, title: conf.title, color: conf.color };
  });

  let totalCorrect = 0;

  ASSESSMENT_QUESTIONS.forEach((q) => {
    const track = trackStats[q.trackKey];
    if (track) {
      track.total += 1;
      if (answers[q.id] === q.correctOptionId) {
        track.correct += 1;
        totalCorrect += 1;
      }
    }
  });

  const trackScores: TrackScore[] = Object.entries(trackStats).map(([key, stat]) => {
    const score = stat.total > 0 ? Math.round((stat.correct / stat.total) * 100) : 0;
    let status: TrackScore["status"] = "Critical Gap";
    if (score >= 80) status = "Strong";
    else if (score >= 50) status = "Competent";
    else if (score >= 25) status = "Needs Work";

    return {
      key,
      title: stat.title,
      score,
      correctCount: stat.correct,
      totalQuestions: stat.total,
      status,
      color: stat.color
    };
  });

  const overallScore = Math.round((totalCorrect / ASSESSMENT_QUESTIONS.length) * 100);

  // Sort tracks
  const sortedTracks = [...trackScores].sort((a, b) => b.score - a.score);
  const strongestTracks = sortedTracks.slice(0, 2).map((t) => t.title);
  const weakest = [...trackScores].sort((a, b) => a.score - b.score);
  const weakestTracks = weakest.slice(0, 2).map((t) => t.title);

  // Recommendations: pick from weakest tracks
  const recommendedItemSlugs: string[] = [];
  weakest.slice(0, 3).forEach((track) => {
    const config = TRACK_CONFIGS[track.key];
    if (config && config.recommendedSlugs) {
      recommendedItemSlugs.push(...config.recommendedSlugs.slice(0, 1));
    }
  });

  let readinessLevel = "AI Engineer Aspirant";
  let readinessSummary = "You have an emerging foundation in programming, but critical architectural and machine learning gaps must be addressed before interview readiness.";

  if (overallScore >= 85) {
    readinessLevel = "Senior AI Systems Engineer";
    readinessSummary = "Exceptional first-principles depth across concurrency, deep learning math, and modern serving infrastructure. You are ready for top-tier AI engineering interviews.";
  } else if (overallScore >= 70) {
    readinessLevel = "Production AI Engineer";
    readinessSummary = "Strong proficiency in AI architectures and core ML pipelines. Focusing on your weakest tracks will push you into top percentile candidate readiness.";
  } else if (overallScore >= 50) {
    readinessLevel = "Applied AI Practitioner";
    readinessSummary = "Good working intuition with modern tools, but some first-principles mathematical and architectural nuances need strengthening.";
  } else if (overallScore >= 30) {
    readinessLevel = "Junior AI Engineer / Transitioning Developer";
    readinessSummary = "Solid general software engineering instinct, with targeted learning needed across RAG, Agents, and Deep Learning mechanics.";
  }

  return {
    overallScore,
    readinessLevel,
    readinessSummary,
    trackScores,
    strongestTracks,
    weakestTracks,
    recommendedItemSlugs,
  };
}
