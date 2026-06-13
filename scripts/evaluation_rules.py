EVALUATION_RULES = {
    1: [
        "Defines the function `evaluate_memory_usage`",
        "Uses `sys.getsizeof` to check memory usage",
        "Creates a list comprehension using `[` and `]`",
        "Creates a generator expression using `(` and `)`",
        "Does not contain `TODO`"
    ],
    2: [
        "Defines the decorator `time_it`",
        "Uses `@time_it` to decorate the function",
        "Uses `@wraps` or `wraps(func)` to preserve metadata",
        "Does not contain `TODO`"
    ],
    3: [
        "Defines the function `forward_arguments`",
        "Uses `*args` and `**kwargs` in the signature",
        "Calls `target_func(*args, **kwargs)`",
        "Does not contain `TODO`"
    ],
    4: [
        "Defines the class `DatabaseConnection`",
        "Defines `__enter__` and `__exit__` in the class",
        "Defines generator context manager `db_connection_generator` using `@contextmanager`",
        "Does not contain `TODO`"
    ],
    5: [
        "Defines the class `Vector2D`",
        "Implements `__add__` operator overloading",
        "Implements `__len__` to calculate length",
        "Implements comparison method `__lt__` or `__eq__`",
        "Implements indexing method `__getitem__`",
        "Does not contain `TODO`"
    ],
    6: [
        "Defines the class `FibonacciIterator`",
        "Implements `__iter__` method returning self",
        "Implements `__next__` method to yield numbers",
        "Raises `StopIteration` when limit is exceeded",
        "Does not contain `TODO`"
    ],
    7: [
        "Defines the function `run_concurrent_tasks`",
        "Uses `ThreadPoolExecutor` or `ProcessPoolExecutor`",
        "Supports mode parameter for `thread` vs `process`",
        "Does not contain `TODO`"
    ],
    8: [
        "Defines the async function `fetch_source`",
        "Defines the async function `fetch_data_from_sources`",
        "Uses `asyncio.sleep` to simulate delay",
        "Uses `asyncio.gather` to run concurrently",
        "Does not contain `TODO`"
    ],
    9: [
        "Defines the metaclass `RequireModelFormatMeta` inheriting from `type`",
        "Implements `__new__` method in the metaclass",
        "Raises `TypeError` if class format requirements are not met",
        "Does not contain `TODO`"
    ],
    10: [
        "Defines the function `build_leak` creating circular refs",
        "Defines the function `build_fixed_leak` breaking cycles",
        "Uses `weakref.ref` or `weakref` module",
        "Does not contain `TODO`"
    ],
    11: [
        "Defines the function `calculate_central_tendencies`",
        "Uses `statistics` or `np` functions to calculate mean, median, mode",
        "Appends a large outlier to test percentage shifts",
        "Does not contain `TODO`"
    ],
    12: [
        "Defines the function `verify_independence`",
        "Calculates conditional probability of purchase given mobile",
        "Determines and returns a boolean for variable independence",
        "Does not contain `TODO`"
    ],
    13: [
        "Defines the function `calculate_posterior_clean`",
        "Applies Bayes Theorem mathematically using prior and likelihood",
        "Does not contain `TODO`"
    ],
    14: [
        "Defines the function `integrate_normal_pdf`",
        "Implements trapezoidal numerical integration rule",
        "Does not contain `TODO`"
    ],
    15: [
        "Defines the function `simulate_clt`",
        "Draws samples from the population with replacement using `random` or `np`",
        "Calculates empirical standard error and theoretical standard error",
        "Does not contain `TODO`"
    ],
    16: [
        "Defines the function `two_proportion_z_test`",
        "Calculates z-statistic using standard error of differences",
        "Uses `norm.cdf` or `norm.sf` to calculate two-tailed p-value",
        "Does not contain `TODO`"
    ],
    17: [
        "Defines the function `calculate_type_ii_error`",
        "Calculates critical value using `norm.ppf`",
        "Computes beta type II error rate using `norm.cdf`",
        "Does not contain `TODO`"
    ],
    18: [
        "Defines the function `compute_critical_values`",
        "Uses `scipy.stats` distributions `norm` and `t`",
        "Calculates two-tailed critical z and t scores using `ppf`",
        "Does not contain `TODO`"
    ],
    19: [
        "Defines the function `one_way_anova`",
        "Calculates SSB (Sum of Squares Between) and SSW (Sum of Squares Within)",
        "Returns the final F-statistic",
        "Does not contain `TODO`"
    ],
    20: [
        "Defines the function `compare_correlations`",
        "Uses `scipy.stats` or stats modules to calculate Pearson and Spearman",
        "Does not contain `TODO`"
    ],
    21: [
        "Defines the function `find_mle_bernoulli`",
        "Calculates parameter p using the average of binary observations",
        "Does not contain `TODO`"
    ],
    22: [
        "Defines the function `calculate_confidence_interval`",
        "Calculates standard error of mean using sample standard deviation",
        "Uses T-distribution critical value using `t.ppf`",
        "Does not contain `TODO`"
    ],
    23: [
        "Defines the function `simulate_bias_variance`",
        "Fits a simple model across multiple simulated training sets",
        "Estimates bias squared, variance, and MSE",
        "Does not contain `TODO`"
    ],
    24: [
        "Defines the function `adjust_p_values`",
        "Implements Bonferroni correction by scaling p-values",
        "Implements Benjamini-Hochberg FDR procedure",
        "Does not contain `TODO`"
    ],
    25: [
        "Defines the function `metropolis_hastings`",
        "Implements sampling loop with acceptance probability check",
        "Does not contain `TODO`"
    ],
    26: [
        "Defines the function `fit_linear_regression`",
        "Uses `np.dot` or `@` operator to compute matrix multiplication",
        "Uses `np.linalg.inv` or `np.linalg.pinv` to invert the matrix",
        "Does not contain `TODO`"
    ],
    27: [
        "Defines the function `gradient_descent_step`",
        "Calculates predictions and prediction error",
        "Computes MSE loss value",
        "Updates weights theta using computed gradients and learning rate",
        "Does not contain `TODO`"
    ],
    28: [
        "Defines the function `predict_probability`",
        "Defines the function `binary_cross_entropy`",
        "Uses `np.clip` to avoid log(0) numerical errors",
        "Does not contain `TODO`"
    ],
    29: [
        "Defines the function `knn_classify`",
        "Computes Euclidean distances between test sample and training samples",
        "Selects top k nearest neighbors",
        "Assigns classes using majority vote via `Counter` or statistics",
        "Does not contain `TODO`"
    ],
    30: [
        "Defines the function `calculate_entropy`",
        "Defines the function `calculate_gini`",
        "Defines the function `calculate_information_gain`",
        "Calculates gain by subtracting weighted child impurities from parent",
        "Does not contain `TODO`"
    ],
    31: [
        "Defines the function `k_fold_indices`",
        "Yields training and validation index splits as pairs",
        "Does not contain `TODO`"
    ],
    32: [
        "Defines the function `regularized_loss`",
        "Computes MSE loss between true and predicted targets",
        "Adds L1 absolute weight penalty",
        "Adds L2 squared weight penalty",
        "Does not contain `TODO`"
    ],
    33: [
        "Defines the function `rbf_kernel`",
        "Computes pairwise squared Euclidean distances between X1 and X2",
        "Returns the exponential of negative scaled distances",
        "Does not contain `TODO`"
    ],
    34: [
        "Defines the function `bootstrap_sample`",
        "Draws samples with replacement using `np.random.choice` or similar",
        "Identifies Out-Of-Bag (OOB) indices using differences",
        "Does not contain `TODO`"
    ],
    35: [
        "Defines the function `compute_pseudo_residuals`",
        "Defines the function `mock_boosting_step`",
        "Calculates difference between true targets and predicted probabilities",
        "Updates prediction vector by adding scaled weak predictions",
        "Does not contain `TODO`"
    ],
    36: [
        "Defines the function `kmeans_step`",
        "Assigns each data point to its closest centroid",
        "Recomputes centroid coordinates as the mean of assigned points",
        "Does not contain `TODO`"
    ],
    37: [
        "Defines the function `pca_projection`",
        "Standardizes input data to zero mean and unit variance",
        "Computes covariance matrix using `np.cov` or matrix multiplication",
        "Computes eigenvalues and eigenvectors using `np.linalg.eig` or `np.linalg.eigh`",
        "Projects centered data onto top principal components",
        "Does not contain `TODO`"
    ],
    38: [
        "Defines the function `compute_precision_recall_f1`",
        "Counts true positives, false positives, false negatives",
        "Computes precision, recall, and F1-score with division safety",
        "Does not contain `TODO`"
    ],
    39: [
        "Defines the function `weighted_cross_entropy`",
        "Penalizes class 0 and class 1 errors using custom weight coefficients",
        "Does not contain `TODO`"
    ],
    40: [
        "Defines the function `random_search_sampler`",
        "Samples values randomly from choices list or float uniform interval",
        "Yields hyperparameter combinations as dictionaries",
        "Does not contain `TODO`"
    ],
    41: [
        "Defines the function `target_encode`",
        "Calculates global target mean from training set",
        "Computes category target means smoothed by global statistics",
        "Maps computed encodings to training and validation sets",
        "Does not contain `TODO`"
    ],
    42: [
        "Defines the function `calculate_xgboost_split_gain`",
        "Computes gain using leaf score formulas (summed gradients and hessians)",
        "Subtracts base parent score and subtracts split penalty parameter gamma",
        "Does not contain `TODO`"
    ],
    43: [
        "Defines the function `naive_bayes_predict`",
        "Applies Laplace smoothing by adding alpha to counts in numerator and vocab_size to denominator",
        "Uses class priors and log likelihood sums for prediction scores",
        "Does not contain `TODO`"
    ],
    44: [
        "Defines the function `gmm_e_step`",
        "Uses `multivariate_normal.pdf` or similar to compute likelihoods",
        "Calculates responsibility matrix normalized by partition sum",
        "Does not contain `TODO`"
    ],
    45: [
        "Defines the function `kernel_pca_matrix`",
        "Computes centered kernel matrix using centering equation formula",
        "Does not contain `TODO`"
    ],
    46: [
        "Defines the function `relu` using `np.maximum` or comparison",
        "Defines the function `relu_derivative` returning 1 for positive, 0 otherwise",
        "Does not contain `TODO`"
    ],
    47: [
        "Defines the function `forward_pass`",
        "Calculates hidden layer pre-activations and applies `relu` activation",
        "Computes output logits using linear weights projection",
        "Does not contain `TODO`"
    ],
    48: [
        "Defines the function `backward_pass`",
        "Computes output error gradient and hidden layer error gradient",
        "Computes gradients dW2 and dW1 using transpose dot products",
        "Does not contain `TODO`"
    ],
    49: [
        "Defines the function `softmax_cross_entropy_gradient`",
        "Calculates logit gradients as the difference between softmax probabilities and target matrix",
        "Does not contain `TODO`"
    ],
    50: [
        "Defines the function `check_gradient_norms`",
        "Computes Frobenius norm for each layer matrix using `np.linalg.norm` or sum of squares",
        "Categorizes norm states based on min and max threshold boundaries",
        "Does not contain `TODO`"
    ],
    51: [
        "Defines the function `adam_update`",
        "Updates running first moment estimate using beta1",
        "Updates running second moment estimate using beta2",
        "Computes bias-corrected moment estimates",
        "Updates parameter vector using corrected moments and epsilon",
        "Does not contain `TODO`"
    ],
    52: [
        "Defines the function `dropout_layer`",
        "Generates boolean scaling mask from uniform or binomial distributions",
        "Applies scaled mask to activations (inverted dropout)",
        "Bypasses dropout modification during evaluation mode (training=False)",
        "Does not contain `TODO`"
    ],
    53: [
        "Defines the function `batch_norm_forward`",
        "Computes mini-batch mean and variance across training dimensions",
        "Normalizes activations and applies learnable scaling gamma and shift beta",
        "Updates running mean and running variance statistics in-place",
        "Does not contain `TODO`"
    ],
    54: [
        "Defines the function `calculate_cnn_output_shape`",
        "Calculates spatial dimensions using floor division including padding and stride factors",
        "Does not contain `TODO`"
    ],
    55: [
        "Defines the function `lstm_cell_forward`",
        "Computes gates (forget, input, output, candidate) using sigmoid and tanh activations",
        "Updates cell state and calculates next hidden state activations",
        "Does not contain `TODO`"
    ],
    56: [
        "Defines the function `autoencoder_loss`",
        "Calculates Mean Squared Error reconstruction loss using square differences",
        "Does not contain `TODO`"
    ],
    57: [
        "Defines the function `freeze_model_layers`",
        "Sets `requires_grad = False` for all backbone model params",
        "Retains `requires_grad = True` for the final classifier head parameter",
        "Does not contain `TODO`"
    ],
    58: [
        "Defines the function `scaled_dot_product_attention`",
        "Computes query-key attention scores using dot product matrix multiplication",
        "Scales attention scores by dividing by square root of head dimension",
        "Applies softmax to get weights and multiplies by value vectors",
        "Does not contain `TODO`"
    ],
    59: [
        "Defines the function `causal_attention`",
        "Creates a causal lower-triangular mask matrix",
        "Applies mask by adding negative infinity (-inf or -1e9) to future positions",
        "Does not contain `TODO`"
    ],
    60: [
        "Defines the function `calculate_zero_stage_memory`",
        "Calculates memory partition distributions across GPUs for Stage 1, 2, and 3 configurations",
        "Does not contain `TODO`"
    ],
    61: [
        "Defines the function `get_stats` counting adjacent token pairs",
        "Defines the function `merge_vocab` substituting character pairs with merged token",
        "Does not contain `TODO`"
    ],
    62: [
        "Defines the function `sample_logits`",
        "Scales logits using temperature parameter division",
        "Applies top-p filtering threshold to cumulative sorted probability sums",
        "Does not contain `TODO`"
    ],
    63: [
        "Defines the class `PromptBuilder`",
        "Implements method `add_example` registering few-shot pairs",
        "Implements method `build_prompt` formatting input instructions, examples, and CoT suffix",
        "Does not contain `TODO`"
    ],
    64: [
        "Defines the function `cosine_similarity`",
        "Calculates dot product of vectors and divides by product of L2 norms",
        "Does not contain `TODO`"
    ],
    65: [
        "Defines the function `calculate_attention_matrix_size`",
        "Calculates memory size of L x L attention matrix in megabytes",
        "Does not contain `TODO`"
    ],
    66: [
        "Defines the function `mask_prompt_loss`",
        "Replaces target token IDs in prompt prefix region with classification ignore index",
        "Does not contain `TODO`"
    ],
    67: [
        "Defines the class `LoraLinear`",
        "Initializes trainable low-rank adapters A and B with dimensions r",
        "Implements LoRA forward equation adding low-rank update to frozen projection",
        "Does not contain `TODO`"
    ],
    68: [
        "Defines the function `dpo_loss`",
        "Calculates log ratios of policy model choices and reference model choices",
        "Computes cross-entropy DPO objective using sigmoid of scaled differences",
        "Does not contain `TODO`"
    ],
    69: [
        "Defines the function `quantize_symmetric` mapping values to range",
        "Defines the function `quantize_asymmetric` incorporating zero-point shift",
        "Does not contain `TODO`"
    ],
    70: [
        "Defines the function `calculate_kv_cache_size`",
        "Computes cache memory scale for Multi-Head, Multi-Query, and Grouped-Query settings",
        "Does not contain `TODO`"
    ],
    71: [
        "Defines the function `self_consistency_vote`",
        "Extracts numeric answers from reasoning paths",
        "Applies majority vote consensus to select winning output candidate",
        "Does not contain `TODO`"
    ],
    72: [
        "Defines the function `online_softmax_update`",
        "Updates running maximum metric scale",
        "Normalizes running sum denominators using scaling exponents",
        "Does not contain `TODO`"
    ],
    73: [
        "Defines the function `verify_tokens`",
        "Implements target acceptance threshold verification loop for speculative generation",
        "Does not contain `TODO`"
    ],
    74: [
        "Defines the function `moe_router`",
        "Selects top-k experts for tokens using similarity gating weights",
        "Computes load balancing helper loss to enforce routing fairness",
        "Does not contain `TODO`"
    ],
    75: [
        "Defines the function `apply_rope_2d`",
        "Computes rotary angle based on position index and theta base frequency",
        "Applies 2D rotation matrix multiplication to coordinates",
        "Does not contain `TODO`"
    ],
    76: [
        "Defines the function `recursive_chunker`",
        "Segments input text into character chunks using size and sliding window overlap",
        "Does not contain `TODO`"
    ],
    77: [
        "Defines the function `brute_force_vector_search`",
        "Computes cosine similarities between query and all document embedding vectors",
        "Returns document indices sorted from highest to lowest similarity score",
        "Does not contain `TODO`"
    ],
    78: [
        "Defines the function `query_rag_pipeline`",
        "Retrieves top context documents using retriever function",
        "Injects query and text context into template and calls generator",
        "Does not contain `TODO`"
    ],
    79: [
        "Defines the class `ParentChildRetriever`",
        "Stores sub-chunk mapping relations and computes document retrieval references",
        "Does not contain `TODO`"
    ],
    80: [
        "Defines the function `reciprocal_rank_fusion`",
        "Calculates RRF scores for merged ranks using smoothing constant k",
        "Returns final candidate lists sorted from highest to lowest score",
        "Does not contain `TODO`"
    ],
    81: [
        "Defines the function `rerank_candidates`",
        "Scores query-document pairs using cross-encoder scorer function",
        "Returns sorted top-N high relevance candidates",
        "Does not contain `TODO`"
    ],
    82: [
        "Defines the function `generate_sub_queries`",
        "Decomposes single user query into multiple search tasks",
        "Does not contain `TODO`"
    ],
    83: [
        "Defines the function `evaluate_faithfulness`",
        "Compares generated claims against context using helper evaluator",
        "Returns ratio score indicating how many claims are fully grounded",
        "Does not contain `TODO`"
    ],
    84: [
        "Defines the function `build_adjacency_list`",
        "Constructs graph structure representation from entities and relationship tuples",
        "Does not contain `TODO`"
    ],
    85: [
        "Defines the function `reorder_documents`",
        "Places highest relevance documents at boundaries and lowest in middle",
        "Does not contain `TODO`"
    ],
    86: [
        "Defines the function `parse_react_response`",
        "Parses Thought, Action, Action Input, or Final Answer keys",
        "Does not contain `TODO`"
    ],
    87: [
        "Defines the function `run_agent`",
        "Executes Thought -> Action -> Observation cycle iteratively",
        "Invokes tools and formats history until final answer is generated",
        "Does not contain `TODO`"
    ],
    88: [
        "Defines the function `sliding_window_memory`",
        "Prunes chat message history context to fit within token boundaries",
        "Guarantees that the first system instruction message is never pruned",
        "Does not contain `TODO`"
    ],
    89: [
        "Defines the function `validate_and_execute_tool`",
        "Parses input parameters and checks compliance with schema instructions",
        "Executes callback handler with valid arguments",
        "Does not contain `TODO`"
    ],
    90: [
        "Defines the class `SimpleAgentGraph`",
        "Registers execution nodes and edge router functions",
        "Runs graph traversal loops starting from initial state until terminal status",
        "Does not contain `TODO`"
    ],
    91: [
        "Defines the function `reflection_loop`",
        "Runs code generator and critique loops to update draft proposals",
        "Does not contain `TODO`"
    ],
    92: [
        "Defines the function `orchestrate_agents`",
        "Invokes central supervisor to distribute tasks to specialized workers",
        "Aggregates and formats results",
        "Does not contain `TODO`"
    ],
    93: [
        "Defines the function `execute_with_self_healing`",
        "Executes python code dynamically inside safety boundaries",
        "Captures execution errors and routes stacktrace back to corrector",
        "Does not contain `TODO`"
    ],
    94: [
        "Defines the function `agentic_rag_loop`",
        "Routes user questions to database context or web search",
        "Grades retrieval relevance and falls back if grading fails",
        "Does not contain `TODO`"
    ],
    95: [
        "Defines the function `prune_dom_tree`",
        "Parses html page tree structure using BeautifulSoup parser",
        "Filters for interactive elements like anchor, input, and button elements",
        "Does not contain `TODO`"
    ]
}

MANUAL_TEST_CASES = {
    1: [
        {"input": "evaluate_memory_usage()", "expected": "(8000120, 112)"}
    ],
    2: [
        {"input": "compute_heavy_sum(1000000)", "expected": "500000500000"}
    ],
    3: [
        {"input": "forward_arguments(lambda a, b: a + b, 1, 2)", "expected": "3"}
    ],
    5: [
        {"input": "v1 = Vector2D(1, 2); v2 = Vector2D(3, 4); v1 + v2", "expected": "Vector2D(4, 6)"},
        {"input": "len(Vector2D(3, 4))", "expected": "5"}
    ],
    11: [
        {"input": "calculate_central_tendencies([1, 2, 2, 3, 4])", "expected": "{'mean_shift': 99.6, 'median_shift': 0.0, 'mode_shift': 0.0}"}
    ],
    26: [
        {"input": "fit_linear_regression(np.array([[1], [2], [3]]), np.array([3, 5, 7]))", "expected": "[1.0, 2.0]"}
    ],
    86: [
        {"input": "parse_react_response('Thought: thinking\\nAction: call_tool\\nAction Input: input')", "expected": "{'Thought': 'thinking', 'Action': 'call_tool', 'Action Input': 'input'}"}
    ]
}

