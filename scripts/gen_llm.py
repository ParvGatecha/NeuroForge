def get_questions():
    questions = []
    
    # Q61: Tokenization
    questions.append({
        "id": 61,
        "slug": "tokenization",
        "title": "Build a Byte Pair Encoding (BPE) Tokenizer",
        "section": "LLM",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 15,
        "tags": ["tokenization", "nlp", "bpe"],
        "learning_objectives": [
            "Explain the BPE tokenization merge algorithm",
            "Calculate character pair frequencies in text strings"
        ],
        "problem_statement": "Build a BPE tokenizer helper by implementing two python functions: `get_stats(vocab)` that counts the frequency of all adjacent character pairs in a BPE vocabulary, and `merge_vocab(pair, vocab)` that merges a selected pair into a single token across the vocabulary.",
        "real_world_context": "BPE is used by GPT models (via tiktoken) and Llama models. Selecting the correct vocabulary size balances model embedding parameters against sequence token length efficiency.",
        "hints": [
            "Represent vocabulary words as lists of individual characters or sub-tokens, ending with a space marker.",
            "Iterate over adjacent pairs in each word, multiplying the pair count by the word's frequency.",
            "Replace occurrences of `pair[0], pair[1]` in the word list with the unified string `pair[0] + pair[1]`."
        ],
        "solution": {
            "explanation": "BPE (Byte Pair Encoding) is a subword tokenization algorithm. It begins by splitting text into characters. It then iteratively finds the most frequent adjacent pair of tokens in the vocabulary and merges them into a new token. This process repeats until the target vocabulary size is reached. This enables the tokenizer to represent common words as single tokens, while fallback options exist for rare words.",
            "key_takeaways": [
                "BPE builds subword vocabularies by iteratively merging frequent adjacent pairs.",
                "Subword tokenization resolves the out-of-vocabulary issue while preserving semantic roots."
            ]
        },
        "starter_code": {
            "python": "import re\nfrom collections import defaultdict\n\ndef get_stats(vocab):\n    # vocab: dict {word_string: count}\n    # TODO: Count consecutive token pairs and return them\n    pass\n\ndef merge_vocab(pair, v_in):\n    # TODO: Merge pair 'ab' into 'ab' inside the vocabulary structure\n    pass"
        },
        "expected_output": "Updated vocabulary dict with merged tokens and pair count stats.",
        "follow_up_questions": [
            "Why is Tiktoken faster than HuggingFace's tokenizers for GPT models?",
            "How do tokenizers handle special characters and numbers in the BPE vocabulary?"
        ],
        "references": [
            {
                "title": "Neural Machine Translation of Rare Words with Subword Units",
                "url": "https://arxiv.org/abs/1508.07909"
            }
        ]
    })
    
    # Q62: Greedy vs Beam Search
    questions.append({
        "id": 62,
        "slug": "greedy-vs-beam-search",
        "title": "Build a Nucleus (Top-p) Logit Sampler",
        "section": "LLM",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 10,
        "tags": ["decoding", "generation", "sampling"],
        "learning_objectives": [
            "Contrast greedy search decoding with beam search decoding",
            "Adjust sampling parameters (temperature, top-k, top-p) to regulate text diversity"
        ],
        "problem_statement": "Build a python function `sample_logits(logits, temperature, top_p)` that applies temperature scaling to raw output logits and filters out low probability options using top-p (nucleus) thresholding before softmax.",
        "real_world_context": "Configuring generation parameters is essential for application deployment: code generation demands high precision (low temperature), while creative copywriting requires high variety (higher temperature and top-p).",
        "hints": [
            "Temperature scaling: divide logits by temperature before softmax.",
            "Top-p (nucleus) sampling: sort logits descending, compute cumulative probabilities of sorted values, and discard logits that fall outside the top cumulative threshold `p`."
        ],
        "solution": {
            "explanation": "Greedy search selects the single most probable token at each step, which can lead to repetitive text or suboptimal local minima. Beam search keeps a tracking window of `B` candidate paths, selecting the path with the highest cumulative log probability at the end, yielding more coherent text. Temperature scales the distribution: dividing by `T < 1` sharpens probabilities (making output more deterministic), while `T > 1` flattens them. Top-p restricts selections to a dynamic subset of tokens that make up the top `p` cumulative probability, preserving vocabulary options while eliminating low-probability nonsense.",
            "key_takeaways": [
                "Greedy search is fast but shortsighted; beam search evaluates multiple future generation paths.",
                "Top-p (nucleus) sampling clips the tail of the distribution dynamically, adapting to model confidence."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef sample_logits(logits, temperature=1.0, top_p=0.9):\n    # TODO: Apply temperature, sort, calculate cumulative probs, filter by top_p, and return probabilities\n    pass"
        },
        "expected_output": "Numpy array of probability scores summing to 1.0.",
        "follow_up_questions": [
            "Why is beam search rarely used for chat generation in modern LLMs?",
            "What is the mathematical definition of top-k sampling?"
        ],
        "references": [
            {
                "title": "Hugging Face Decoding Strategies Guide",
                "url": "https://huggingface.co/blog/how-to-generate"
            }
        ]
    })

    # Q63: Prompt Engineering
    questions.append({
        "id": 63,
        "slug": "prompt-engineering",
        "title": "Build a Chain-of-Thought Prompt Builder",
        "section": "LLM",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 10,
        "tags": ["prompting", "in-context-learning", "chain-of-thought"],
        "learning_objectives": [
            "Structure effective few-shot context templates",
            "Incorporate Chain-of-Thought (CoT) instructions to improve reasoning accuracy"
        ],
        "problem_statement": "Build a Python utility class `PromptBuilder` that dynamically formats a user query with (1) role descriptions, (2) three matching exemplars (few-shot), and (3) a Chain-of-Thought 'Let's think step by step' reasoning prefix.",
        "real_world_context": "Before fine-tuning models, robust prompt engineering is the fastest way to validate LLM features in production, resolving logic bugs in mathematical and reasoning workflows.",
        "hints": [
            "Format the prompt with clear delimitators like `### Instruction`, `### Examples`, and `### Query`.",
            "Incorporate input-output pairs in the examples to show the desired formatting.",
            "Appending 'Let's think step-by-step' forces the model to generate intermediate steps, preventing it from predicting the final answer immediately based on simple word correlations."
        ],
        "solution": {
            "explanation": "Few-shot prompting provides the LLM with example patterns in the prompt, allowing it to adapt to output formats without updating weights (in-context learning). Chain-of-Thought (CoT) prompting instructs the model to generate intermediate reasoning steps. This works because Transformers compute representations sequentially; by outputting reasoning tokens first, the model allocates compute steps to process the logical path before outputting the final answer, improving accuracy on complex reasoning tasks.",
            "key_takeaways": [
                "Few-shot prompting guides formatting and style without weight updates.",
                "Chain-of-Thought utilizes output token generation to allocate computational steps for logical reasoning."
            ]
        },
        "starter_code": {
            "python": "class PromptBuilder:\n    def __init__(self, system_instruction):\n        self.system = system_instruction\n        self.examples = []\n        \n    def add_example(self, user_in, assistant_out):\n        self.examples.append((user_in, assistant_out))\n        \n    def build_prompt(self, user_query):\n        # TODO: Format system instruction, examples, and user query with CoT suffix\n        pass"
        },
        "expected_output": "A formatted prompt string ready for API submission.",
        "follow_up_questions": [
            "How does zero-shot Chain-of-Thought differ from few-shot Chain-of-Thought?",
            "What is Self-Consistency in the context of prompt engineering?"
        ],
        "references": [
            {
                "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
                "url": "https://arxiv.org/abs/2201.11903"
            }
        ]
    })

    # Q64: Embedding Models
    questions.append({
        "id": 64,
        "slug": "embedding-models",
        "title": "Build a Cosine Similarity Calculator",
        "section": "LLM",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 10,
        "tags": ["embeddings", "vector-search", "similarity"],
        "learning_objectives": [
            "Explain how semantic embedding models represent text strings in multi-dimensional spaces",
            "Calculate cosine similarity between query and document vectors"
        ],
        "problem_statement": "Build a python function `cosine_similarity(vec1, vec2)` that calculates the cosine similarity between two 1D arrays, and explain how it simplifies mathematically when vectors are L2 unit-normalized.",
        "real_world_context": "Semantic embeddings are the core technology behind vector search, question answering search engines, and RAG architectures.",
        "hints": [
            "Cosine similarity formula: `dot(A, B) / (||A|| * ||B||)`.",
            "L2 norm of a vector A is `sqrt(sum(Ai^2))`.",
            "If both vectors are L2-normalized, the denominator is 1.0, so cosine similarity simplifies to the dot product: `dot(A, B)`."
        ],
        "solution": {
            "explanation": "Embedding models map raw text to fixed-size vectors in a high-dimensional space where semantic similarity corresponds to geometric proximity. Cosine similarity measures the cosine of the angle between two vectors, ignoring their magnitudes. When embedding vectors are unit-normalized (L2 norm = 1.0), the formula simplifies to a simple dot product, which is computationally faster to calculate on large databases.",
            "key_takeaways": [
                "Embedding models capture semantic relationships as geometric proximity.",
                "For L2-normalized embeddings, cosine similarity is equivalent to the dot product."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef cosine_similarity(v1, v2):\n    # v1, v2: 1D numpy arrays\n    # TODO: Calculate cosine similarity\n    pass"
        },
        "expected_output": "A float value between -1.0 and 1.0.",
        "follow_up_questions": [
            "What is the difference between Euclidean distance and cosine similarity, and when is each preferred?",
            "How do bi-encoders and cross-encoders differ in computing text similarity?"
        ],
        "references": [
            {
                "title": "Text Embeddings and Cosine Similarity (OpenAI)",
                "url": "https://platform.openai.com/docs/guides/embeddings"
            }
        ]
    })

    # Q65: Context Window Limits
    questions.append({
        "id": 65,
        "slug": "context-window-limits",
        "title": "Build a Transformer Attention Memory Estimator",
        "section": "LLM",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 10,
        "tags": ["attention-complexity", "context-window", "kv-cache"],
        "learning_objectives": [
            "Explain the quadratic scaling complexity of self-attention",
            "Identify the memory bottleneck of context size in LLMs"
        ],
        "problem_statement": "Build a python function `calculate_attention_matrix_size(seq_len, num_heads, precision_bytes)` that calculates the size of the attention matrix (in megabytes) for a given sequence length, explaining the quadratic O(L^2) memory bottleneck.",
        "real_world_context": "The quadratic scaling of attention is why early LLMs were limited to 2,048 tokens. Extending context windows requires optimization techniques like FlashAttention, sparse attention, or RoPE scaling.",
        "hints": [
            "Self-attention calculates a weight matrix between every token and every other token, which is of size `L x L`.",
            "An `L x L` matrix of floats (4 bytes each) requires `L * L * 4` bytes of memory.",
            "Recall that the dot product `Q @ K.T` multiplies a matrix of shape `(seq_len, d_k)` by `(d_k, seq_len)`, yielding a `(seq_len, seq_len)` attention score matrix."
        ],
        "solution": {
            "explanation": "Self-attention computes dot products between all pairs of tokens in a sequence, creating an `L x L` attention score matrix. For a sequence length of 8,192, the matrix contains `8,192 * 8,192 = 67,108,864` elements. At 4 bytes per float, this single matrix requires `268.4 MB` per attention head. Multiplied across many layers and attention heads, memory usage scales quadratically, creating a massive bottleneck on GPUs.",
            "key_takeaways": [
                "Attention score matrices scale as O(L^2) with sequence length.",
                "This quadratic footprint bounds context sizes due to GPU memory capacity limits."
            ]
        },
        "starter_code": {
            "python": "def calculate_attention_matrix_size(seq_len, num_heads, precision_bytes=4):\n    # TODO: Calculate total bytes and return size in MB\n    bytes_size = 0\n    return bytes_size / (1024 * 1024)"
        },
        "expected_output": "The memory size of the attention matrices in megabytes.",
        "follow_up_questions": [
            "How does Linear Attention attempt to bypass the quadratic bottleneck?",
            "What is the KV cache, and how does it save compute time during autoregressive generation?"
        ],
        "references": [
            {
                "title": "Transformer Attention Complexity Analysis",
                "url": "https://arxiv.org/abs/1706.03762"
            }
        ]
    })

    # Q66: Instruction Tuning
    questions.append({
        "id": 66,
        "slug": "instruction-tuning",
        "title": "Build an SFT Loss Target Masker",
        "section": "LLM",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 15,
        "tags": ["fine-tuning", "sft", "loss-masking"],
        "learning_objectives": [
            "Explain Supervised Fine-Tuning (SFT) data preparation",
            "Implement target loss masking to train models ONLY on assistant responses"
        ],
        "problem_statement": "Build a python function `mask_prompt_loss(target_token_ids, prompt_len, ignore_index)` that prepares token labels for training by setting target prompt token IDs to a special ignore index (e.g. `-100`), ensuring the model's cross-entropy loss is calculated only on assistant response tokens.",
        "real_world_context": "SFT converts a base pre-trained model into a helpful conversational assistant. Correctly masking prompt tokens ensures the model is penalized only for generating bad assistant responses, not for prompt variations.",
        "hints": [
            "We want the model to learn to generate the answer, not the prompt. Calculating loss on prompt tokens wastes gradient updates on memorizing prompts.",
            "PyTorch's `nn.CrossEntropyLoss(ignore_index=-100)` ignores target indices equal to `-100`.",
            "Replace target indices from `0` to `prompt_len - 1` with `-100`."
        ],
        "solution": {
            "explanation": "During Supervised Fine-Tuning (SFT), the model is fed the concatenated prompt and response. If we compute the loss on the prompt tokens, the model updates its weights to predict the prompt text. This is counterproductive since prompts are user-provided. By setting the target labels of prompt tokens to `-100` (the default ignore index in PyTorch), we restrict gradient updates to the assistant response tokens, optimizing training efficiency and answer quality.",
            "key_takeaways": [
                "Loss masking focuses training on predicting the response rather than memorizing the prompt.",
                "ignore_index=-100 in PyTorch excludes specific tokens from Cross-Entropy loss calculations."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef mask_prompt_loss(target_token_ids, prompt_len, ignore_index=-100):\n    # target_token_ids: numpy array of token IDs representing the full sequence\n    # TODO: Replace the prompt portion of the target array with ignore_index\n    pass"
        },
        "expected_output": "The modified target array with the first prompt_len elements set to -100.",
        "follow_up_questions": [
            "What is the ChatML format, and why is it useful for training conversational LLMs?",
            "What is the difference between instruction tuning and alignment?"
        ],
        "references": [
            {
                "title": "LIMA: Less Is More for Alignment",
                "url": "https://arxiv.org/abs/2305.11206"
            }
        ]
    })

    # Q67: Parameter-Efficient Fine-Tuning (LoRA)
    questions.append({
        "id": 67,
        "slug": "parameter-efficient-fine-tuning",
        "title": "Build a LoRA Linear Layer Adapter",
        "section": "LLM",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 20,
        "tags": ["peft", "lora", "math"],
        "learning_objectives": [
            "Explain the low-rank adaptation matrix decomposition",
            "Implement a forward pass of a LoRA linear layer"
        ],
        "problem_statement": "Build a python class `LoraLinear(base_weight, r, alpha)` that implements a LoRA forward pass: `h = X @ W_base.T + (X @ A.T @ B.T) * (alpha / r)`. `W_base` of shape (d x k) is frozen, while `A` (r x k) and `B` (d x r) are low-rank update adapter matrices.",
        "real_world_context": "LoRA allows fine-tuning a 70B parameter model on a single consumer GPU by reducing trainable parameters by 99%, saving millions in infrastructure costs.",
        "hints": [
            "Initialize matrix `A` using a normal distribution (mean 0) and matrix `B` with zeros, ensuring the adapter outputs zero at the start of training.",
            "The scaling factor `alpha / r` regulates the influence of the adapter weights.",
            "During forward pass, make sure the base weight is not updated by gradients (freeze base weights)."
        ],
        "solution": {
            "explanation": "LoRA hypothesizes that weight updates during adaptation have a low 'intrinsic rank'. Instead of updating the full weight matrix `W` (d x k), LoRA factorizes the update into two low-rank matrices `B` (d x r) and `A` (r x k), where rank `r << min(d, k)`. The total output is the sum of the frozen base layer output and the adapter output scaled by `alpha / r`. Initializing `B` to zero ensures the adapter has no effect at the start of training, behaving exactly like the base model.",
            "key_takeaways": [
                "LoRA reduces trainable parameters by decomposing updates into low-rank matrices A and B.",
                "Scaling factor alpha/r ensures training stability across different values of rank r."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\nclass LoraLinear:\n    def __init__(self, W_base, r=8, alpha=16):\n        self.W_base = W_base # Frozen base weight, shape (d, k)\n        self.r = r\n        self.alpha = alpha\n        # TODO: Initialize trainable adapter matrices A and B\n        # A shape (r, k), B shape (d, r)\n        self.A = None\n        self.B = None\n        \n    def forward(self, X):\n        # X shape (batch_size, k)\n        # TODO: Compute forward pass\n        pass"
        },
        "expected_output": "The forward pass activations array of shape (batch_size, d).",
        "follow_up_questions": [
            "Why is matrix B initialized to zero while matrix A is initialized with random values?",
            "How does QLoRA (Quantized LoRA) achieve even greater memory savings during training?"
        ],
        "references": [
            {
                "title": "LoRA: Low-Rank Adaptation of Large Language Models",
                "url": "https://arxiv.org/abs/2106.09685"
            }
        ]
    })

    # Q68: RLHF: PPO vs DPO
    questions.append({
        "id": 68,
        "slug": "rlhf-ppo-dpo",
        "title": "Build a DPO Loss Objective Function",
        "section": "LLM",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 20,
        "tags": ["rlhf", "dpo", "alignment"],
        "learning_objectives": [
            "Explain the limitation of PPO reinforcement learning in LLM alignment",
            "Implement the mathematical loss function of Direct Preference Optimization"
        ],
        "problem_statement": "Build a python function `dpo_loss(policy_chosen_logps, policy_rejected_logps, ref_chosen_logps, ref_rejected_logps, beta)` that calculates Direct Preference Optimization (DPO) loss for preference pairs relative to a frozen reference model.",
        "real_world_context": "DPO has largely replaced PPO for aligning models to human preferences because it is a stable, single-stage supervised optimization that avoids training an independent reward model.",
        "hints": [
            "DPO loss formula: `-E[ log sigmoid( beta * (log(pi_theta(y_w|x)/pi_ref(y_w|x)) - log(pi_theta(y_l|x)/pi_ref(y_l|x))) ) ]`.",
            "Use `np.log(sigmoid_input)` or build a stable log-sigmoid implementation: `log(1 / (1 + exp(-x))) = -log1p(exp(-x))`."
        ],
        "solution": {
            "explanation": "Standard PPO-based RLHF is complex because it requires training four models concurrently: the active policy, a value network, a reward model, and a reference model to prevent policy drift. DPO bypasses this by showing mathematically that the reward model can be expressed directly in terms of the policy likelihood ratio. This reformulates alignment as a simple binary cross-entropy loss over preference pairs, trained directly on the policy model without needing reinforcement learning.",
            "key_takeaways": [
                "DPO aligns models directly on preference pairs without needing an auxiliary reward model.",
                "The reference model prevents the policy from drifting too far from the base model's distribution."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef dpo_loss(policy_chosen_logps, policy_rejected_logps, ref_chosen_logps, ref_rejected_logps, beta=0.1):\n    # logps: numpy arrays of log probabilities\n    # TODO: Implement DPO loss calculation\n    pass"
        },
        "expected_output": "Float DPO loss value.",
        "follow_up_questions": [
            "What role does the hyperparameter beta play in the DPO loss function?",
            "What is the Bradley-Terry preference model, and how does DPO relate to it?"
        ],
        "references": [
            {
                "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
                "url": "https://arxiv.org/abs/2305.18290"
            }
        ]
    })

    # Q69: Model Quantization
    questions.append({
        "id": 69,
        "slug": "model-quantization",
        "title": "Build Symmetric and Asymmetric Quantizers",
        "section": "LLM",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 20,
        "tags": ["quantization", "model-compression", "edge-deployment"],
        "learning_objectives": [
            "Implement symmetric and asymmetric INT8 quantization",
            "Calculate scale factors and zero points for float weight tensors"
        ],
        "problem_statement": "Build two python functions: `quantize_symmetric(w)` and `quantize_asymmetric(w)` that compute scale factors and zero points to map a float weight matrix `w` into signed INT8 values and back, comparing their reconstruction errors.",
        "real_world_context": "Quantizing a 70B parameter model from FP16 (140GB) to INT4 (35GB) allows it to run on a single workstation with commercial GPUs, reducing hosting costs by 75%.",
        "hints": [
            "For symmetric quantization: `scale = max(abs(w)) / 127`. Quantize: `q = round(w / scale)`. Dequantize: `w_approx = q * scale`.",
            "For asymmetric quantization: `scale = (max(w) - min(w)) / 255`, `zero_point = round(-min(w) / scale) - 128`. Clip values to the [-128, 127] range for signed INT8.",
            "Compute reconstruction error as mean squared error between `w` and `w_approx`."
        ],
        "solution": {
            "explanation": "Quantization maps continuous floats to discrete integers. Symmetric quantization maps the range `[-max_val, max_val]` to `[-127, 127]`, aligning zero points to 0. Asymmetric quantization maps the exact `[min_val, max_val]` range to `[-128, 127]`, tracking an explicit zero-point offset. Asymmetric quantization is more accurate for skewed, non-centered weight distributions because it makes full use of the integer range, reducing rounding errors.",
            "key_takeaways": [
                "Symmetric quantization maps zero to zero; asymmetric tracks a zero-point offset.",
                "Asymmetric quantization reduces reconstruction errors for skewed tensor distributions."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef quantize_symmetric(w):\n    # w: numpy array of floats\n    # TODO: Calculate scale, quantize to signed int8, and return (q, scale)\n    pass\n\ndef quantize_asymmetric(w):\n    # w: numpy array of floats\n    # TODO: Calculate scale, zero_point, quantize to signed int8, and return (q, scale, zero_point)\n    pass"
        },
        "expected_output": "Quantized arrays and float scale factors.",
        "follow_up_questions": [
            "What is the difference between Post-Training Quantization (PTQ) and Quantization-Aware Training (QAT)?",
            "Why do activations suffer more from quantization errors than weights? What is the 'outlier features' problem?"
        ],
        "references": [
            {
                "title": "A Survey of Quantization Methods for Efficient Neural Network Inference",
                "url": "https://arxiv.org/abs/2103.13630"
            }
        ]
    })

    # Q70: KV Cache Optimization
    questions.append({
        "id": 70,
        "slug": "kv-cache-optimization",
        "title": "Build a KV Cache Size Estimator",
        "section": "LLM",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 20,
        "tags": ["kv-cache", "gqa", "vllm"],
        "learning_objectives": [
            "Identify the memory bottleneck of the Key-Value (KV) cache",
            "Contrast Multi-Head (MHA), Multi-Query (MQA), and Grouped-Query Attention (GQA)"
        ],
        "problem_statement": "Build a python function `calculate_kv_cache_size(batch_size, seq_len, num_layers, num_heads, head_dim, attention_type, group_ratio, precision_bytes)` that computes the exact memory consumption in gigabytes of the Key-Value Cache under MHA, MQA, and GQA settings.",
        "real_world_context": "At high batch sizes, the KV Cache consumes more GPU memory than the model weights themselves. Optimizations like GQA and PagedAttention (vLLM) are required to scale concurrent user counts.",
        "hints": [
            "KV Cache size formula: `2 * num_layers * seq_len * batch_size * (num_kv_heads * head_dim) * precision_bytes`.",
            "For Multi-Head Attention (MHA): `num_kv_heads = num_heads`.",
            "For Multi-Query Attention (MQA): `num_kv_heads = 1`.",
            "For Grouped-Query Attention (GQA): `num_kv_heads = num_heads / group_ratio`."
        ],
        "solution": {
            "explanation": "During autoregressive generation, keys and values of past tokens are cached to avoid recomputing them at every step. This KV cache grows linearly with batch size and sequence length. MHA replicates KV parameters across all attention heads. MQA uses a single key-value head for all query heads, reducing memory use but degrading quality. GQA groups query heads into clusters, sharing a single KV head per cluster, balancing memory savings with model performance.",
            "key_takeaways": [
                "KV cache stores key-value projections to avoid O(L^2) redundant calculations.",
                "GQA achieves a compromise by grouping query heads, saving memory while preserving model accuracy."
            ]
        },
        "starter_code": {
            "python": "def calculate_kv_cache_size(batch_size, seq_len, num_layers, num_heads, head_dim, attention_type='mha', group_ratio=8, precision_bytes=2):\n    # TODO: Compute KV cache memory in gigabytes\n    pass"
        },
        "expected_output": "The computed size in gigabytes (float).",
        "follow_up_questions": [
            "How does PagedAttention resolve memory fragmentation in GPU servers?",
            "Why is the KV Cache size constant during the prefill phase but grows dynamically during the decoding phase?"
        ],
        "references": [
            {
                "title": "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints",
                "url": "https://arxiv.org/abs/2305.13245"
            }
        ]
    })

    # Q71: Hallucination Mitigation
    questions.append({
        "id": 71,
        "slug": "hallucination-mitigation",
        "title": "Build a Self-Consistency Voting Aggregator",
        "section": "LLM",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 15,
        "tags": ["hallucination", "self-consistency", "evaluation"],
        "learning_objectives": [
            "Explain the causes of model hallucination",
            "Implement a self-consistency aggregation algorithm"
        ],
        "problem_statement": "Build a python function `self_consistency_vote(responses)` that implements a voting aggregation system: it extracts numbers or final answers from multiple sampled reasoning paths and selects the consensus winner via majority voting.",
        "real_world_context": "When deploying LLMs for customer support or financial reporting, ensuring factual accuracy is critical. Self-consistency is a key technique to improve reasoning reliability in production.",
        "hints": [
            "Count frequencies of each candidate answer in the response list.",
            "The candidate with the highest frequency wins.",
            "Self-consistency samples multiple paths from the decoder by setting a non-zero temperature, averaging out random calculation mistakes."
        ],
        "solution": {
            "explanation": "Hallucinations occur because LLMs predict tokens based on statistical associations rather than logical reasoning or factual databases. Self-Consistency samples multiple diverse reasoning paths (e.g. 5 or 10 runs) from the model using non-zero temperature. If the model makes a random reasoning error in one path, the other paths are likely to converge on the correct answer. Aggregating the final outputs via majority vote filters out anomalous reasoning paths, increasing reliability.",
            "key_takeaways": [
                "Self-consistency aggregates multiple generations to find the consensus answer.",
                "Sampling diverse reasoning paths reduces sensitivity to local token selection errors."
            ]
        },
        "starter_code": {
            "python": "from collections import Counter\n\ndef self_consistency_vote(responses):\n    # responses: list of strings, e.g. ['The answer is 42', 'We get 42', 'Calculated 15']\n    # TODO: Extract numbers, run majority vote, and return the winner\n    pass"
        },
        "expected_output": "The consensus numerical answer.",
        "follow_up_questions": [
            "What is the difference between hallucination mitigation and verification?",
            "How does RAG (Retrieval-Augmented Generation) act as a grounding mechanism for LLMs?"
        ],
        "references": [
            {
                "title": "Self-Consistency Improves Chain of Thought Reasoning in Language Models",
                "url": "https://arxiv.org/abs/2203.11171"
            }
        ]
    })

    # Q72: FlashAttention SRAM Tiling
    questions.append({
        "id": 72,
        "slug": "flash-attention",
        "title": "Build an Online Softmax Block Updater",
        "section": "LLM",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 25,
        "tags": ["flash-attention", "gpu-hardware", "tiling"],
        "learning_objectives": [
            "Explain GPU memory hierarchy (HBM vs SRAM) and memory-bound operations",
            "Describe the tiling and online softmax scaling equations used in FlashAttention"
        ],
        "problem_statement": "Build a python function `online_softmax_update(m_old, d_old, m_block, d_block)` that updates the running maximum `m` and scaling denominator `d` to allow block-wise online softmax evaluation in SRAM, avoiding writing the global L x L attention matrix back to HBM.",
        "real_world_context": "FlashAttention speedups are the reason why modern LLMs can support 32k or 128k context windows. It reduces training and inference times by 2x to 4x without changing the mathematical output of attention.",
        "hints": [
            "High Bandwidth Memory (HBM) is large but slow; SRAM is tiny but extremely fast.",
            "Standard attention writes the intermediate `L x L` matrix to HBM and reads it back, causing high memory traffic.",
            "Online softmax updates: `m_new = max(m_old, m_block)`, `d_new = d_old * exp(m_old - m_new) + d_block * exp(m_block - m_new)`."
        ],
        "solution": {
            "explanation": "Modern GPUs have massive computing power (FLOPS) but are bottlenecked by memory transfer speeds (Memory-Bound). Standard attention writes intermediate results (`S = Q @ K.T`, `P = softmax(S)`, `O = P @ V`) back to slow HBM. FlashAttention computes attention in tiles that fit into fast SRAM. To do this, it uses online softmax tracking: it stores a running maximum `m` and denominator `d` to scale intermediate values, avoiding the need to materialise the full `L x L` matrix in HBM.",
            "key_takeaways": [
                "FlashAttention speeds up attention by optimizing GPU memory IO (HBM vs SRAM).",
                "Online softmax tracking allows computing softmax incrementally on data blocks."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef online_softmax_update(m_old, d_old, m_block, d_block):\n    # m_old, m_block: floats representing max logits\n    # d_old, d_block: floats representing softmax denominators\n    # TODO: Compute updated m_new and d_new and return them\n    pass"
        },
        "expected_output": "A tuple of floats (m_new, d_new).",
        "follow_up_questions": [
            "Why is self-attention memory-bound while matrix multiplication is compute-bound?",
            "How does FlashAttention-2 improve work partitioning across GPU thread blocks?"
        ],
        "references": [
            {
                "title": "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness",
                "url": "https://arxiv.org/abs/2205.14135"
            }
        ]
    })

    # Q73: Speculative Decoding Math
    questions.append({
        "id": 73,
        "slug": "speculative-decoding",
        "title": "Build a Speculative Decoding Token Verifier",
        "section": "LLM",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 25,
        "tags": ["speculative-decoding", "inference-acceleration", "sampling"],
        "learning_objectives": [
            "Explain the inference acceleration achieved by speculative decoding",
            "Implement the token acceptance criteria of speculative decoding"
        ],
        "problem_statement": "Build a python function `verify_tokens(draft_probs, target_probs, draft_tokens, r_values)` that evaluates speculative decoding candidates generated by a small draft model, implementing the probabilistic acceptance check and returning the accepted tokens.",
        "real_world_context": "Speculative decoding is used in high-performance serving frameworks to accelerate serving speed by 2x without degrading output quality.",
        "hints": [
            "Draft token `t` is accepted if `r <= p(t)/q(t)`, where `p` is target distribution, `q` is draft distribution, and `r ~ U(0,1)`.",
            "If a token is rejected, sample the next token from the adjusted distribution: `norm(max(0, p(x) - q(x)))`."
        ],
        "solution": {
            "explanation": "LLM decoding is memory-bandwidth bound: for each token generated, we must load gigabytes of weights from GPU HBM. Speculative decoding uses a small 'draft' model to quickly generate K candidate tokens. We then run these tokens through the large 'target' model in a single forward pass (which is fast due to batching). We accept draft tokens if their likelihood matches the target model's distribution. If a token is rejected, we discard future tokens and sample a new token from the adjusted target distribution.",
            "key_takeaways": [
                "Speculative decoding accelerates inference by validating multiple tokens in a single target forward pass.",
                "Acceptance checks ensure the output matches the exact probability distribution of the target model."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef verify_tokens(draft_probs, target_probs, draft_tokens, r_values):\n    # draft_probs: (K, vocab) probabilities from draft model\n    # target_probs: (K+1, vocab) probabilities from target model\n    # draft_tokens: list of K token IDs\n    # r_values: list of K random floats drawn from U(0,1)\n    # TODO: Determine how many draft tokens are accepted, and return accepted list + next token ID\n    pass"
        },
        "expected_output": "A tuple of (accepted_indices_list, next_sampled_token_id).",
        "follow_up_questions": [
            "How does the size difference between the draft model and target model affect the speedup ratio?",
            "Can speculative decoding be used with temperature=0 (greedy decoding)? How does the acceptance check simplify?"
        ],
        "references": [
            {
                "title": "Fast Inference from Transformers via Speculative Decoding",
                "url": "https://arxiv.org/abs/2211.17192"
            }
        ]
    })

    # Q74: Mixture of Experts (MoE) Routing
    questions.append({
        "id": 74,
        "slug": "mixture-of-experts",
        "title": "Build a Top-K Router with Load Balancing Loss",
        "section": "LLM",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 25,
        "tags": ["moe", "mixture-of-experts", "load-balancing"],
        "learning_objectives": [
            "Explain the architecture of Sparse Mixture of Experts",
            "Implement a Top-K router and calculate the load balancing loss"
        ],
        "problem_statement": "Build a python function `moe_router(token_inputs, expert_weights, k)` that routes token vectors to their Top-K expert components using dot-product similarity, and computes a load-balancing auxiliary loss to prevent routing collapse.",
        "real_world_context": "MoE is the architecture behind models like Mixtral and GPT-4. It enables models to have over 100B total parameters while only running 10-20B parameters per token, saving massive compute costs.",
        "hints": [
            "Routing scores are computed as `softmax(token_embeddings @ expert_centroids.T, axis=-1)`.",
            "Top-K selection gets the top indices and scales their scores to sum to 1.0.",
            "Load balancing loss is computed as `N * sum(f_i * P_i)`, where `f_i` is the fraction of tokens sent to expert `i`, and `P_i` is the average routing probability for expert `i`."
        ],
        "solution": {
            "explanation": "A sparse MoE replaces standard FFN layers with multiple independent 'experts' (e.g. 8). A routing network computes scores for each token and routes it to the Top-K experts (usually K=2). Only the selected experts process the token, keeping active parameters low. To prevent the router from sending all tokens to the same expert (routing collapse), we add a load balancing loss that penalizes uneven token allocations, encouraging the router to distribute workload across experts.",
            "key_takeaways": [
                "Sparse MoE keeps active parameters constant while scaling model capacity.",
                "Load balancing loss is critical to prevent routing collapse and utilize all experts."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef moe_router(token_inputs, expert_weights, k=2):\n    # token_inputs: (N, D) embeddings\n    # expert_weights: (num_experts, D) router weights\n    # TODO: Compute routing probabilities, find Top-K experts, normalize, and calculate load balancing loss\n    pass"
        },
        "expected_output": "A tuple of (expert_indices array, normalized_routing_scores, float_load_balancing_loss).",
        "follow_up_questions": [
            "What is expert capacity limit, and what happens to tokens when an expert is over-capacity?",
            "How does MoE affect memory requirements during inference deployment?"
        ],
        "references": [
            {
                "title": "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer",
                "url": "https://arxiv.org/abs/1701.06538"
            }
        ]
    })

    # Q75: Rotary Positional Embeddings (RoPE)
    questions.append({
        "id": 75,
        "slug": "rotary-positional-embeddings",
        "title": "Build a Rotary Positional Embedding (RoPE) Rotator",
        "section": "LLM",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Large Language Models",
        "estimated_time_minutes": 25,
        "tags": ["rope", "positional-encoding", "transformers-math"],
        "learning_objectives": [
            "Explain the advantages of relative positional encoding over absolute encoding",
            "Implement the 2D rotation matrix transformations of Rotary Positional Embeddings"
        ],
        "problem_statement": "Build a python function `apply_rope_2d(x, position, theta)` that applies Rotary Positional Embeddings to Query/Key coordinate pairs by rotating a 2D vector by an angle determined by token position and base frequency.",
        "real_world_context": "RoPE is the standard positional encoding used in Llama, Mistral, and Gemma models. It enables dynamic context window extension using interpolation or extrapolation techniques.",
        "hints": [
            "RoPE rotates adjacent coordinate pairs `(x1, x2)` by an angle `m * theta` where `m` is the position index.",
            "2D rotation matrix formula: `[cos(m*t), -sin(m*t); sin(m*t), cos(m*t)]`.",
            "Apply rotation: `x1_rot = x1 * cos(m*t) - x2 * sin(m*t)`, `x2_rot = x1 * sin(m*t) + x2 * cos(m*t)`."
        ],
        "solution": {
            "explanation": "Absolute positional encodings add position vectors to token embeddings, which is lost as vectors travel through attention layers. RoPE (Rotary Position Embedding) encodes position by rotating Query and Key vectors in 2D subspaces. The dot product of rotated queries and keys depends only on their *relative* distance: `R_m^T * R_n = R_(n-m)`. This preserves relative distance relationships mathematically, allowing the model to naturally handle longer sequence contexts.",
            "key_takeaways": [
                "RoPE encodes relative position by rotating Query and Key vectors in 2D planes.",
                "The dot product of RoPE-encoded query-key pairs depends only on their relative distance."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef apply_rope_2d(x, position, theta=10000.0):\n    # x: numpy array of shape (2,) representing coordinates\n    # position: integer position index\n    # TODO: Calculate rotation angle and apply rotation matrix\n    pass"
        },
        "expected_output": "Rotated coordinate vector of shape (2,).",
        "follow_up_questions": [
            "What is RoPE scaling (e.g. NTK-aware scaling), and how does it extend context windows without re-training?",
            "Why is RoPE applied only to Queries and Keys and not to Values?"
        ],
        "references": [
            {
                "title": "RoFormer: Enhanced Transformer with Rotary Position Embedding",
                "url": "https://arxiv.org/abs/2104.09864"
            }
        ]
    })
    
    return questions
