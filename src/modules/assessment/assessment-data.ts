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
  sessionOrder?: number;
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

export const ALL_ASSESSMENT_QUESTIONS: AssessmentQuestion[] = [
  // ==========================================
  // 1. PYTHON CONCURRENCY & ARCHITECTURE
  // ==========================================
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
  {
    id: 17,
    trackKey: "python",
    trackTitle: "Python Concurrency",
    difficulty: "Medium",
    question: "When streaming 50GB of vector embeddings from disk, why is a generator function with 'yield' preferred over returning a populated Python list?",
    options: [
      { id: "A", text: "Generators compile into C machine code upon first invocation." },
      { id: "B", text: "Generators evaluate lazily, consuming O(1) memory by yielding one batch at a time instead of buffering the entire dataset in RAM." },
      { id: "C", text: "Generators automatically parallelize disk I/O across available GPU threads." },
      { id: "D", text: "Python lists cannot hold NumPy array references greater than 2GB." }
    ],
    correctOptionId: "B",
    explanation: "Generators produce items on demand (lazy evaluation), maintaining minimal working memory footprint regardless of dataset size, avoiding out-of-memory (OOM) crashes."
  },
  {
    id: 18,
    trackKey: "python",
    trackTitle: "Python Concurrency",
    difficulty: "Hard",
    question: "Why does the statement 'counter += 1' across multiple threads in Python still require a threading.Lock despite the existence of the GIL?",
    options: [
      { id: "A", text: "The GIL only protects dictionary reads, not integer mutations." },
      { id: "B", text: "'counter += 1' compiles into multiple bytecode instructions (LOAD, ADD, STORE); thread preemption between bytecode instructions causes race conditions." },
      { id: "C", text: "CPython disables the GIL whenever integer values exceed 256." },
      { id: "D", text: "Multithreading automatically promotes integers to atomic CPU registers." }
    ],
    correctOptionId: "B",
    explanation: "The GIL prevents concurrent C execution, but bytecode preemption can occur between LOAD_FAST, BINARY_ADD, and STORE_FAST instructions, leading to lost updates without an explicit Lock."
  },
  {
    id: 19,
    trackKey: "python",
    trackTitle: "Python Concurrency",
    difficulty: "Medium",
    question: "Why should a developer define '__slots__' on custom Node/Token classes when instantiating millions of objects in memory?",
    options: [
      { id: "A", text: "It prevents garbage collection from ever deleting the instances." },
      { id: "B", text: "It eliminates the internal '__dict__' per instance, saving significant memory and accelerating attribute access." },
      { id: "C", text: "It converts Python objects into PyTorch GPU tensors automatically." },
      { id: "D", text: "It enables multi-process IPC without pickle serialization." }
    ],
    correctOptionId: "B",
    explanation: "__slots__ reserves space for a fixed set of attributes, suppressing the creation of the dynamic __dict__ and __weakref__ for each instance, which can reduce memory consumption by 40-60%."
  },
  {
    id: 20,
    trackKey: "python",
    trackTitle: "Python Concurrency",
    difficulty: "Hard",
    question: "How does Python handle circular references between objects (e.g. Node A references Node B, which references Node A), and why might this cause memory leaks?",
    options: [
      { id: "A", text: "CPython immediately raises a RecursionError when a cycle is detected." },
      { id: "B", text: "Reference counting alone cannot free cycles; they rely on the periodic cyclic GC, and objects with custom '__del__' methods historically prevented cleanup." },
      { id: "C", text: "Circular references are automatically redirected to the weakref registry." },
      { id: "D", text: "The OS kernel automatically reclaims cyclic memory during context switches." }
    ],
    correctOptionId: "B",
    explanation: "Standard CPython deallocation relies on reference counts reaching 0. Cycles retain a ref count >= 1 and require the generational cyclic garbage collector to detect and collect them."
  },

  // ==========================================
  // 2. STATISTICS & MATH FOR ML
  // ==========================================
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
  {
    id: 21,
    trackKey: "statistics",
    trackTitle: "Mathematical Stats",
    difficulty: "Easy",
    question: "According to the Central Limit Theorem (CLT), what happens to the sampling distribution of the sample mean as sample size n becomes large?",
    options: [
      { id: "A", text: "It converges to a Uniform distribution across the sample range." },
      { id: "B", text: "It approximates a Normal distribution with variance σ²/n, regardless of the underlying population distribution." },
      { id: "C", text: "Its variance grows proportional to n." },
      { id: "D", text: "It strictly matches the skewness and kurtosis of the original population." }
    ],
    correctOptionId: "B",
    explanation: "The CLT establishes that the mean of independent, identically distributed random variables approaches a Gaussian distribution with variance σ²/n, enabling parametric hypothesis testing on non-normal populations."
  },
  {
    id: 22,
    trackKey: "statistics",
    trackTitle: "Mathematical Stats",
    difficulty: "Medium",
    question: "Why is the F1-score computed as the Harmonic Mean of Precision and Recall rather than their Arithmetic Mean?",
    options: [
      { id: "A", text: "Harmonic mean is computationally faster to calculate on GPUs." },
      { id: "B", text: "Harmonic mean penalizes extreme values; if either Precision or Recall approaches 0, F1 plummets toward 0." },
      { id: "C", text: "Arithmetic mean cannot handle floating point probabilities between 0 and 1." },
      { id: "D", text: "Harmonic mean scales linearly with total sample size." }
    ],
    correctOptionId: "B",
    explanation: "The arithmetic mean of 0.99 Precision and 0.01 Recall is 0.50, masking severe failure. The harmonic mean gives 2*(0.99*0.01)/(0.99+0.01) ≈ 0.0198, correctly identifying the model as dysfunctional."
  },
  {
    id: 23,
    trackKey: "statistics",
    trackTitle: "Mathematical Stats",
    difficulty: "Hard",
    question: "In Bayesian inference, what defines a 'Conjugate Prior' relative to a given likelihood function?",
    options: [
      { id: "A", text: "A prior that has zero covariance with the test dataset." },
      { id: "B", text: "A prior that yields a posterior distribution belonging to the exact same probability distribution family as the prior." },
      { id: "C", text: "A prior that forces the posterior mean to equal the sample median." },
      { id: "D", text: "A prior parameterized exclusively with non-informative uniform bounds." }
    ],
    correctOptionId: "B",
    explanation: "A conjugate prior (e.g. Beta prior for Binomial likelihood, or Dirichlet prior for Multinomial likelihood) ensures the posterior has a closed-form analytical distribution in the same family, avoiding expensive numerical integration."
  },
  {
    id: 24,
    trackKey: "statistics",
    trackTitle: "Mathematical Stats",
    difficulty: "Medium",
    question: "When evaluating semantic similarity scores between embedding pairs that have a non-linear but strictly monotonic relationship, which correlation metric is most appropriate?",
    options: [
      { id: "A", text: "Pearson correlation coefficient" },
      { id: "B", text: "Spearman rank correlation coefficient" },
      { id: "C", text: "Mean Squared Error" },
      { id: "D", text: "Gini impurity" }
    ],
    correctOptionId: "B",
    explanation: "Pearson assesses linear relationships, whereas Spearman evaluates monotonic relationships by assessing rank order, making it robust against non-linear scaling in similarity metrics."
  },

  // ==========================================
  // 3. CLASSICAL MACHINE LEARNING
  // ==========================================
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
  {
    id: 25,
    trackKey: "machine-learning",
    trackTitle: "Classical ML",
    difficulty: "Hard",
    question: "Geometric intuition: Why does L1 regularization (Lasso) drive coefficients to exactly zero, whereas L2 regularization (Ridge) only shrinks them toward zero?",
    options: [
      { id: "A", text: "L1 uses quadratic penalty contours that touch axes tangentially." },
      { id: "B", text: "The L1 constraint region is a diamond with sharp corners on the coordinate axes where loss contours frequently intersect first." },
      { id: "C", text: "L2 regularization sets the gradient to infinity at zero." },
      { id: "D", text: "L1 regularization modifies feature standard deviations directly." }
    ],
    correctOptionId: "B",
    explanation: "The L1 ball is a polyhedron with sharp corners (vertices) situated directly on axes where parameter values equal zero. Elliptical loss contours are statistically far more likely to intersect vertices first."
  },
  {
    id: 26,
    trackKey: "machine-learning",
    trackTitle: "Classical ML",
    difficulty: "Medium",
    question: "What is the core algorithmic difference between Random Forests and Gradient Boosted Decision Trees (GBDT)?",
    options: [
      { id: "A", text: "Random Forests train trees sequentially; GBDT trains trees independently in parallel." },
      { id: "B", text: "Random Forests use bagging to train independent deep trees; GBDT trains shallow trees sequentially to fit the pseudo-residuals of previous trees." },
      { id: "C", text: "GBDT only handles continuous features; Random Forests only handle categorical." },
      { id: "D", text: "Random Forests minimize cross-entropy; GBDT can only minimize mean absolute error." }
    ],
    correctOptionId: "B",
    explanation: "Random Forest builds independent, deep trees on bootstrap samples to reduce variance. GBDT builds shallow trees sequentially, each predicting the negative gradient (residual errors) of the ensemble, primarily reducing bias."
  },
  {
    id: 27,
    trackKey: "machine-learning",
    trackTitle: "Classical ML",
    difficulty: "Medium",
    question: "Why is standard K-Fold cross validation inappropriate for time-series forecasting models (e.g. predicting next-hour GPU demand)?",
    options: [
      { id: "A", text: "K-Fold cross validation requires categorical target variables." },
      { id: "B", text: "It shuffles data randomly, causing future data to leak into the training fold for past predictions (look-ahead bias)." },
      { id: "C", text: "It reduces training dataset size below minimum gradient descent bounds." },
      { id: "D", text: "Time series data cannot be evaluated with Mean Absolute Percentage Error." }
    ],
    correctOptionId: "B",
    explanation: "Time-series data has strict temporal dependencies. Random shuffling trains models on future data to predict past events, causing severe optimistic bias; TimeSeriesSplit (walk-forward validation) must be used."
  },
  {
    id: 28,
    trackKey: "machine-learning",
    trackTitle: "Classical ML",
    difficulty: "Hard",
    question: "When clustering high-dimensional vector embeddings (d = 1536) using K-Means with Euclidean distance, why do cluster boundaries frequently become uninformative?",
    options: [
      { id: "A", text: "Euclidean distance cannot be computed on vectors with more than 128 dimensions." },
      { id: "B", text: "Due to the Curse of Dimensionality, distances between all pairs of points concentrate around the mean, causing relative distance contrast to approach zero." },
      { id: "C", text: "K-Means centroids are mathematically constrained to 2D projections." },
      { id: "D", text: "High dimensional space forces all dot products to -1." }
    ],
    correctOptionId: "B",
    explanation: "In high dimensional spaces (Curse of Dimensionality), the ratio between the distance to the nearest neighbor and farthest neighbor approaches 1, diminishing the discriminative power of Euclidean metrics unless dimensionality reduction or cosine similarity is applied."
  },

  // ==========================================
  // 4. DEEP LEARNING ARCHITECTURES
  // ==========================================
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
  {
    id: 29,
    trackKey: "deep-learning",
    trackTitle: "Deep Learning",
    difficulty: "Medium",
    question: "Why do modern Transformers use Layer Normalization (LayerNorm / RMSNorm) rather than Batch Normalization (BatchNorm)?",
    options: [
      { id: "A", text: "BatchNorm requires fixed-size 2D images and cannot be calculated on matrices." },
      { id: "B", text: "LayerNorm normalizes across feature dimensions per token independently of batch size, supporting variable sequence lengths and batch size 1 inference." },
      { id: "C", text: "BatchNorm cannot be accelerated by modern CUDA tensor cores." },
      { id: "D", text: "LayerNorm forces all attention weights to be strictly positive." }
    ],
    correctOptionId: "B",
    explanation: "BatchNorm computes statistics across the mini-batch, making it brittle with variable sequence padding, distributed micro-batches, and single-sequence autoregressive serving. LayerNorm operates across channel/hidden dimensions for each sample independently."
  },
  {
    id: 30,
    trackKey: "deep-learning",
    trackTitle: "Deep Learning",
    difficulty: "Hard",
    question: "In the Adam optimizer, what is the specific role of the second moment vector v_t (exponential moving average of squared gradients)?",
    options: [
      { id: "A", text: "It maintains parameter momentum in the direction of the historical average gradient." },
      { id: "B", text: "It scales the learning rate inversely by √v_t, dampening updates for frequently updated parameters and boosting updates for sparse features." },
      { id: "C", text: "It guarantees that loss functions remain strictly convex." },
      { id: "D", text: "It automatically clips gradient norms above 1.0." }
    ],
    correctOptionId: "B",
    explanation: "Adam divides the first moment (momentum) by the square root of the second moment (RMS of past gradients). Parameters with large, erratic gradients receive smaller step sizes, while rarely updated weights receive larger relative updates."
  },
  {
    id: 31,
    trackKey: "deep-learning",
    trackTitle: "Deep Learning",
    difficulty: "Medium",
    question: "Why did modern LLM architectures replace the standard ReLU activation with SwiGLU / GELU?",
    options: [
      { id: "A", text: "ReLU requires double precision floating-point arithmetic." },
      { id: "B", text: "SwiGLU provides smooth non-zero gradients for negative inputs, preventing 'dying neurons' and improving gradient flow through deep networks." },
      { id: "C", text: "ReLU produces output values bounded between 0 and 1." },
      { id: "D", text: "SwiGLU eliminates the need for matrix multiplications in Feed-Forward layers." }
    ],
    correctOptionId: "B",
    explanation: "ReLU has zero derivative for all x < 0, which can permanently deactivate neurons if gradients knock weights negative. Smooth activations like GELU and SwiGLU maintain non-zero curvature and deliver superior empirical convergence."
  },
  {
    id: 32,
    trackKey: "deep-learning",
    trackTitle: "Deep Learning",
    difficulty: "Hard",
    question: "How does FlashAttention dramatically accelerate attention computation on GPUs without altering the mathematical output?",
    options: [
      { id: "A", text: "By quantizing the Q and K matrices into 4-bit integers." },
      { id: "B", text: "By tiling the inputs and computing Softmax incrementally in fast on-chip SRAM, avoiding high-latency reads/writes of the N×N attention matrix to High-Bandwidth Memory (HBM)." },
      { id: "C", text: "By approximating the attention matrix using low-rank singular value decomposition." },
      { id: "D", text: "By pruning tokens whose attention weight is below a threshold." }
    ],
    correctOptionId: "B",
    explanation: "Standard attention writes the massive N×N intermediate matrix to slow GPU HBM and reads it back for Softmax. FlashAttention tiles queries, keys, and values into fast SRAM, computing exact Softmax incrementally via online rescaling (IO-aware computation)."
  },

  // ==========================================
  // 5. LARGE LANGUAGE MODELS (LLMs)
  // ==========================================
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
  {
    id: 33,
    trackKey: "llm",
    trackTitle: "Large Language Models",
    difficulty: "Hard",
    question: "In Mixture of Experts (MoE) models (like Mixtral 8x7B), what mechanism ensures high capacity without increasing per-token inference compute proportionally?",
    options: [
      { id: "A", text: "Every expert evaluates every token, and outputs are averaged using a softmax gate." },
      { id: "B", text: "A sparse routing router network dynamically selects only Top-K experts (e.g. 2 of 8) per token, keeping active FLOPs low while total parameters remain large." },
      { id: "C", text: "Experts run sequentially as fallback layers if confidence is low." },
      { id: "D", text: "MoE layers replace attention mechanisms with convolutional filters." }
    ],
    correctOptionId: "B",
    explanation: "Sparse MoE routes each token to only top-k experts (e.g. 2 out of 8). A model with 47B total parameters executes only ~13B active FLOPs per forward pass, providing the quality of a giant model at the speed of a smaller one."
  },
  {
    id: 34,
    trackKey: "llm",
    trackTitle: "Large Language Models",
    difficulty: "Hard",
    question: "How does Speculative Decoding accelerate LLM generation speed by 2-3x without degrading sampling accuracy?",
    options: [
      { id: "A", text: "It skips 50% of the transformer layers during even-numbered token steps." },
      { id: "B", text: "A fast, small draft model speculatively generates K tokens, which are verified simultaneously in a single parallel forward pass of the large target model." },
      { id: "C", text: "It uses search engine autocomplete heuristics to predict upcoming words." },
      { id: "D", text: "It quantizes the vocabulary embedding matrix to 1-bit binary weights." }
    ],
    correctOptionId: "B",
    explanation: "Because verifying K tokens in parallel takes roughly the same GPU time as generating 1 token autoregressively (due to GPU compute vs memory bandwidth dynamics), speculative decoding accepts multiple valid draft tokens per iteration."
  },
  {
    id: 35,
    trackKey: "llm",
    trackTitle: "Large Language Models",
    difficulty: "Medium",
    question: "Why do modern LLM quantization schemes (like AWQ or GPTQ) preserve a small subset of salient weights in full 16-bit precision?",
    options: [
      { id: "A", text: "Certain weights act as cryptographic checksums for model weights." },
      { id: "B", text: "Feature activations exhibit massive outlier channels (up to 100x magnitude); quantizing them causes catastrophic perplexity degradation." },
      { id: "C", text: "PyTorch tensor operations crash if all layers are 4-bit." },
      { id: "D", text: "Salient weights correspond strictly to punctuation tokens." }
    ],
    correctOptionId: "B",
    explanation: "Research revealed that transformer activations develop persistent outlier dimensions with high magnitudes in specific channels. Activation-aware Weight Quantization (AWQ) protects top 1% salient weights to prevent perplexity collapse."
  },
  {
    id: 36,
    trackKey: "llm",
    trackTitle: "Large Language Models",
    difficulty: "Medium",
    question: "Why do modern models like LLaMA and Mistral use Rotary Position Embedding (RoPE) instead of absolute sinusoidal embeddings?",
    options: [
      { id: "A", text: "RoPE eliminates the Key and Value projections entirely." },
      { id: "B", text: "RoPE encodes relative token distance via complex rotational geometry in 2D subspaces, naturally decaying attention for distant tokens and facilitating context length extension." },
      { id: "C", text: "RoPE enforces that sequence generation must be strictly palindrome-invariant." },
      { id: "D", text: "RoPE stores positions in GPU registers rather than model weights." }
    ],
    correctOptionId: "B",
    explanation: "RoPE rotates query and key vectors by an angle proportional to their sequence index. The inner product <R_m q, R_n k> depends purely on relative offset (m - n), enabling superior context generalization."
  },

  // ==========================================
  // 6. RETRIEVAL-AUGMENTED GENERATION (RAG)
  // ==========================================
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
  {
    id: 37,
    trackKey: "rag",
    trackTitle: "RAG Engineering",
    difficulty: "Medium",
    question: "Why is a two-stage retrieval pipeline (Bi-Encoder first stage + Cross-Encoder reranker second stage) standard in high-precision RAG?",
    options: [
      { id: "A", text: "Cross-encoders cannot output numerical similarity scores." },
      { id: "B", text: "Bi-encoders index millions of docs offline for fast O(log N) MIPS vector search; Cross-encoders perform joint full cross-attention over Query + Doc pairs, which is highly accurate but too slow for full-database sweeps." },
      { id: "C", text: "Bi-encoders only operate on tabular SQL data." },
      { id: "D", text: "Cross-encoders replace the vector database altogether." }
    ],
    correctOptionId: "B",
    explanation: "Bi-encoders map queries and docs into separate vectors, allowing rapid ANN search across millions of items. Cross-encoders feed query and document together through all attention layers, capturing intricate semantic alignment for the top 20-50 candidates."
  },
  {
    id: 38,
    trackKey: "rag",
    trackTitle: "RAG Engineering",
    difficulty: "Easy",
    question: "When chunking markdown technical manuals for RAG, why should chunk overlap (e.g. 10-20% token overlap) be configured?",
    options: [
      { id: "A", text: "To compress the vector database index size by 50%." },
      { id: "B", text: "To prevent vital semantic context or sentences from being severed midway at rigid chunk boundaries." },
      { id: "C", text: "To enforce that chunks are encrypted in transit." },
      { id: "D", text: "To guarantee that every document has an even number of tokens." }
    ],
    correctOptionId: "B",
    explanation: "Without overlap, sentences or code snippets split across adjacent chunk boundaries lose their relational context, degrading retrieval relevance and generating incomplete answers."
  },
  {
    id: 39,
    trackKey: "rag",
    trackTitle: "RAG Engineering",
    difficulty: "Hard",
    question: "How does Hierarchical Navigable Small World (HNSW) achieve sub-millisecond Approximate Nearest Neighbor (ANN) search over millions of vectors?",
    options: [
      { id: "A", text: "It stores vectors as raw strings in an inverted index." },
      { id: "B", text: "It builds a multi-layer graph where top layers have long-range skip connections (fast routing) and bottom layers have dense local clustering, achieving logarithmic search complexity." },
      { id: "C", text: "It computes exact cosine similarities across all rows using brute-force matrix multiplication." },
      { id: "D", text: "It replaces vector embeddings with MD5 hashes." }
    ],
    correctOptionId: "B",
    explanation: "HNSW is inspired by skip-lists. Top layers skip across vast regions of the vector space to quickly locate the neighborhood of the query, while lower layers greedily refine search among local nearest neighbors in O(log N) time."
  },
  {
    id: 40,
    trackKey: "rag",
    trackTitle: "RAG Engineering",
    difficulty: "Medium",
    question: "How does Hypothetical Document Embeddings (HyDE) improve RAG retrieval for vague or terse user queries?",
    options: [
      { id: "A", text: "It automatically translates the query into binary SQL statements." },
      { id: "B", text: "An LLM generates a hypothetical answer to the query first; this synthetic answer is embedded and used to retrieve actual relevant documents in vector space." },
      { id: "C", text: "It deletes stop words from the query before BM25 scoring." },
      { id: "D", text: "It runs k-means clustering directly on the raw prompt tokens." }
    ],
    correctOptionId: "B",
    explanation: "User queries are often short (e.g. 'refund policy delay'). HyDE instructs an LLM to hallucinate a plausible answer passage. Even if factually inaccurate, its vector embedding is semantically and stylistically closer to real document chunks than the terse query."
  },

  // ==========================================
  // 7. AI AGENTS & TOOL CALLING
  // ==========================================
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
  {
    id: 41,
    trackKey: "agents",
    trackTitle: "AI Agent Systems",
    difficulty: "Medium",
    question: "How do structured Tool Calling schemas (JSON Schema / Pydantic) prevent agents from hallucinating invalid function arguments?",
    options: [
      { id: "A", text: "They compile Python code to WebAssembly sandbox runtimes." },
      { id: "B", text: "They constrain grammar and token decoding probabilities during sampling to only produce tokens conforming to the declared JSON schema properties." },
      { id: "C", text: "They run regex assertions after every token emission and restart generation on failure." },
      { id: "D", text: "They convert all tool arguments to base64 strings." }
    ],
    correctOptionId: "B",
    explanation: "Structured generation frameworks (like outlines or instructor) mask the LLM's next-token logit distribution with finite-state machine (FSM) grammar rules, guaranteeing 100% syntactically valid JSON output conforming to the schema."
  },
  {
    id: 42,
    trackKey: "agents",
    trackTitle: "AI Agent Systems",
    difficulty: "Hard",
    question: "Why are cyclical stateful graphs (e.g. LangGraph) preferred over simple linear chains (DAGs) for complex production agent workflows?",
    options: [
      { id: "A", text: "Cyclical graphs run exclusively on CPU without requiring an LLM." },
      { id: "B", text: "Real-world tasks require conditional loops, human-in-the-loop review interruptions, persistence checkpoints, and recovery cycles that DAGs cannot express." },
      { id: "C", text: "Linear chains consume 10x more token memory than cyclical graphs." },
      { id: "D", text: "Cyclical graphs execute all sub-tasks in a single forward pass." }
    ],
    correctOptionId: "B",
    explanation: "Production agents must loop back (e.g. Code Generator -> Unit Test Evaluator -> Code Corrector loop) and support pause/resume state checkpointing for human approval, making cyclic state graphs essential."
  },
  {
    id: 43,
    trackKey: "agents",
    trackTitle: "AI Agent Systems",
    difficulty: "Medium",
    question: "What is the crucial architectural distinction between an agent's Short-Term Memory and Long-Term Memory?",
    options: [
      { id: "A", text: "Short-term memory uses SQLite; Long-term memory uses browser local storage." },
      { id: "B", text: "Short-term memory resides in the active prompt context window; Long-term memory is persisted in vector/document stores and retrieved on demand across sessions." },
      { id: "C", text: "Short-term memory stores floats; Long-term memory stores strings." },
      { id: "D", text: "Long-term memory is hard-coded into the model's neural network weights." }
    ],
    correctOptionId: "B",
    explanation: "Short-term working memory consists of the ongoing conversational context within the model's finite window. Long-term memory persists episodic experiences, user preferences, and knowledge externally in vector/graph databases."
  },
  {
    id: 44,
    trackKey: "agents",
    trackTitle: "AI Agent Systems",
    difficulty: "Hard",
    question: "In a Supervisor Multi-Agent architecture, what is the role of the orchestrator/supervisor LLM?",
    options: [
      { id: "A", text: "To fine-tune worker models on user chat sessions in real time." },
      { id: "B", text: "To act as a central router that analyzes task state, delegates sub-goals to specialized worker agents, and aggregates their outputs into a final synthesized response." },
      { id: "C", text: "To act as a database cache for raw vector embeddings." },
      { id: "D", text: "To terminate worker threads if token count exceeds 100." }
    ],
    correctOptionId: "B",
    explanation: "The supervisor agent breaks complex multi-step user prompts into discrete domain problems, routes them to specialized agents (e.g. Researcher, Coder, Reviewer), and synthesizes the outputs."
  },

  // ==========================================
  // 8. AI SYSTEM DESIGN & SERVING
  // ==========================================
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
  },
  {
    id: 45,
    trackKey: "system-design",
    trackTitle: "AI System Design",
    difficulty: "Hard",
    question: "Why is Continuous Batching (iteration-level scheduling) far superior to static request batching for LLM serving engines?",
    options: [
      { id: "A", text: "It forces all requests to generate exactly 128 tokens." },
      { id: "B", text: "Static batching waits for the slowest request in a batch to finish, idling GPU cores; continuous batching evicts completed requests and injects new ones after every single token iteration." },
      { id: "C", text: "Continuous batching eliminates KV cache computation entirely." },
      { id: "D", text: "It runs inference on CPU threads while GPU is busy with rendering." }
    ],
    correctOptionId: "B",
    explanation: "In static batching, if one request generates 500 tokens and another generates 5 tokens, the batch slot is wasted for 495 steps. Continuous batching operates at iteration granularity, yielding 10x-20x higher GPU saturation."
  },
  {
    id: 46,
    trackKey: "system-design",
    trackTitle: "AI System Design",
    difficulty: "Hard",
    question: "What is the primary architectural difference between Tensor Parallelism (TP) and Pipeline Parallelism (PP) when deploying 70B+ parameter models across multiple GPUs?",
    options: [
      { id: "A", text: "TP splits model layers sequentially across nodes; PP splits individual weight matrices inside each layer." },
      { id: "B", text: "TP shards individual matrix multiplications (intra-layer) across GPUs requiring ultra-high NVLink bandwidth; PP splits sequential layers across GPUs (inter-layer), tolerating lower network speeds." },
      { id: "C", text: "TP is used for audio models; PP is used for text models." },
      { id: "D", text: "TP duplicates the entire model on every GPU." }
    ],
    correctOptionId: "B",
    explanation: "Tensor Parallelism splits weight matrices within each attention/FFN layer, requiring all-reduce synchronization on every layer (demanding 900GB/s NVLink inside an 8-GPU box). Pipeline Parallelism splits layers across servers with pipeline bubble management."
  },
  {
    id: 47,
    trackKey: "system-design",
    trackTitle: "AI System Design",
    difficulty: "Medium",
    question: "How does Semantic Caching work in an enterprise LLM API gateway?",
    options: [
      { id: "A", text: "It matches exact SHA-256 hashes of HTTP request bodies." },
      { id: "B", text: "It embeds incoming user queries into vectors and checks for nearest neighbors in a fast cache above a similarity threshold (e.g. cosine > 0.96) to return cached responses." },
      { id: "C", text: "It caches user passwords in Redis." },
      { id: "D", text: "It stores prompt responses directly in browser cookies." }
    ],
    correctOptionId: "B",
    explanation: "Exact string matching misses paraphrased questions ('How to reset password?' vs 'Password reset steps'). Semantic caching computes query embeddings and retrieves stored responses when cosine similarity exceeds a high confidence threshold, slashing API cost and latency."
  },
  {
    id: 48,
    trackKey: "system-design",
    trackTitle: "AI System Design",
    difficulty: "Medium",
    question: "When profiling LLM inference latency, what is the technical distinction between TTFT (Time to First Token) and TPOT (Time Per Output Token)?",
    options: [
      { id: "A", text: "TTFT measures network DNS lookup; TPOT measures server TLS handshake." },
      { id: "B", text: "TTFT is dominated by the compute-bound prefill phase processing the prompt in parallel; TPOT is dominated by memory-bandwidth-bound autoregressive decoding generating one token at a time." },
      { id: "C", text: "TTFT applies only to streaming responses; TPOT applies only to batch jobs." },
      { id: "D", text: "TTFT is measured in seconds; TPOT is measured in hours." }
    ],
    correctOptionId: "B",
    explanation: "The prompt prefill phase processes all input tokens concurrently (high compute intensity, GPU compute-bound). The decode phase reads all model weights from HBM to SRAM for every single token produced (memory-bandwidth-bound)."
  }
];

// Backwards compatibility alias
export const ASSESSMENT_QUESTIONS: AssessmentQuestion[] = ALL_ASSESSMENT_QUESTIONS;

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

/**
 * Dynamically samples a randomized test session across all 8 tracks.
 * By default selects 2 questions per track (16 questions total), randomized on every retake.
 */
export function generateAssessmentSession(questionsPerTrack: number = 2): AssessmentQuestion[] {
  const selected: AssessmentQuestion[] = [];
  const trackKeys: AssessmentQuestion["trackKey"][] = [
    "python",
    "statistics",
    "machine-learning",
    "deep-learning",
    "llm",
    "rag",
    "agents",
    "system-design",
  ];

  trackKeys.forEach((key) => {
    const trackPool = ALL_ASSESSMENT_QUESTIONS.filter((q) => q.trackKey === key);
    // Shuffle the track pool
    const shuffled = [...trackPool].sort(() => Math.random() - 0.5);
    selected.push(...shuffled.slice(0, questionsPerTrack));
  });

  // Interleave/shuffle the questions so tracks don't always appear in predictable order
  const shuffledSession = [...selected].sort(() => Math.random() - 0.5);

  return shuffledSession.map((q, idx) => ({
    ...q,
    sessionOrder: idx + 1,
  }));
}

export function computeAssessmentResult(
  answers: { [questionId: number]: string },
  sessionQuestions: AssessmentQuestion[] = ALL_ASSESSMENT_QUESTIONS.slice(0, 16)
): AssessmentResult {
  const trackStats: { [trackKey: string]: { correct: number; total: number; title: string; color: string } } = {};

  Object.entries(TRACK_CONFIGS).forEach(([key, conf]) => {
    trackStats[key] = { correct: 0, total: 0, title: conf.title, color: conf.color };
  });

  let totalCorrect = 0;

  sessionQuestions.forEach((q) => {
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

  const overallScore = sessionQuestions.length > 0 
    ? Math.round((totalCorrect / sessionQuestions.length) * 100) 
    : 0;

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
