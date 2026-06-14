def get_questions():
    questions = []
    
    # Q76: Document Chunking
    questions.append({
        "id": 76,
        "slug": "document-chunking",
        "title": "Build a Sliding-Window Text Chunker",
        "section": "RAG",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 10,
        "tags": ["chunking", "data-ingest", "preprocessing"],
        "learning_objectives": [
            "Compare character-based, recursive character, and semantic chunking",
            "Implement a simple recursive character splitter"
        ],
        "problem_statement": "Build a sliding-window text chunker by implementing a python function `recursive_chunker(text, chunk_size, overlap)` that splits a string into chunks of maximum size `chunk_size` with a sliding overlap window.",
        "real_world_context": "If chunks are too small, they miss the surrounding context (e.g. pronoun references). If chunks are too large, they pollute the retrieval space with irrelevant noise and exceed model context windows.",
        "hints": [
            "A simple character slide takes a slice `text[i:i + chunk_size]` and increments the index by `chunk_size - overlap`.",
            "Make sure to handle the end of the string correctly to avoid infinite loops."
        ],
        "solution": {
            "explanation": "Character chunking splits text at fixed intervals, often cutting sentences in half. Recursive character chunking splits at logical separators (paragraphs, sentences, words) iteratively to keep semantic units together. Semantic chunking calculates embedding differences between adjacent sentences, splitting when similarity drops below a threshold, ensuring each chunk covers a single coherent topic.",
            "key_takeaways": [
                "Recursive chunking splits text on semantic boundaries (paragraphs, sentences) first.",
                "Overlap prevents information loss at chunk boundaries."
            ]
        },
        "starter_code": {
            "python": "def recursive_chunker(text, chunk_size=100, overlap=20):\n    # TODO: Implement basic character overlap chunking\n    chunks = []\n    return chunks"
        },
        "expected_output": "A list of text chunk strings.",
        "follow_up_questions": [
            "Why is overlapping chunks critical for embedding search quality?",
            "How does semantic chunking adjust split boundaries dynamically?"
        ],
        "references": [
            {
                "title": "Pinecone Document Chunking Guide",
                "url": "https://www.pinecone.io/learn/chunking-strategies/"
            }
        ]
    })
    
    # Q77: Vector Databases
    questions.append({
        "id": 77,
        "slug": "vector-databases",
        "title": "Build a Cosine Similarity Brute-Force Search Engine",
        "section": "RAG",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 15,
        "tags": ["vector-search", "hnsw", "ivf"],
        "learning_objectives": [
            "Explain similarity metric spaces (Euclidean, Cosine, Inner Product)",
            "Contrast Hierarchical Navigable Small World (HNSW) and Inverted File (IVF) index performance"
        ],
        "problem_statement": "Build a python function `brute_force_vector_search(query_vector, document_matrix)` that performs exact nearest-neighbor search using cosine similarity, and contrast its scaling with approximate nearest neighbor (ANN) indexes like HNSW and IVF.",
        "real_world_context": "At scales of 100M+ vectors, exact brute-force search is too slow. Vector databases use approximate nearest neighbor (ANN) indexes like HNSW to achieve millisecond search latency.",
        "hints": [
            "HNSW builds a multi-layer graph where query routing moves from sparse long-range jumps to dense local refinement. It is fast and accurate but consumes high memory.",
            "IVF partitions the space using K-Means and searches only inside the nearest clusters, saving memory but risking missing the absolute closest point (lower recall)."
        ],
        "solution": {
            "explanation": "HNSW (Hierarchical Navigable Small World) structures vectors as a multi-layer graph, achieving O(log N) search times. It requires storing graph edges in memory, leading to a high memory footprint. IVF (Inverted File) clusters vectors into partitions using K-Means. During query time, it only searches inside the closest centroids. This requires much less memory but can miss neighbors if they fall on partition boundaries.",
            "key_takeaways": [
                "HNSW offers high speed and recall at the expense of high memory usage.",
                "IVF reduces memory usage by partitioning the space, but has slightly lower recall."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef brute_force_vector_search(query, docs):\n    # query: (D,) embedding, docs: (N, D) matrix\n    # TODO: Compute cosine similarities and return sorted document indices\n    pass"
        },
        "expected_output": "Sorted list of tuple (doc_index, similarity_score).",
        "follow_up_questions": [
            "What is Product Quantization (PQ), and how does it compress vector index size?",
            "Why is inner-product search equivalent to cosine similarity for normalized vectors?"
        ],
        "references": [
            {
                "title": "Hierarchical Navigable Small World Graphs Paper",
                "url": "https://arxiv.org/abs/1603.09320"
            }
        ]
    })

    # Q78: Naive RAG Pipeline
    questions.append({
        "id": 78,
        "slug": "naive-rag-pipeline",
        "title": "Build a Naive RAG Prompt Injector Pipeline",
        "section": "RAG",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 15,
        "tags": ["rag", "pipelines", "architecture"],
        "learning_objectives": [
            "Implement a basic end-to-end RAG query flow",
            "Synthesize context prompts from retrieved document strings"
        ],
        "problem_statement": "Build an end-to-end RAG prompt formatting pipeline by writing a python function `query_rag_pipeline(query, retriever_func, generator_func)` that retrieves the top-K relevant context documents, inserts them into a prompt template, and sends the prompt to the generator.",
        "real_world_context": "Naive RAG is the standard starting point for building context-aware AI applications like internal document Q&A chatbots and customer support systems.",
        "hints": [
            "Call the retriever function with the query to get a list of context strings.",
            "Concatenate the context strings with clear markers like `[Document 1]...`.",
            "Construct a prompt template: 'Answer the question based only on this context: ... Question: ...'"
        ],
        "solution": {
            "explanation": "A Naive RAG pipeline performs three steps. Ingest: text is chunked, embedded, and stored. Retrieval: the user query is embedded to retrieve similar document chunks. Generation: the retrieved chunks are injected into a prompt template alongside the query, providing the LLM with the factual context needed to generate an accurate answer.",
            "key_takeaways": [
                "Naive RAG combines similarity retrieval with prompt injection to ground LLM answers.",
                "Retrieving irrelevant context can dilute the prompt and confuse the generator."
            ]
        },
        "starter_code": {
            "python": "def query_rag_pipeline(query, retriever_fn, generator_fn):\n    # retriever_fn: returns list of dict [{'text': '...'}]\n    # generator_fn: takes prompt string, returns answer string\n    # TODO: Combine retrieval context and query into a system prompt\n    pass"
        },
        "expected_output": "The response string from the generator model.",
        "follow_up_questions": [
            "What is the risk of the model ignoring the retrieved context in favor of its pre-trained weights?",
            "How does latency scale with the number of retrieved context documents?"
        ],
        "references": [
            {
                "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
                "url": "https://arxiv.org/abs/2005.11401"
            }
        ]
    })

    # Q79: Hierarchical Chunking (Parent-Child)
    questions.append({
        "id": 79,
        "slug": "hierarchical-chunking-parent-child",
        "title": "Build a Parent-Child Document Retriever",
        "section": "RAG",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 15,
        "tags": ["hierarchical-chunking", "retrieval", "search-precision"],
        "learning_objectives": [
            "Explain the conflict between retrieval granularity and generation context size",
            "Implement a parent-child document lookup map"
        ],
        "problem_statement": "Build a python class `ParentChildRetriever` that manages indexing child document sub-chunks for semantic matching while returning their corresponding larger parent document text for generation.",
        "real_world_context": "In contract analysis, a single sentence might match a user's legal query perfectly. However, the LLM needs the entire section containing that sentence to explain the contract terms accurately.",
        "hints": [
            "Divide documents into large 'parent' chunks (e.g. 1000 characters) and sub-divide those into smaller 'child' chunks (e.g. 200 characters).",
            "Embed and index ONLY the child chunks.",
            "When a child chunk matches during retrieval, look up and return its parent chunk ID in the map to feed to the LLM."
        ],
        "solution": {
            "explanation": "Small chunks (e.g., single sentences) have dense, specific semantic embeddings, making them highly effective for similarity search. However, they lack context, which can lead to disjointed or incorrect generation. Hierarchical (Parent-Child) retrieval resolves this: we search using the small child embeddings, but when a match is found, we swap the child chunk for the larger parent document before feeding it to the generator. This provides the LLM with the surrounding context needed to generate a coherent answer.",
            "key_takeaways": [
                "Child chunks optimize search precision; parent chunks optimize generation context.",
                "Swapping child chunks for parents resolves the trade-off between search and generation requirements."
            ]
        },
        "starter_code": {
            "python": "class ParentChildRetriever:\n    def __init__(self):\n        self.child_to_parent_map = {} # dict mapping child_id to parent_text\n        self.child_embeddings = {} # dict mapping child_id to vector\n        \n    def add_document(self, parent_text, child_texts, child_vectors):\n        # TODO: Store child embeddings and link child IDs to parent text\n        pass\n        \n    def retrieve(self, query_vector, k=1):\n        # TODO: Find top child vector, swap for parent text, and return it\n        pass"
        },
        "expected_output": "The parent document text associated with the top matching child vector.",
        "follow_up_questions": [
            "How does hierarchical chunking differ from Sentence-Window retrieval?",
            "What is the memory overhead of storing parent mappings in the vector index?"
        ],
        "references": [
            {
                "title": "LlamaIndex Parent-Child Retriever Guide",
                "url": "https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/"
            }
        ]
    })

    # Q80: Hybrid Search & RRF
    questions.append({
        "id": 80,
        "slug": "hybrid-search",
        "title": "Build an RRF Hybrid Search Merger",
        "section": "RAG",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 20,
        "tags": ["hybrid-search", "rrf", "bm25"],
        "learning_objectives": [
            "Combine keyword-based sparse search (BM25) with vector-based dense search",
            "Implement the Reciprocal Rank Fusion (RRF) algorithm"
        ],
        "problem_statement": "Build a python function `reciprocal_rank_fusion(dense_ranks, sparse_ranks, k)` that implements the Reciprocal Rank Fusion (RRF) algorithm, merging ranked outputs from dense vector search and sparse BM25 search into a unified list.",
        "real_world_context": "Commercial search systems (like Elasticsearch or Pinecone) use hybrid search to ensure users get relevant results regardless of whether they search using exact keywords or semantic concepts.",
        "hints": [
            "RRF Score of a document d is: `sum(1 / (k_constant + rank(d)))` across the ranked lists.",
            "Rank starts at 1 for the top item in each list.",
            "If a document is missing from a list, its rank contribution from that list is 0."
        ],
        "solution": {
            "explanation": "Dense vector search captures semantic concepts but often misses exact keyword matches like product codes or names. Sparse BM25 search matches exact words but misses synonyms and concepts. Hybrid search combines both. Since their raw scores (cosine vs BM25 score) are in different ranges, they cannot be added directly. Reciprocal Rank Fusion (RRF) solves this by ranking documents in both lists and scoring them based on their reciprocal rank position, yielding a robust merged ranking.",
            "key_takeaways": [
                "RRF merges search results based on rank positions rather than raw scores.",
                "Hybrid search balances semantic matching with exact keyword lookup."
            ]
        },
        "starter_code": {
            "python": "def reciprocal_rank_fusion(dense_ranks, sparse_ranks, k=60):\n    # dense_ranks: list of doc IDs sorted by vector similarity\n    # sparse_ranks: list of doc IDs sorted by BM25 score\n    # TODO: Calculate RRF scores and return sorted doc IDs list\n    pass"
        },
        "expected_output": "A list of doc IDs sorted by their calculated RRF score in descending order.",
        "follow_up_questions": [
            "What is the significance of the constant parameter `k` in the RRF formula?",
            "How does Cohere's reranking model compare to RRF in performance?"
        ],
        "references": [
            {
                "title": "Reciprocal Rank Fusion Paper",
                "url": "https://dl.acm.org/doi/10.1145/1571941.1572114"
            }
        ]
    })

    # Q81: Reranking
    questions.append({
        "id": 81,
        "slug": "reranking",
        "title": "Build a Cross-Encoder Candidate Reranker",
        "section": "RAG",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 15,
        "tags": ["reranking", "cross-encoders", "bi-encoders"],
        "learning_objectives": [
            "Contrast bi-encoder and cross-encoder architectures",
            "Implement a two-stage retrieval pipeline using a mock cross-encoder"
        ],
        "problem_statement": "Build a python function `rerank_candidates(query, candidates, cross_encoder_fn, top_n)` that acts as the second stage in a RAG retrieval system by re-evaluating and sorting candidate document strings using a high-precision cross-encoder scoring function.",
        "real_world_context": "Initial retrieval searches millions of documents, requiring fast vector operations. Once narrowed down to 100 candidates, we can afford a slower, more accurate cross-encoder model to sort the final list, improving generation accuracy.",
        "hints": [
            "Bi-encoders embed query and documents independently, allowing vector pre-computation. Cross-encoders feed the concatenated query + document string into a transformer, computing deep cross-attention.",
            "A cross-encoder is more accurate but far slower, making it unsuitable for searching millions of records.",
            "Sort the candidate list in descending order based on scores returned by the cross-encoder function."
        ],
        "solution": {
            "explanation": "Bi-encoders (like SentenceTransformers) embed text independently, allowing document vectors to be cached. This enables fast initial retrieval using vector similarity. However, they cannot model token-level interactions between the query and documents. Cross-encoders process the concatenated query-document pair, allowing full self-attention across all tokens. While too slow for searching a large database, they are ideal for re-scoring the top-100 retrieved candidates in a secondary step.",
            "key_takeaways": [
                "Bi-encoders support fast index retrieval; cross-encoders offer high-precision ranking.",
                "Two-stage retrieval combines bi-encoder speed with cross-encoder accuracy."
            ]
        },
        "starter_code": {
            "python": "def rerank_candidates(query, candidates, cross_encoder_fn, top_n=3):\n    # candidates: list of strings\n    # cross_encoder_fn: function taking (query, doc_str) and returning a float score\n    # TODO: Calculate scores, sort candidates, and return top_n\n    pass"
        },
        "expected_output": "A list of the top N reranked document strings.",
        "follow_up_questions": [
            "Why is a cross-encoder computationally expensive to deploy at scale?",
            "What is ColBERT, and how does it achieve late interaction similarity?"
        ],
        "references": [
            {
                "title": "SentenceTransformers Cross-Encoders Guide",
                "url": "https://www.sbert.net/examples/applications/cross-encoder/README.html"
            }
        ]
    })

    # Q82: Query Transformation
    questions.append({
        "id": 82,
        "slug": "query-transformation",
        "title": "Build a Multi-Query Decomposer",
        "section": "RAG",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 15,
        "tags": ["query-transformation", "query-rewriting", "search-recall"],
        "learning_objectives": [
            "Explain query drift and vocabulary mismatch issues",
            "Implement a mock sub-query generator"
        ],
        "problem_statement": "Build a python function `generate_sub_queries(query, mock_llm_fn)` that takes a complex, multi-part user query and uses a mock LLM generator to expand or decompose it into several specific search queries, improving overall retrieval recall.",
        "real_world_context": "If a user asks 'Compare revenue of Apple and Microsoft in 2023', a single vector search fails because the query requires looking up two separate financial reports. Decomposing the query retrieves both documents.",
        "hints": [
            "Pass the query to the LLM with instructions: 'Break down this question into sub-questions to lookup...' and parse the output.",
            "Combine the sub-queries' search results to provide a comprehensive context for the final answer."
        ],
        "solution": {
            "explanation": "Users often write vague queries or complex multi-part questions. Query expansion uses an LLM to generate synonyms or sub-queries, translating the user's intent into search-friendly terms. Decomposing complex queries into sub-queries allows retrieving distinct documents, which are then combined to answer the original multi-part question.",
            "key_takeaways": [
                "Query transformation translates conversational queries into search-optimized terms.",
                "Sub-queries split complex tasks into targeted retrievals."
            ]
        },
        "starter_code": {
            "python": "def generate_sub_queries(query, mock_llm_fn):\n    # mock_llm_fn: takes query and returns a list of sub-queries\n    # TODO: Call mock_llm_fn and return the sub-queries list\n    pass"
        },
        "expected_output": "A list of sub-query strings.",
        "follow_up_questions": [
            "What is HyDE (Hypothetical Document Embeddings), and how does it improve retrieval?",
            "How do you handle duplicate search results returned from multiple sub-queries?"
        ],
        "references": [
            {
                "title": "Query Transformations in LlamaIndex",
                "url": "https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/"
            }
        ]
    })

    # Q83: RAG Evaluation (Ragas)
    questions.append({
        "id": 83,
        "slug": "rag-evaluation-ragas",
        "title": "Build a Faithfulness Grounding Evaluator",
        "section": "RAG",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 20,
        "tags": ["evaluation", "ragas", "metrics"],
        "learning_objectives": [
            "Define the three core Ragas evaluation metrics: Faithfulness, Answer Relevance, Context Precision",
            "Implement a mock check for Faithfulness using LLM extraction"
        ],
        "problem_statement": "Build a python function `evaluate_faithfulness(generated_answer, contexts, mock_evaluator_llm)` that programmatically evaluates the grounding of a RAG model's answer, computing a faithfulness score based on how many claims can be verified directly from the retrieved context.",
        "real_world_context": "In regulated industries like banking or medicine, evaluating RAG outputs programmatically is essential to ensure models do not invent facts and stay grounded in approved documentation.",
        "hints": [
            "Faithfulness = (Number of statements in answer supported by context) / (Total number of statements in answer).",
            "Use the extractor LLM to split the answer into factual claims, then verify each claim against the context."
        ],
        "solution": {
            "explanation": "Evaluating RAG with standard metrics like BLEU or ROUGE is unreliable because they measure word overlap rather than semantic correctness. Ragas uses LLM-as-a-judge to evaluate metrics: (1) Faithfulness: verifies if the generated answer is derived *only* from the retrieved context (no hallucinations), (2) Answer Relevance: measures if the answer addresses the user's question, and (3) Context Recall: evaluates if the retriever found all the information required.",
            "key_takeaways": [
                "Ragas uses LLM evaluation to measure semantic correctness and grounding.",
                "Faithfulness measures grounding; Answer Relevance measures query alignment."
            ]
        },
        "starter_code": {
            "python": "def evaluate_faithfulness(generated_answer, contexts, mock_evaluator_llm):\n    # mock_evaluator_llm: takes (statement, context) and returns boolean support\n    # TODO: Parse answer into claims, verify against context, and return score (0.0 to 1.0)\n    pass"
        },
        "expected_output": "A float score between 0.0 and 1.0 indicating faithfulness.",
        "follow_up_questions": [
            "Why is Context Recall evaluated using ground truth, while Faithfulness is evaluated without it?",
            "What are the risks of using LLMs as judges to evaluate other LLMs?"
        ],
        "references": [
            {
                "title": "RAGAS: Automated Evaluation of Retrieval Augmented Generation",
                "url": "https://arxiv.org/abs/2309.15217"
            }
        ]
    })

    # Q84: Metadata Filtering & Graph RAG
    questions.append({
        "id": 84,
        "slug": "metadata-filtering-graph-rag",
        "title": "Build a Graph RAG Adjacency List Constructor",
        "section": "RAG",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 25,
        "tags": ["metadata-filtering", "graph-rag", "knowledge-graphs"],
        "learning_objectives": [
            "Apply metadata filtering to narrow down vector searches",
            "Explain how Graph RAG builds entity relationships for global queries"
        ],
        "problem_statement": "Build a python function `build_adjacency_list(entities, relationships)` that constructs a graph representation of extracted RAG entities and their relationships, facilitating structured Graph RAG path traversal for multi-hop queries.",
        "real_world_context": "Standard RAG excels at local, specific queries ('What is the return policy?'). Graph RAG is designed for global queries ('What are the common complaints across all customer reviews?'), resolving connections across separate documents.",
        "hints": [
            "Metadata filtering applies SQL-like clauses during the vector search (e.g., in HNSW graph traversal) to ignore invalid nodes.",
            "Graph RAG extracts (Subject, Relationship, Object) triples and groups entities into hierarchical communities.",
            "An adjacency list maps each node to a list of its connected neighbors and edge attributes."
        ],
        "solution": {
            "explanation": "Metadata filtering applies hard constraints (like `year=2023`) to vector searches. Doing this during index traversal (pre-filtering) is much more efficient than filtering results after the search (post-filtering), which can lead to returning fewer than K results. Graph RAG extracts entities and relationships from texts, building a knowledge graph. By clustering the graph into communities and generating summaries for each community, it can answer global queries that span the entire document library, which standard RAG struggles to do.",
            "key_takeaways": [
                "Metadata filtering applies hard filters during vector traversal to preserve search precision.",
                "Graph RAG clusters entity relationship networks, enabling global, cross-document summaries."
            ]
        },
        "starter_code": {
            "python": "def build_adjacency_list(entities, relationships):\n    # entities: list of strings ['Apple', 'Microsoft', ...]\n    # relationships: list of tuples [('Apple', 'competes_with', 'Microsoft')]\n    # TODO: Build and return adjacency list dictionary\n    pass"
        },
        "expected_output": "A dictionary mapping nodes to lists of connected neighbors and edge details.",
        "follow_up_questions": [
            "Why does post-filtering in vector databases result in returning fewer than the requested K documents?",
            "What clustering algorithm is commonly used in Graph RAG to define entity communities?"
        ],
        "references": [
            {
                "title": "From Local to Global: A Graph RAG Approach to Query-Focused Summarization",
                "url": "https://arxiv.org/abs/2404.16130"
            }
        ]
    })

    # Q85: Lost in the Middle & Compression
    questions.append({
        "id": 85,
        "slug": "lost-in-the-middle-context-compression",
        "title": "Build a Lost-in-the-Middle Context Reorderer",
        "section": "RAG",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Retrieval-Augmented Generation",
        "estimated_time_minutes": 25,
        "tags": ["lost-in-the-middle", "context-compression", "llmlingua"],
        "learning_objectives": [
            "Explain the 'lost-in-the-middle' phenomenon in long-context models",
            "Implement a mock information density context compressor"
        ],
        "problem_statement": "Build a python function `reorder_documents(sorted_docs)` that mitigates the 'lost-in-the-middle' phenomenon in long prompt sequences by taking a list of documents sorted from most to least relevant and redistributing them such that the highest-ranked documents are positioned at the boundaries (start and end) of the prompt.",
        "real_world_context": "Even if an LLM supports a 128k context, feeding it large, uncompressed document sets increases latency, cost, and the risk of the model overlooking the correct answer if it is buried in the middle of the prompt.",
        "hints": [
            "The U-shaped curve shows that LLMs focus best on information at the start (primacy effect) and end (recency effect) of the prompt.",
            "Sort documents by relevance descending, then distribute them: place rank 1 at the start, rank 2 at the end, rank 3 next to start, rank 4 next to end, etc.",
            "LLMLingua calculates the perplexity of tokens using a small model (like LLaMA-2-7B), discarding tokens that have low information density (low perplexity) without losing semantic meaning."
        ],
        "solution": {
            "explanation": "Research shows LLMs are much better at retrieving information from the beginning (primacy) and end (recency) of a long prompt. If the answer is in the middle of a long context, retrieval performance degrades (lost-in-the-middle). Reordering documents places the highest-ranked results at the boundaries, minimizing this issue. Prompt compression (like LLMLingua) uses a small model to calculate the perplexity of each word. Words with low perplexity are highly predictable (e.g. 'the', 'and', or filler) and can be removed without losing the core information, saving tokens and costs.",
            "key_takeaways": [
                "LLMs pay attention best to the start and end of prompt contexts, ignoring the middle.",
                "Reordering documents distributes high-relevance chunks to the prompt boundaries.",
                "Perplexity-based compression removes redundant tokens, reducing latency and API costs."
            ]
        },
        "starter_code": {
            "python": "def reorder_documents(sorted_docs):\n    # sorted_docs: list of document strings sorted from most to least relevant\n    # TODO: Reorder list such that best docs are at the start and end, and worst are in the middle\n    pass"
        },
        "expected_output": "The reordered list of document strings.",
        "follow_up_questions": [
            "How does prompt length affect LLM generation latency (TTFT vs execution time)?",
            "Under what conditions does prompt compression degrade model response quality?"
        ],
        "references": [
            {
                "title": "Lost in the Middle: How Language Models Use Long Contexts",
                "url": "https://arxiv.org/abs/2307.03172"
            },
            {
                "title": "LLMLingua: Compressing Prompts for Accelerated Inference",
                "url": "https://arxiv.org/abs/2310.05736"
            }
        ]
    })
    
    return questions
