def get_questions():
    questions = []
    
    # Q86: Agent Definition Loop
    questions.append({
        "id": 86,
        "slug": "agent-definition-loop",
        "title": "Build a ReAct Output Parser",
        "section": "Agents",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 10,
        "tags": ["agents", "react-pattern", "foundations"],
        "learning_objectives": [
            "Explain the Reasoning and Acting (ReAct) paradigm",
            "Implement a basic ReAct parser loop"
        ],
        "problem_statement": "Build a python function `parse_react_response(text)` that parses ReAct formatted text to extract keys like `Thought:`, `Action:`, `Action Input:`, and `Final Answer:`. Return a dictionary containing the parsed keys.",
        "real_world_context": "ReAct is the fundamental design pattern behind frameworks like LangChain and CrewAI, enabling models to interact with APIs and files to solve multi-step problems.",
        "hints": [
            "Use regular expressions to search for patterns like `Thought: (...)`, `Action: (...)`, and `Action Input: (...)`.",
            "If the model outputs `Final Answer: (...)`, the loop should terminate and return the result."
        ],
        "solution": {
            "explanation": "The ReAct paradigm prompts the LLM to generate both reasoning traces (Thought) and actions (calling tools). This combination helps the model plan, track progress, and handle unexpected observations. The agent loop parses the action request from the model's output, runs the corresponding tool, gets the result (Observation), feeds this observation back into the prompt, and repeats the cycle until a final answer is produced.",
            "key_takeaways": [
                "ReAct combines reasoning (thoughts) with execution actions in alternating cycles.",
                "Robust text parsing is required to extract structured API commands from free-form model text."
            ]
        },
        "starter_code": {
            "python": "import re\n\ndef parse_react_response(text):\n    # TODO: Parse 'Thought', 'Action', 'Action Input', or 'Final Answer'\n    # Return a dictionary containing the parsed fields\n    pass"
        },
        "expected_output": "A dictionary of parsed parameters or None if parsing fails.",
        "follow_up_questions": [
            "What happens to the agent loop if the LLM generates an invalid action name?",
            "How does the size of the prompt context grow at each iteration of the ReAct loop?"
        ],
        "references": [
            {
                "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
                "url": "https://arxiv.org/abs/2210.03629"
            }
        ]
    })
    
    # Q87: Execute a ReAct Loop [NEW]
    questions.append({
        "id": 87,
        "slug": "react-loop-executor",
        "title": "Build a ReAct Loop Executor",
        "section": "Agents",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 20,
        "tags": ["agents", "react-pattern", "execution-loop"],
        "learning_objectives": [
            "Build a core ReAct loop orchestrator",
            "Feed tool observations back into the agent context dynamically"
        ],
        "problem_statement": "Build an agent loop executor by implementing the python function `run_agent(question, available_tools, mock_llm, max_steps)`. The function should run the ReAct cycle (Thought -> Action -> Observation) iteratively, executing tools from the `available_tools` registry using the parsed action input, appending observations to the prompt context, and returning the final answer when the model outputs `Final Answer:`.",
        "real_world_context": "Understanding the core executor loop of an agent is crucial when customising execution flow, managing rate limits, or implementing custom logging in agent frameworks.",
        "hints": [
            "Use your `parse_react_response` logic or similar parsing to extract actions and final answers at each step.",
            "Append the model's output and the subsequent tool observation back onto the query history so the LLM receives the updated state in the next step.",
            "Ensure the loop does not run infinitely by capping execution at `max_steps`."
        ],
        "solution": {
            "explanation": "A ReAct executor loop manages the interaction between the LLM and the external environment. It constructs a prompt containing the tool specifications and user query, calls the LLM, parses the response for action calls, retrieves and invokes the requested tool, formats the tool output as an 'Observation', appends this observation to the chat context, and invokes the LLM again. The cycle halts when a 'Final Answer' is detected or execution step limit is reached.",
            "key_takeaways": [
                "The agent loop is responsible for state maintenance, prompt construction, and error recovery.",
                "Observations must be appended in chronological order to maintain correct logical context for the LLM."
            ]
        },
        "starter_code": {
            "python": "def run_agent(question, available_tools, mock_llm, max_steps=5):\n    # available_tools: dict of callable functions, e.g. {'calculate': calculate_fn}\n    # mock_llm: callable taking prompt string and returning LLM generation\n    # TODO: Run the ReAct loop: format prompt, call mock_llm, parse, run tool, append observation\n    pass"
        },
        "expected_output": "The final answer string extracted from the Final Answer block.",
        "follow_up_questions": [
            "How do you handle tool runtime exceptions within the execution loop?",
            "How can you optimize prompt token usage across multiple iterations of the loop?"
        ],
        "references": [
            {
                "title": "ReAct Paper",
                "url": "https://arxiv.org/abs/2210.03629"
            }
        ]
    })
    
    # Q88: Agent Memory
    questions.append({
        "id": 88,
        "slug": "agent-memory",
        "title": "Build a Sliding-Window Conversation Memory Manager",
        "section": "Agents",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 10,
        "tags": ["memory", "vector-databases", "context-management"],
        "learning_objectives": [
            "Contrast short-term conversational context with long-term episodic memory",
            "Implement a sliding-window conversational memory buffer"
        ],
        "problem_statement": "Build a python function `sliding_window_memory(messages, max_tokens, token_counter_fn)` that crops a list of chat messages (dicts with 'role' and 'content') to fit within `max_tokens` while guaranteeing that the system prompt (the first message in the list) is never pruned.",
        "real_world_context": "Long-running agent workflows require managing memory to avoid exceeding the model's context window. If the history grows too large, the agent slows down, costs more, and becomes less focused.",
        "hints": [
            "The system prompt (usually the first message) must always be preserved.",
            "Remove older user/assistant messages first, working backward from the most recent exchange.",
            "Sum the token counts of the system prompt and the kept messages to ensure the total is less than `max_tokens`."
        ],
        "solution": {
            "explanation": "Short-term memory stores the conversation history in the active prompt context window. This is limited by the model's context length. Long-term memory stores past conversations and facts in a vector database, retrieving them as needed using semantic search. For short-term memory, we use a sliding window or summarizer. A sliding window keeps the system prompt and drops older conversation turns when the token limit is approached, maintaining a stable context footprint.",
            "key_takeaways": [
                "Short-term memory resides in the context window; long-term memory is retrieved from external vector databases.",
                "Sliding windows trim history to prevent token overflow while preserving core system instructions."
            ]
        },
        "starter_code": {
            "python": "def sliding_window_memory(messages, max_tokens, token_counter_fn):\n    # messages: list of dict [{'role': '...', 'content': '...'}]\n    # TODO: Keep system message (first), and prune history from the oldest until sum <= max_tokens\n    pass"
        },
        "expected_output": "The pruned list of messages.",
        "follow_up_questions": [
            "How do 'semantic memory' differ from 'episodic memory' in agent architectures?",
            "What is the computational cost of summarizing conversation history compared to using a sliding window?"
        ],
        "references": [
            {
                "title": "LLM Powered Autonomous Agents (Lilian Weng)",
                "url": "https://lilianweng.github.io/posts/2023-06-23-agent/"
            }
        ]
    })

    # Q89: Tool Calling & Function Calling
    questions.append({
        "id": 89,
        "slug": "tool-calling-function-calling",
        "title": "Build a JSON Schema Tool Validator",
        "section": "Agents",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 15,
        "tags": ["tool-calling", "json-schema", "validation"],
        "learning_objectives": [
            "Define tool schemas in JSON Schema format",
            "Validate model arguments against a JSON Schema before execution"
        ],
        "problem_statement": "Build a python function `validate_and_execute_tool(arguments_json_str, schema, execution_fn)` that parses a JSON string of arguments generated by a model, validates it against a target JSON schema dictionary checking required fields and parameter types, and executes `execution_fn` with the parsed arguments.",
        "real_world_context": "Modern LLM APIs (like OpenAI function calling) output JSON arguments. Pre-validating these inputs protects your internal database and APIs from malformed queries or SQL injection attacks.",
        "hints": [
            "Use `json.loads` to convert the string to a python dictionary.",
            "Use the `jsonschema` library or write a custom validator checking for required keys and parameter types.",
            "Handle JSON decoding errors gracefully and return them as feedback to the agent."
        ],
        "solution": {
            "explanation": "Function calling allows LLMs to interact with external APIs. The model is provided with JSON schemas describing the available functions. The model outputs a JSON string containing the arguments it wants to pass. Since the model output is not guaranteed to be valid JSON or match the schema, we must parse and validate it before execution to ensure system safety and stability.",
            "key_takeaways": [
                "Function calling prompts the model to output structured JSON arguments instead of free text.",
                "Pre-execution schema validation protects downstream APIs from errors and injection attacks."
            ]
        },
        "starter_code": {
            "python": "import json\n\ndef validate_and_execute_tool(arguments_json_str, schema, execution_fn):\n    # schema: dict representing expected JSON schema\n    # TODO: Parse, validate against schema, and call execution_fn(parsed_args)\n    pass"
        },
        "expected_output": "The output value of execution_fn or a validation error message.",
        "follow_up_questions": [
            "How does native function calling differ from simple ReAct text parsing?",
            "What is the best way to return tool execution errors back to the model?"
        ],
        "references": [
            {
                "title": "OpenAI Function Calling Guide",
                "url": "https://platform.openai.com/docs/guides/function-calling"
            }
        ]
    })

    # Q90: State Management Graphs
    questions.append({
        "id": 90,
        "slug": "state-management-graphs",
        "title": "Build a Stateful Agent Graph Router",
        "section": "Agents",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 20,
        "tags": ["state-management", "graphs", "langgraph"],
        "learning_objectives": [
            "Design agent workflows as state machines using directed graphs",
            "Implement a state update and conditional routing node"
        ],
        "problem_statement": "Build a state graph execution manager class `SimpleAgentGraph` that registers nodes (functions taking and returning state dictionary) and conditional edge routers, and runs an execution loop starting from an initial state until a terminating state is reached.",
        "real_world_context": "Complex enterprise workflows (like multi-step document audits or code generation with tests) are fragile when run in simple loops. Directed acyclic graphs (DAGs) like LangGraph provide control and reliability.",
        "hints": [
            "Define nodes as callable functions that accept the state dict and return updates.",
            "The graph runner loops, executing the current node, updating the shared state, and checking the routing function to find the next node.",
            "The loop continues until it reaches an designated end state."
        ],
        "solution": {
            "explanation": "Modeling workflows as state graphs allows developers to define structured, predictable execution paths. Nodes represent functional steps (e.g. LLM call, tool execution), while edges represent transition rules. Conditional edges (routers) evaluate the current state to choose the next node. This approach provides fine-grained control, making it easy to implement loops, fallback steps, and human-in-the-loop approvals that are difficult to manage in free-form ReAct loops.",
            "key_takeaways": [
                "Agent graphs model workflows as state machines, improving control and reliability.",
                "Shared state dicts aggregate updates across nodes, serving as a unified database for the run."
            ]
        },
        "starter_code": {
            "python": "class SimpleAgentGraph:\n    def __init__(self):\n        self.nodes = {}\n        self.edges = {} # node -> router_fn\n        \n    def add_node(self, name, func):\n        self.nodes[name] = func\n        \n    def add_conditional_edges(self, source, router_fn):\n        self.edges[source] = router_fn\n        \n    def execute(self, initial_state):\n        # TODO: Run the graph loop, executing nodes and routing dynamically\n        pass"
        },
        "expected_output": "The final state dictionary after the graph reaches 'end'.",
        "follow_up_questions": [
            "How do state graphs enable cycles (loops) compared to standard pipeline orchestrators?",
            "What is the role of a state schema in validating graph updates?"
        ],
        "references": [
            {
                "title": "LangGraph State Graph Concepts",
                "url": "https://langchainai.github.io/langgraph/concepts/"
            }
        ]
    })

    # Q91: Agent Planning & Reflection
    questions.append({
        "id": 91,
        "slug": "agent-planning-reflection",
        "title": "Build a Self-Correction Reflection Loop",
        "section": "Agents",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 15,
        "tags": ["planning", "reflection", "self-correction"],
        "learning_objectives": [
            "Explain task planning decomposition (Tree of Thoughts)",
            "Implement a reflection node that reviews and self-corrects prior outputs"
        ],
        "problem_statement": "Build a python function `reflection_loop(task, mock_generator_fn, mock_critic_fn, max_steps)` that implements a generation-evaluation cycle: the generator produces a draft, the critic evaluates it to generate critiques, and the generator revises the draft based on the feedback.",
        "real_world_context": "When generating code, the initial draft often contains syntax errors or edge-case bugs. An agent that runs the code in a sandbox, catches errors, and reflects on them can correct its own bugs before returning the output.",
        "hints": [
            "The generator LLM creates the draft.",
            "The critic LLM reviews the draft against instructions, highlighting weaknesses or errors.",
            "Feed the draft and critique back to the generator, requesting a revised version."
        ],
        "solution": {
            "explanation": "LLMs predict tokens sequentially without looking ahead, which can lead to early reasoning mistakes that ruin the rest of the generation. Reflection prompts break the task into two steps: generation and evaluation. The critic evaluates the draft, and the generator uses this feedback to correct its work. This self-correction loop mimics human revision, leading to much higher quality outputs for complex coding and reasoning tasks.",
            "key_takeaways": [
                "Reflection separates creation from critique, reducing single-pass logical errors.",
                "Criticism feedback acts as dynamic prompt context that guides self-correction."
            ]
        },
        "starter_code": {
            "python": "def reflection_loop(task, mock_generator_fn, mock_critic_fn, max_steps=2):\n    # TODO: Implement generate -> critique -> regenerate loop\n    pass"
        },
        "expected_output": "The final corrected output string.",
        "follow_up_questions": [
            "How does Reflexion differ from simple Chain-of-Thought?",
            "What is the risk of the critic introducing false corrections (over-critiquing)?"
        ],
        "references": [
            {
                "title": "Reflexion: Language Agents with Systematic Self-Reflection",
                "url": "https://arxiv.org/abs/2303.11366"
            }
        ]
    })

    # Q92: Multi-Agent Orchestration
    questions.append({
        "id": 92,
        "slug": "multi-agent-orchestration",
        "title": "Build a Multi-Agent Supervisor Router",
        "section": "Agents",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 20,
        "tags": ["multi-agent", "orchestration", "collaboration"],
        "learning_objectives": [
            "Compare hierarchical (supervisor-worker) and peer-to-peer agent architectures",
            "Implement a central router that delegates tasks to specialized workers"
        ],
        "problem_statement": "Build a hierarchical multi-agent router function `orchestrate_agents(task, mock_supervisor_fn, worker_dict)` that takes a master task, invokes a supervisor agent to delegate work to specialized worker agents in `worker_dict`, and aggregates their responses.",
        "real_world_context": "A single agent with 50 tools struggles with focus and instruction drift. Splitting the task across multiple agents (e.g. a Writer agent, a Researcher agent, and a Coder agent) improves overall system reliability.",
        "hints": [
            "The supervisor receives the task, decides which specialized worker to call (e.g., 'researcher'), and passes the sub-task.",
            "The worker processes the sub-task and returns its output to the supervisor.",
            "The supervisor evaluates the worker's output to decide if the task is complete or requires further delegation."
        ],
        "solution": {
            "explanation": "Hierarchical multi-agent systems use a central supervisor agent to route sub-tasks to specialized worker agents, maintaining control. Peer-to-peer systems allow agents to communicate directly with each other, which is more flexible but harder to debug. Splitting responsibilities reduces the number of tools and instructions each agent has to handle, reducing context dilution and improving reliability.",
            "key_takeaways": [
                "Hierarchical orchestration uses a supervisor to delegate and aggregate worker outputs.",
                "Splitting tasks across specialized agents reduces tool confusion and instruction drift."
            ]
        },
        "starter_code": {
            "python": "def orchestrate_agents(task, mock_supervisor_fn, worker_dict):\n    # worker_dict: dict of specialized callable functions {'researcher': fn, 'writer': fn}\n    # TODO: Route tasks, invoke worker, and return response\n    pass"
        },
        "expected_output": "The final combined result from the multi-agent execution.",
        "follow_up_questions": [
            "How do multi-agent systems handle message-passing and state synchronization?",
            "What is the risk of infinite loops in peer-to-peer agent conversations?"
        ],
        "references": [
            {
                "title": "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation",
                "url": "https://arxiv.org/abs/2308.08155"
            }
        ]
    })

    # Q93: Agentic Error Handling & Fallbacks
    questions.append({
        "id": 93,
        "slug": "error-handling-fallback",
        "title": "Build a Self-Healing Code Execution Loop",
        "section": "Agents",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 20,
        "tags": ["error-handling", "fallbacks", "self-healing"],
        "learning_objectives": [
            "Implement self-healing agent error catch blocks",
            "Feed compiler and runtime execution error stacktraces back to the LLM for correction"
        ],
        "problem_statement": "Build a python function `execute_with_self_healing(code_to_run, mock_corrector_llm, max_retries)` that executes python code dynamically using `exec()`. If execution raises an exception, capture the traceback stacktrace and pass it back to the corrector LLM to generate corrected code, retrying until success or maximum retries are reached.",
        "real_world_context": "Code interpreters (like Advanced Data Analysis in ChatGPT) rely on self-healing loops. If generated Python code fails to run due to a missing library or runtime typo, the agent reads the error log and fixes the code automatically.",
        "hints": [
            "Use Python's `exec()` inside a `try...except` block.",
            "Use `traceback.format_exc()` to extract the traceback string.",
            "Pass the exact traceback error back to the LLM: 'Your code failed with this error: [Error]. Please write the corrected code block.'"
        ],
        "solution": {
            "explanation": "Standard software raises exceptions and halts on execution errors. Agentic self-healing wraps execution in a retry loop. If an error occurs, the stacktrace is caught and sent back to the LLM as feedback. The model reads the error context (e.g. NameError or TypeError) and generates a corrected version. This allows agents to recover from minor typos, formatting bugs, or API shifts autonomously.",
            "key_takeaways": [
                "Self-healing loops use execution errors as feedback prompts to guide corrections.",
                "Wrapping dynamic code executions in try-except blocks is essential to prevent system crashes."
            ]
        },
        "starter_code": {
            "python": "import traceback\n\ndef execute_with_self_healing(code_to_run, mock_corrector_llm, max_retries=3):\n    # TODO: Implement exec loop with try-except, routing stacktraces back to mock_corrector_llm\n    pass"
        },
        "expected_output": "A dictionary containing the execution output or final error log.",
        "follow_up_questions": [
            "What security risks are associated with using `exec()` on code generated by an LLM?",
            "How do you restrict resource usage (CPU/memory) when running code generated by an agent?"
        ],
        "references": [
            {
                "title": "Self-Debugging Code Generation (Google DeepMind)",
                "url": "https://arxiv.org/abs/2304.05128"
            }
        ]
    })

    # Q94: Agentic RAG Routing
    questions.append({
        "id": 94,
        "slug": "agentic-rag-routing",
        "title": "Build an Adaptive Agentic RAG Router",
        "section": "Agents",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 25,
        "tags": ["agentic-rag", "routing", "self-grading"],
        "learning_objectives": [
            "Implement an adaptive routing layer for incoming user queries",
            "Build a self-grading RAG loop that evaluates retrieved documents before generating answers"
        ],
        "problem_statement": "Build an adaptive Agentic RAG loop by writing a python function `agentic_rag_loop(query, mock_router_fn, vector_retriever, web_searcher, mock_grader_fn, generator_fn)` that: (1) routes query requests dynamically to vector search or web search, (2) retrieves documents, (3) grades retrieved context relevance, and (4) falls back to web search if the vector retrieve context is graded as irrelevant.",
        "real_world_context": "If a user query asks for real-time information ('What was Tesla's stock price today?'), a standard vector search fails because the database is static. Agentic routing directs the query to a web search tool instead.",
        "hints": [
            "First step: use the router LLM to classify the query type ('static' vs 'real-time').",
            "Second step: retrieve documents using the selected tool.",
            "Third step: use the grader LLM to verify if the retrieved documents contain information to answer the query. If not, trigger re-retrieval with an expanded query."
        ],
        "solution": {
            "explanation": "Agentic RAG adds decision-making layers to the retrieval process. A routing layer inspects the query to select the best source (e.g. vector index, sql database, or web search). A self-grading layer evaluates the retrieved documents for relevance before generation. If the context is graded as insufficient, the agent corrects its search query and tries again, avoiding hallucinations caused by poor retrieval context.",
            "key_takeaways": [
                "Agentic RAG uses routers to dynamically select the best data source for a query.",
                "Self-grading filters out irrelevant documents and triggers re-retrieval if necessary, reducing hallucinations."
            ]
        },
        "starter_code": {
            "python": "def agentic_rag_loop(query, mock_router_fn, vector_retriever, web_searcher, mock_grader_fn, generator_fn):\n    # TODO: Route query, retrieve context, grade relevance, fallback to search if needed, and generate answer\n    pass"
        },
        "expected_output": "The generated answer grounded in the graded context.",
        "follow_up_questions": [
            "How does Corrective RAG (CRAG) handle cases where both vector database and web search fail?",
            "What is the latency trade-off of running self-grading loops compared to Naive RAG?"
        ],
        "references": [
            {
                "title": "Corrective Retrieval-Augmented Generation",
                "url": "https://arxiv.org/abs/2401.15884"
            }
        ]
    })

    # Q95: Autonomous Web Browsing & RPA
    questions.append({
        "id": 95,
        "slug": "autonomous-web-browsing-rpa",
        "title": "Build an Autonomous DOM Pruning Web Agent",
        "section": "Agents",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "AI Agent Engineering",
        "estimated_time_minutes": 25,
        "tags": ["web-agents", "rpa", "dom-parsing"],
        "learning_objectives": [
            "Explain the challenges web agents face with large DOM trees and dynamic selectors",
            "Implement a DOM pruning utility to fit within context windows"
        ],
        "problem_statement": "Build a DOM pruning utility for web navigation agents by writing a python function `prune_dom_tree(raw_html)` that parses an HTML string using BeautifulSoup, filters for only interactive tags (`<a>`, `<button>`, `<input>`), and retains key locator attributes while stripping layout clutter to minimize token usage.",
        "real_world_context": "AI agents that book flights, purchase products, or fill out web forms must navigate complex, dynamic web pages. Pruning the DOM is essential to fit page structures within the model's context window.",
        "hints": [
            "Raw HTML pages can be hundreds of kilobytes, exceeding model context limits.",
            "Use `BeautifulSoup` to parse the HTML string and extract elements that have user interaction handlers or specific tags.",
            "Retain attributes like `id`, `class`, `href`, and `placeholder` while stripping scripts, styles, and inline SVG assets."
        ],
        "solution": {
            "explanation": "Raw HTML pages are too large and noisy for LLM context windows. Web agents solve this by using accessibility trees or pruned DOM trees, which focus on interactive elements. Dynamic websites generate randomized class names (e.g. Tailwind/CSS-in-JS), causing hardcoded selectors to break. Self-healing selectors use LLMs to match elements based on semantic descriptors (e.g., 'the checkout button') rather than absolute class paths, making web interaction robust to page updates.",
            "key_takeaways": [
                "Pruning DOM trees reduces token counts by filtering out non-interactive layout code.",
                "Self-healing selectors use semantic matching to locate elements when class names change."
            ]
        },
        "starter_code": {
            "python": "from bs4 import BeautifulSoup\n\ndef prune_dom_tree(raw_html):\n    # TODO: Parse HTML, filter for interactive elements, and return clean structural representations\n    pass"
        },
        "expected_output": "A clean, compact string containing only interactive HTML elements.",
        "follow_up_questions": [
            "Why is the browser accessibility tree preferred over raw HTML for web agents?",
            "How do vision-language models (VLMs) assist agents in navigations via screen coordinate click maps?"
        ],
        "references": [
            {
                "title": "WebArena: A Realistic Web Agent Benchmark",
                "url": "https://arxiv.org/abs/2307.13854"
            }
        ]
    })
    
    return questions
