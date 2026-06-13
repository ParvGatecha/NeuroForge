def get_questions():
    questions = []
    
    # Q96: Real-time Fraud Detection Pipeline
    questions.append({
        "id": 96,
        "slug": "real-time-fraud-detection-pipeline",
        "title": "Design a Real-time Fraud Detection Pipeline",
        "section": "System Design",
        "difficulty": "Easy",
        "question_type": "system_design",
        "neuroforge_skill": "Machine Learning System Design",
        "estimated_time_minutes": 15,
        "tags": ["system-design", "streaming", "inference-pipeline"],
        "learning_objectives": [
            "Design a low-latency real-time prediction system",
            "Contrast batch feature calculation with online streaming feature ingestion"
        ],
        "problem_statement": "Design a real-time credit card fraud detection system. The system must process transaction events and return a fraud/no-fraud classification within 50 milliseconds. Detail: (1) how you ingest transaction data, (2) where you store historical transaction features (e.g. 'number of transactions in the last 2 hours'), (3) how you handle the cold start problem for new users, and (4) how you balance model accuracy against latency budgets.",
        "real_world_context": "Financial systems process millions of transactions per minute. A fraud classification service must run inline with payment processing gateways without causing delays for legitimate shoppers.",
        "hints": [
            "Use a streaming pipeline like Apache Kafka or Flink to process events in real time.",
            "Use an online feature store like Redis or Feast to look up pre-computed historical features in under 5 milliseconds.",
            "Fallback to global or group-based feature averages for new users who do not have a transaction history (cold start)."
        ],
        "solution": {
            "explanation": "To achieve <50ms latency, we separate feature computation into offline (batch) and online (streaming) paths. Raw transaction events flow into Kafka. A streaming engine (Flink) processes these events to update online features in Redis (e.g., sliding-window transaction counts). During an transaction request, the API gateway fetches pre-computed features from Redis, combines them with the transaction metadata, and queries a lightweight model (like XGBoost) hosted on a fast inference engine (Triton). If Redis is unavailable, the system falls back to default cached features to maintain service availability.",
            "key_takeaways": [
                "Split-path architectures combine slow batch features with fast streaming features.",
                "Feast/Redis feature stores provide low-latency lookups during online inference."
            ]
        },
        "evaluation_points": [
            "Inference latency (<50ms constraint)",
            "Consistency between training and serving features (no training-serving skew)",
            "System availability during database or cache outages",
            "Data ingestion scalability under high transaction volumes"
        ],
        "follow_up_questions": [
            "How do you handle training-serving skew when updating online features?",
            "What database would you use to store historical transaction logs for offline model training?"
        ],
        "references": [
            {
                "title": "Uber Michelangelo: Machine Learning Platform",
                "url": "https://www.uber.com/blog/michelangelo-machine-learning-platform/"
            }
        ]
    })
    
    # Q97: LLM Serving Infrastructure
    questions.append({
        "id": 97,
        "slug": "llm-serving-infrastructure",
        "title": "Design a High-Throughput LLM Serving Infrastructure",
        "section": "System Design",
        "difficulty": "Medium",
        "question_type": "system_design",
        "neuroforge_skill": "Machine Learning System Design",
        "estimated_time_minutes": 25,
        "tags": ["system-design", "serving", "vllm", "concurrency"],
        "learning_objectives": [
            "Optimize serving systems for high concurrent user throughput",
            "Describe the mechanics of continuous batching and PagedAttention"
        ],
        "problem_statement": "Design a high-throughput LLM serving infrastructure capable of handling 500 concurrent user requests. Detail: (1) why static batching is inefficient for LLM generation, (2) how continuous batching (dynamic iteration-level scheduling) solves this, (3) how PagedAttention reduces GPU memory fragmentation, and (4) how you allocate GPU resources between the prefill and decoding phases of generation.",
        "real_world_context": "Serving LLMs is expensive due to GPU memory and compute requirements. Serving frameworks like vLLM or TensorRT-LLM use these optimization techniques to cut hosting costs by 4x.",
        "hints": [
            "In static batching, all requests in a batch wait until the longest generation finishes, wasting GPU cycles on completed requests.",
            "Continuous batching inserts and extracts requests from the active execution batch at the token-generation iteration level.",
            "PagedAttention splits the KV cache into non-contiguous virtual pages, avoiding the need to pre-allocate maximum-length contiguous memory blocks for every request."
        ],
        "solution": {
            "explanation": "LLM generation is an autoregressive process where output lengths vary. Static batching forces the system to pad shorter outputs, wasting compute. We implement continuous batching, scheduling new requests into the batch at the token-iteration level. To prevent GPU memory fragmentation caused by pre-allocating memory for the worst-case context window, we implement PagedAttention. This allocates KV cache pages in virtual memory blocks, allowing non-contiguous GPU memory to be used. We also partition GPUs into prefill (compute-bound) and decode (memory-bound) clusters to optimize resource allocation.",
            "key_takeaways": [
                "Continuous batching schedulers operate at the token-iteration level, eliminating padding waste.",
                "PagedAttention resolves GPU memory fragmentation, allowing higher concurrency batch sizes."
            ]
        },
        "evaluation_points": [
            "Requests per second throughput",
            "Time to First Token (TTFT) latency",
            "Inter-token latency (decoding speed)",
            "GPU memory utilization efficiency"
        ],
        "follow_up_questions": [
            "How does Tensor Parallelism affect serving latency across a multi-GPU node?",
            "What is the difference between offline batch inference and online streaming inference for LLMs?"
        ],
        "references": [
            {
                "title": "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention",
                "url": "https://arxiv.org/abs/2309.06180"
            }
        ]
    })
    
    # Q98: Search & Recommendation System
    questions.append({
        "id": 98,
        "slug": "search-recommendation-system",
        "title": "Design a Two-Stage Search and Recommendation System",
        "section": "System Design",
        "difficulty": "Medium",
        "question_type": "system_design",
        "neuroforge_skill": "Machine Learning System Design",
        "estimated_time_minutes": 20,
        "tags": ["system-design", "recommendation-system", "two-stage-architecture"],
        "learning_objectives": [
            "Design a two-stage recommendation pipeline (Retrieval + Ranking)",
            "Optimize candidate generation and precise ranking models"
        ],
        "problem_statement": "Design an e-commerce item recommendation system for a catalog of 10 million products. Detail: (1) why a two-stage architecture is required, (2) how the Retrieval (candidate generation) stage narrows down products, (3) how the Ranking stage scores candidates, and (4) how you incorporate real-time user click feedback into the recommendation loop.",
        "real_world_context": "Tech companies like YouTube, Netflix, and Amazon use two-stage recommendation systems to balance search speed across massive catalogs with precise prediction accuracy.",
        "hints": [
            "A single complex model cannot score 10 million products in under 100 milliseconds.",
            "Stage 1 (Retrieval) uses fast, simple models (like collaborative filtering or dual-encoder vector search) to select the top 100-500 candidates.",
            "Stage 2 (Ranking) uses a deep neural network (like Deep & Cross Networks) with dense features to score the candidates."
        ],
        "solution": {
            "explanation": "We implement a two-stage recommendation pipeline. Stage 1: Retrieval. We use a dual-encoder model (user embeddings and item embeddings) in a vector database to perform approximate nearest-neighbor search, filtering 10 million items down to 500 candidates in under 10ms. Stage 2: Ranking. We pass these 500 candidates to a deep ranking model (e.g. DLRM) that incorporates real-time features (user's current session, device, time of day, item category matches). This model predicts click-through and purchase probabilities, sorting the final list for display.",
            "key_takeaways": [
                "Two-stage design resolves the speed vs accuracy trade-off in large recommendation spaces.",
                "Retrieval prioritizes high recall; ranking prioritizes high precision."
            ]
        },
        "evaluation_points": [
            "End-to-end system latency (<100ms)",
            "Candidate generation recall (retrieving the correct items)",
            "Ranking model accuracy (CTR, conversion rate metrics)",
            "Feature ingestion latency for real-time user signals"
        ],
        "follow_up_questions": [
            "How do you address the cold-start problem for new items that have no click history?",
            "Why is log transformation applied to numerical features in recommendation models?"
        ],
        "references": [
            {
                "title": "Deep Neural Networks for YouTube Recommendations",
                "url": "https://dl.acm.org/doi/10.1145/2959100.2959190"
            }
        ]
    })
    
    # Q99: Multimodal Search Engine
    questions.append({
        "id": 99,
        "slug": "multimodal-search-engine",
        "title": "Design a Multimodal Image-Text Search Engine",
        "section": "System Design",
        "difficulty": "Medium",
        "question_type": "system_design",
        "neuroforge_skill": "Machine Learning System Design",
        "estimated_time_minutes": 20,
        "tags": ["system-design", "multimodal", "clip", "vector-search"],
        "learning_objectives": [
            "Design a joint embedding space for visual and text search",
            "Optimize large-scale image feature extraction pipelines"
        ],
        "problem_statement": "Design a multimodal search engine that allows users to search a library of 50 million images using text queries ('dog running in park') or reference images. Detail: (1) how you train a joint embedding space, (2) your offline image ingestion and feature extraction pipeline, (3) how you index and search the vectors, and (4) how you keep vector index updates in sync with database modifications.",
        "real_world_context": "Multimodal search powers platforms like Pinterest, Google Photos, and e-commerce visual searches, enabling users to find visual assets using natural language queries.",
        "hints": [
            "Use a dual-encoder architecture like CLIP, trained on image-text pairs using contrastive loss to map both modalities to the same vector space.",
            "Offline ingestion: run image extraction jobs asynchronously using workers (e.g., Celery) to process images, generate vectors, and write to a vector index.",
            "Use a vector database with HNSW indexes for fast similarity search."
        ],
        "solution": {
            "explanation": "We use a pre-trained CLIP model to map images and text into a shared vector space. During ingestion, images are uploaded, processed asynchronously by workers to generate visual embeddings, and indexed in a vector database. To search, we embed the user's text query or image using the CLIP encoders, and run a nearest-neighbor search in the vector database. We use an event-driven system (CDC with Kafka) to sync vector index updates with database changes.",
            "key_takeaways": [
                "Contrastive pre-training maps different modalities (image and text) to a shared vector space.",
                "Asynchronous worker pipelines are essential to handle expensive image processing operations."
            ]
        },
        "evaluation_points": [
            "Cross-modal retrieval precision and recall",
            "Feature extraction throughput (images processed per second)",
            "Query vector lookup latency (<50ms)",
            "System reliability and recovery during database sync lag"
        ],
        "follow_up_questions": [
            "How do you handle NSFW content filtering at scale in a visual search pipeline?",
            "Why is contrastive loss used to train CLIP instead of standard classification loss?"
        ],
        "references": [
            {
                "title": "Learning Transferable Visual Models From Natural Language Supervision (CLIP)",
                "url": "https://arxiv.org/abs/2103.00020"
            }
        ]
    })
    
    # Q100: Agentic Customer Support System
    questions.append({
        "id": 100,
        "slug": "agentic-customer-support-system",
        "title": "Design an Agentic Customer Support System",
        "section": "System Design",
        "difficulty": "Hard",
        "question_type": "system_design",
        "neuroforge_skill": "Machine Learning System Design",
        "estimated_time_minutes": 30,
        "tags": ["system-design", "agents", "production-architecture", "safety"],
        "learning_objectives": [
            "Design a robust, multi-agent enterprise customer support system",
            "Implement safety guardrails, SLA monitoring, and fallback escalations"
        ],
        "problem_statement": "Design an enterprise multi-agent customer support system. The system must process thousands of incoming customer emails, route them to specialized agents (e.g. billing, tech support), interact with internal APIs to resolve issues, and draft responses. Detail: (1) your multi-agent architecture and graph orchestration, (2) how you manage conversation memory and user context across sessions, (3) how you implement safety guardrails to prevent jailbreaks and offensive outputs, and (4) your escalation path when agents fail or violate SLAs.",
        "real_world_context": "Automating enterprise customer support requires balancing high autonomy (resolving tickets without human intervention) with strict safety, SLA tracking, and fallback paths.",
        "hints": [
            "Use a hierarchical agent graph: a Router agent inspects the ticket and forwards it to specialized worker graphs.",
            "Store user state and session history in a database like PostgreSQL, loading it into the agent's context at the start of each run.",
            "Apply dual-layer guardrails: input checkers (e.g. LlamaGuard) to block prompt injections, and output validation rules to check tool calls and draft texts.",
            "Incorporate a queue (like RabbitMQ) to track ticket processing time. If an agent takes too long or fails, route the ticket to a human queue (Escalation)."
        ],
        "solution": {
            "explanation": "We design a hierarchical multi-agent graph system. Incoming emails are queued in RabbitMQ and routed by a Supervisor agent. Specialized worker sub-graphs (Billing, Tech Support) handle their respective tickets. The worker graphs use tools (e.g. database query, refund API) to resolve the issue. If the customer is angry or the action is high-risk (like issuing refunds over $100), the graph pauses for human approval. We apply LlamaGuard to check inputs for jailbreaks and output checkers to validate draft responses. An SLA monitor tracks execution times, escalating tickets to human representatives if timeouts occur.",
            "key_takeaways": [
                "Hierarchical agent graphs isolate tool sets, improving safety and reliability.",
                "Dual-layer guardrails (input/output) protect enterprise systems from malicious inputs and bad generations.",
                "Queues and SLA monitors ensure ticket resolution times are met, falling back to human support when needed."
            ]
        },
        "slate_points": [], # dummy for now, let's keep evaluation_points
        "evaluation_points": [
            "Ticket resolution rate without human intervention",
            "Customer satisfaction (CSAT) and response relevance",
            "End-to-end processing latency and SLA compliance",
            "System safety (rate of prompt injections or bad outputs blocked)"
        ],
        "follow_up_questions": [
            "How do you evaluate agent performance changes after modifying the system prompt?",
            "What database model would you use to store persistent conversation history and agent states?"
        ],
        "references": [
            {
                "title": "Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations",
                "url": "https://arxiv.org/abs/2312.06674"
            }
        ]
    })
    
    return questions
