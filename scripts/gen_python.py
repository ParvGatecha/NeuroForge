def get_questions():
    questions = []
    
    # Q1: List Comprehensions vs Generators
    questions.append({
        "id": 1,
        "slug": "list-comprehensions-generators",
        "title": "Build a Memory Benchmarker for Lists vs Generators",
        "section": "Python",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 10,
        "tags": ["memory-optimization", "generators", "list-comprehensions"],
        "learning_objectives": [
            "Implement a memory comparison benchmark between list comprehensions and generators",
            "Identify lazy evaluation in Python"
        ],
        "problem_statement": "Build a python function `evaluate_memory_usage()` that programmatically measures and returns the memory allocation in bytes of a list comprehension containing one million integers vs a generator expression generating the same sequence. Use the `sys` module.",
        "real_world_context": "When processing huge text datasets or parsing large server logs, loading everything into memory at once can crash the container. Using generators allows streaming logs row-by-row, keeping memory consumption constant.",
        "hints": [
            "A list comprehension uses square brackets `[]` and allocates memory immediately.",
            "A generator expression uses parentheses `()` and yields items lazily on demand.",
            "Use the `sys.getsizeof()` function to check the size in bytes of both objects."
        ],
        "solution": {
            "explanation": "List comprehensions create the entire list in memory when called, requiring memory proportional to the length of the list (O(N)). Generators, on the other hand, return a generator object that produces items one-by-one as requested (lazy evaluation), maintaining an O(1) memory footprint regardless of sequence size.",
            "key_takeaways": [
                "List comprehensions are eager and consume memory proportional to sequence length.",
                "Generators are lazy and maintain a constant, minimal memory overhead."
            ]
        },
        "starter_code": {
            "python": "import sys\n\ndef evaluate_memory_usage():\n    # TODO: Build a list comprehension and a generator expression for numbers 0 to 999999\n    # and return their sizes in a tuple: (list_size_bytes, gen_size_bytes)\n    list_comp = []\n    gen_expr = None\n    return sys.getsizeof(list_comp), sys.getsizeof(gen_expr)"
        },
        "expected_output": "A tuple containing: (the memory size in bytes of the list, which will be ~8MB, and the memory size of the generator, which will be under 200 bytes).",
        "follow_up_questions": [
            "What happens if you convert a generator to a list using `list(gen_expr)`?",
            "Can you iterate over a generator expression multiple times? Why or why not?"
        ],
        "references": [
            {
                "title": "Python Generators Wiki",
                "url": "https://wiki.python.org/moin/Generators"
            }
        ]
    })
    
    # Q2: Decorators
    questions.append({
        "id": 2,
        "slug": "decorators-timing",
        "title": "Build a Timing Decorator",
        "section": "Python",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 15,
        "tags": ["decorators", "functional-programming", "logging"],
        "learning_objectives": [
            "Build a reusable wrapper function that measures runtime",
            "Preserve original function metadata using functools.wraps"
        ],
        "problem_statement": "Build a decorator `@time_it` that measures the execution time of any function it decorates. The decorator should print the execution time in seconds and return the result of the decorated function. Make sure to preserve the name and docstring of the original function.",
        "real_world_context": "Decorators are widely used in frameworks like Flask or FastAPI for request logging, authentication checks, and database session management without repeating code in every endpoint.",
        "hints": [
            "Use `time.perf_counter()` or `time.time()` to measure exact duration.",
            "Import and use `functools.wraps` on the inner wrapper function to preserve original function metadata.",
            "The wrapper function must accept `*args` and `**kwargs` to support any function signature."
        ],
        "solution": {
            "explanation": "A decorator is a function that takes another function as an argument, adds some functionality, and returns a new function. Using `functools.wraps` is crucial to prevent the decorated function's `__name__` and `__doc__` from being replaced by the wrapper's details, which would break debugging and introspection tools.",
            "key_takeaways": [
                "Decorators modify function behavior dynamically without altering the original code.",
                "Always use `functools.wraps` to prevent loss of function metadata."
            ]
        },
        "starter_code": {
            "python": "import time\nfrom functools import wraps\n\ndef time_it(func):\n    # TODO: Build the decorator wrapper\n    pass\n\n@time_it\ndef compute_heavy_sum(n):\n    \"\"\"Computes sum of numbers up to n.\"\"\"\n    return sum(range(n))"
        },
        "expected_output": "The function executes, logs duration to console, and returns the correct sum.",
        "follow_up_questions": [
            "How do you pass arguments to a decorator itself (e.g. `@time_it(precision=3)`)?",
            "What is the execution order when stacking multiple decorators on a single function?"
        ],
        "references": [
            {
                "title": "Python Decorators Guide",
                "url": "https://realpython.com/primer-on-python-decorators/"
            }
        ]
    })

    # Q3: Args and Kwargs Unpacking
    questions.append({
        "id": 3,
        "slug": "args-kwargs-unpacking",
        "title": "Build a Dynamic Argument Forwarder",
        "section": "Python",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 10,
        "tags": ["arguments", "syntax", "unpacking"],
        "learning_objectives": [
            "Build functions with variable-length signatures using *args and **kwargs",
            "Perform dictionary and list unpacking for argument dispatching"
        ],
        "problem_statement": "Build a function `forward_arguments(target_func, *args, **kwargs)` that logs all positional arguments and keyword arguments to the console, and then forwards them exactly to `target_func`, returning its output. Show how to unpack a list `l = [1, 2]` and a dict `d = {'c': 3}` into a function `foo(a, b, c)`.",
        "real_world_context": "This pattern is essential in building API client wrappers, custom print utilities, or logging proxies where the wrapper function does not know the specific parameters of the target function ahead of time.",
        "hints": [
            "Use `*args` to capture extra positional arguments as a tuple.",
            "Use `**kwargs` to capture extra keyword arguments as a dictionary.",
            "Forward them using `target_func(*args, **kwargs)`."
        ],
        "solution": {
            "explanation": "In Python, `*args` inside a function parameter list packs extra positional arguments into a tuple. `**kwargs` packs keyword arguments into a dictionary. When calling a function, prefixing a sequence with `*` unpacks it as positional arguments, and a dictionary with `**` unpacks it as keyword arguments.",
            "key_takeaways": [
                "`*args` handles variable positional arguments, `**kwargs` handles keyword arguments.",
                "Unpacking allows passing collections directly to match individual parameters."
            ]
        },
        "starter_code": {
            "python": "def forward_arguments(target_func, *args, **kwargs):\n    # TODO: Log parameters to console and call target_func\n    pass"
        },
        "expected_output": "The wrapped function executes correctly and returns the target function value.",
        "follow_up_questions": [
            "What happens if you define a function signature like `def foo(*args, a)`? How do you call it?",
            "Can you have keyword-only arguments in Python?"
        ],
        "references": [
            {
                "title": "Python Arguments Tutorial",
                "url": "https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions"
            }
        ]
    })

    # Q4: Context Managers
    questions.append({
        "id": 4,
        "slug": "context-managers-cleanup",
        "title": "Build a Resource Cleanup Context Manager",
        "section": "Python",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 15,
        "tags": ["context-managers", "resource-cleanup", "exception-handling"],
        "learning_objectives": [
            "Build class-based and generator-based context managers",
            "Perform suppression of targeted exception classes"
        ],
        "problem_statement": "Build a class-based context manager `DatabaseConnection` that simulates connecting to a database. The `__enter__` method should return the connection instance (self) and print 'Connected'. The `__exit__` method must handle exceptions, print 'Disconnected', and suppress specific database-connection exceptions (e.g. ValueError) by returning True. Also, build the equivalent context manager using `@contextlib.contextmanager`.",
        "real_world_context": "Managing file handles, database connections, socket interfaces, and TensorFlow sessions requires deterministic cleanup. If an exception occurs, the socket must still close to avoid connection leaks.",
        "hints": [
            "The `__exit__` method accepts four arguments: self, exc_type, exc_val, exc_tb.",
            "Returning `True` from `__exit__` suppresses exceptions; returning `False` or `None` propagates them.",
            "In `@contextlib.contextmanager`, wrap the yield statement in a `try...finally` block to guarantee cleanup."
        ],
        "solution": {
            "explanation": "Context managers implement `__enter__` and `__exit__`. In case of errors, the `__exit__` method receives exception details. If it returns `True`, Python suppresses the exception, allowing execution to continue. If using `contextlib`, the generator yields control to the `with` block, and the `finally` block handles cleanup, which is executed even if exceptions are raised inside the `with` block.",
            "key_takeaways": [
                "Context managers automate setup and teardown operations.",
                "Exceptions inside a with-block are routed directly to the exit handler."
            ]
        },
        "starter_code": {
            "python": "from contextlib import contextmanager\n\nclass DatabaseConnection:\n    # TODO: Build __enter__ and __exit__\n    pass\n\n@contextmanager\ndef db_connection_generator():\n    # TODO: Build using contextlib generator style\n    pass"
        },
        "expected_output": "The connection is established, logs connection, and safely disconnects even when ValueError is raised.",
        "follow_up_questions": [
            "What is the difference between returning True and returning False in __exit__?",
            "What happens if an exception is raised inside the __enter__ method?"
        ],
        "references": [
            {
                "title": "Python contextlib documentation",
                "url": "https://docs.python.org/3/library/contextlib.html"
            }
        ]
    })

    # Q5: Dunder Methods
    questions.append({
        "id": 5,
        "slug": "dunder-methods-custom-collection",
        "title": "Build a Vector2D Class with Dunder Methods",
        "section": "Python",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 20,
        "tags": ["oop", "dunder-methods", "magic-methods"],
        "learning_objectives": [
            "Build custom classes that implement standard mathematical operators",
            "Customize representation string methods for developers and users"
        ],
        "problem_statement": "Build a class `Vector2D` that represents a mathematical 2D vector. Implement magic (dunder) methods for: vector addition (`+`), length of vector (`len()`), checking vector magnitude comparison (`<`, `==`), customized indexing (`v[0]` returns x, `v[1]` returns y), and clear representation for string casting (`__str__`) and developer debugging (`__repr__`).",
        "real_world_context": "Creating intuitive APIs in PyTorch or NumPy relies heavily on operator overloading. For example, `tensor1 + tensor2` calls `__add__` to perform element-wise tensor addition.",
        "hints": [
            "Implement `__add__` for vector addition.",
            "Use `math.hypot(x, y)` to calculate magnitude.",
            "`__repr__` should return a string that looks like valid Python code to recreate the object."
        ],
        "solution": {
            "explanation": "Python's data model utilizes dunder methods to hook custom classes into built-in operators. `__repr__` should provide an unambiguous string representation suitable for developers, while `__str__` is for end-user readability. `__getitem__` enables container-like index access, making user-defined classes feel like native types.",
            "key_takeaways": [
                "Dunder methods allow custom objects to integrate with native operators.",
                "__repr__ is for developers (debugging); __str__ is for end-users."
            ]
        },
        "starter_code": {
            "python": "import math\n\nclass Vector2D:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n        \n    # TODO: Build dunder methods\n    # __add__, __len__, __lt__, __eq__, __getitem__, __str__, __repr__"
        },
        "expected_output": "Vectors add correctly, compare magnitudes, support indexing, and display debugging representations.",
        "follow_up_questions": [
            "What is the difference between `__len__` returning float and integer in Python?",
            "How would you implement subtraction (`__sub__`) and scalar multiplication (`__mul__`)?"
        ],
        "references": [
            {
                "title": "Python Data Model Reference",
                "url": "https://docs.python.org/3/reference/datamodel.html"
            }
        ]
    })

    # Q6: Custom Iterators
    questions.append({
        "id": 6,
        "slug": "custom-iterators-fibonacci",
        "title": "Build a Custom Sequence Iterator",
        "section": "Python",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 15,
        "tags": ["iterators", "protocols", "generators"],
        "learning_objectives": [
            "Build iterators implementing the Iterator Protocol",
            "Differentiate between iterables and iterators"
        ],
        "problem_statement": "Build a custom class-based iterator `FibonacciIterator` that generates Fibonacci numbers up to a specified limit. The class must implement `__iter__` and `__next__` and raise `StopIteration` when the limit is exceeded. It should not compute values ahead of time.",
        "real_world_context": "Custom iterators are useful when traversing graphs, walking file trees, or iterating over database query paginations where loading all records into memory at once is not feasible.",
        "hints": [
            "`__iter__` should return the iterator object itself (usually `self`).",
            "`__next__` should update internal state (calculating the next Fibonacci number) and return the current one.",
            "Make sure to raise `StopIteration` when the computed value exceeds the specified limit."
        ],
        "solution": {
            "explanation": "To create a custom iterator, a class must implement two methods: `__iter__`, which returns the iterator object, and `__next__`, which returns the next value in the sequence. Raising `StopIteration` signals to loop constructs (like `for` loops) that iteration has finished. A key distinction is that an iterable has an `__iter__` method returning an iterator, while the iterator must have both `__iter__` and `__next__`.",
            "key_takeaways": [
                "The iterator protocol requires __iter__ and __next__ implementation.",
                "StopIteration controls loop exits gracefully."
            ]
        },
        "starter_code": {
            "python": "class FibonacciIterator:\n    def __init__(self, limit):\n        self.limit = limit\n        # TODO: Initialize tracking states\n        \n    def __iter__(self):\n        return self\n        \n    def __next__(self):\n        # TODO: Compute next value or raise StopIteration\n        pass"
        },
        "expected_output": "Iterating over FibonacciIterator(10) yields 0, 1, 1, 2, 3, 5, 8.",
        "follow_up_questions": [
            "Why does an iterator return self in its `__iter__` method?",
            "What happens if you try to loop over the same iterator instance twice?"
        ],
        "references": [
            {
                "title": "Python Iterator Types documentation",
                "url": "https://docs.python.org/3/library/stdtypes.html#iterator-types"
            }
        ]
    })

    # Q7: Threading vs Multiprocessing
    questions.append({
        "id": 7,
        "slug": "threading-vs-multiprocessing",
        "title": "Build a Thread vs Process Task Runner",
        "section": "Python",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 20,
        "tags": ["concurrency", "multiprocessing", "threading", "gil"],
        "learning_objectives": [
            "Build a benchmarking tool to verify threading vs multiprocessing under the GIL",
            "Select the correct module based on whether a task is CPU-bound or I/O-bound"
        ],
        "problem_statement": "Build a Python utility function `run_concurrent_tasks(task_fn, args_list, mode)` that executes a list of tasks using either a ThreadPoolExecutor or ProcessPoolExecutor depending on the mode ('thread' vs 'process'). Benchmarks a CPU-bound task (heavy math) using both modes to prove which yields speedups under the GIL.",
        "real_world_context": "Data processing and augmentation pipelines (like image rotation or tokenization) are CPU-bound and require multiprocessing. In contrast, scraper pipelines downloading web pages are I/O-bound and run efficiently with threads or async networks.",
        "hints": [
            "CPython has a Global Interpreter Lock (GIL) that prevents multiple native threads from executing Python bytecodes at once.",
            "For CPU-bound tasks, threads fight for the GIL, adding overhead. Processes bypass this by spawning independent Python interpreters.",
            "Use `concurrent.futures` module for high-level pool implementations."
        ],
        "solution": {
            "explanation": "Because CPython's execution is protected by the Global Interpreter Lock (GIL), only one thread can execute Python bytecode at a time. Therefore, multi-threading on CPU-bound tasks cannot achieve true parallelism and often degrades performance due to context-switching overhead. Multiprocessing runs separate processes with separate memory spaces and separate GIL instances, achieving true multi-core CPU utilization. For I/O-bound operations, threads release the GIL while waiting for I/O, providing concurrency without process startup overhead.",
            "key_takeaways": [
                "CPU-bound tasks require multiprocessing to leverage multiple CPU cores in Python.",
                "I/O-bound tasks are suited for threading or asyncio as the GIL is released during wait states."
            ]
        },
        "starter_code": {
            "python": "import time\nfrom concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor\n\ndef run_concurrent_tasks(task_fn, args_list, mode='thread'):\n    # TODO: Build pool launcher based on mode and return execution duration\n    pass"
        },
        "expected_output": "The time duration in seconds representing the benchmark run.",
        "follow_up_questions": [
            "Does the GIL affect other implementations of Python like Jython or IronPython?",
            "How does sharing memory work in threading vs multiprocessing?"
        ],
        "references": [
            {
                "title": "What is the Python Global Interpreter Lock (GIL)?",
                "url": "https://realpython.com/python-gil/"
            }
        ]
    })

    # Q8: Asyncio Event Loops
    questions.append({
        "id": 8,
        "slug": "asyncio-event-loops",
        "title": "Build a Concurrent Async Data Fetcher",
        "section": "Python",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 20,
        "tags": ["asyncio", "asynchronous", "concurrency"],
        "learning_objectives": [
            "Build asynchronous cooperative multitasking workflows",
            "Collect and handle concurrent task exceptions using asyncio.gather"
        ],
        "problem_statement": "Build an asynchronous function `fetch_data_from_sources(sources)` where `sources` is a list of API URLs. Simulate a network request delay for each source using `asyncio.sleep()`. Use `asyncio.gather()` to fetch data from all sources concurrently, ensuring that if any request fails, the others are not interrupted but their exceptions are logged.",
        "real_world_context": "High-performance API gateways built with FastAPI handle thousands of concurrent client connections by yielding control during database and external API requests, resulting in extremely high throughput.",
        "hints": [
            "Use `async def` to declare asynchronous functions (coroutines).",
            "Use `await asyncio.sleep(duration)` instead of `time.sleep()` to avoid blocking the event loop.",
            "Pass `return_exceptions=True` to `asyncio.gather()` to capture failures without terminating the entire list."
        ],
        "solution": {
            "explanation": "In asyncio, cooperative multitasking is managed by a single-threaded event loop. When a coroutine awaits an I/O operation (like `asyncio.sleep` or a network socket read), it yields control back to the event loop, allowing other coroutines to execute. `asyncio.gather` wraps these coroutines into tasks and schedules them concurrently. Setting `return_exceptions=True` ensures that failed operations return their exception objects as items in the results list rather than raising them immediately and aborting.",
            "key_takeaways": [
                "asyncio runs on a single thread and achieves concurrency through cooperative multitasking.",
                "Awaiting blocking synchronous functions (like time.sleep) blocks the entire event loop, defeating async benefits."
            ]
        },
        "starter_code": {
            "python": "import asyncio\n\nasync def fetch_source(name, delay, fail=False):\n    # TODO: Simulate data fetching\n    pass\n\nasync def fetch_data_from_sources(sources):\n    # TODO: Build asynchronous concurrent gather execution\n    pass"
        },
        "expected_output": "Fetches execute concurrently, completing in max(delay) time, and failures are returned in the result list.",
        "follow_up_questions": [
            "What happens if you call a standard synchronous blocking function inside an async function?",
            "What is the difference between `asyncio.gather` and `asyncio.as_completed`?"
        ],
        "references": [
            {
                "title": "Python asyncio Documentation",
                "url": "https://docs.python.org/3/library/asyncio.html"
            }
        ]
    })

    # Q9: Metaclasses
    questions.append({
        "id": 9,
        "slug": "metaclasses-validation",
        "title": "Build a Metaclass Class Validator",
        "section": "Python",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 25,
        "tags": ["metaclasses", "advanced-oop", "validation"],
        "learning_objectives": [
            "Build class creation validation using Python metaclasses",
            "Enforce specific method declarations and naming conventions at load-time"
        ],
        "problem_statement": "Build a metaclass `RequireModelFormatMeta` that enforces that any subclass defines a method called `predict(self, X)` and has a class attribute `model_type` that is a string starting with 'custom_'. If these requirements are not met, raise a `TypeError` when the class is defined (at load/import time, not instantiation time).",
        "real_world_context": "Library developers use metaclasses to build plug-and-play frameworks. For instance, in PyTorch or Pydantic, metaclasses scan class attributes to automatically build neural layers or validate schema fields during module imports.",
        "hints": [
            "A metaclass inherits from `type`.",
            "Override the `__new__(mcs, name, bases, namespace)` or `__init__` method of the metaclass.",
            "Check the class dictionary (`namespace`) for the existence of callable 'predict' and the formatting of 'model_type'."
        ],
        "solution": {
            "explanation": "Metaclasses are the classes of classes; they define how classes behave and are constructed. When Python executes a `class` statement, it calls the metaclass's `__new__` method to allocate the class object. By intercepting this creation step, we can inspect class namespace contents, verify method signatures, and validate attributes before the class is registered, raising a `TypeError` immediately if it violates naming/interface rules.",
            "key_takeaways": [
                "Metaclasses customize class creation, executing logic when a module is first loaded.",
                "TypeError raised in metaclass __new__ blocks class compilation, serving as a strict static interface check."
            ]
        },
        "starter_code": {
            "python": "class RequireModelFormatMeta(type):\n    def __new__(mcs, name, bases, namespace):\n        # TODO: Build class checks and raise TypeError if invalid\n        return super().__new__(mcs, name, bases, namespace)"
        },
        "expected_output": "Attempting to declare a class without 'predict' or 'model_type' starting with 'custom_' raises a TypeError immediately.",
        "follow_up_questions": [
            "What is the difference between `__new__` and `__init__` in a metaclass?",
            "Can you achieve class validation without metaclasses using `__init_subclass__` in modern Python?"
        ],
        "references": [
            {
                "title": "Python Metaclasses Tutorial",
                "url": "https://realpython.com/python-metaclasses/"
            }
        ]
    })

    # Q10: Memory Management and GC
    questions.append({
        "id": 10,
        "slug": "memory-management-gc",
        "title": "Build a Circular Reference Leak Breaker",
        "section": "Python",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Python Concurrency & Memory",
        "estimated_time_minutes": 25,
        "tags": ["memory-management", "garbage-collection", "weakref"],
        "learning_objectives": [
            "Build cyclic references to trace reference counting bottlenecks",
            "Resolve reference cycles using weak references"
        ],
        "problem_statement": "Build a cyclic data structure that triggers a reference counting memory leak, and then build a corrected version utilizing `weakref.ref` to break the cycle. Confirm programmatically that the reference counts drop to zero immediately after deleting variables, without waiting for the generational garbage collector.",
        "real_world_context": "In deep learning graph architectures, nodes contain pointers to children, and children point back to their parents. Without breaking these cycles using weak references, loaded neural architectures leak memory indefinitely, causing Out Of Memory (OOM) errors.",
        "hints": [
            "Check reference counts using `sys.getrefcount(obj)`. Remember that calling `sys.getrefcount` temporarily increments the count by 1.",
            "Circular reference occurs when `A.child = B` and `B.parent = A`.",
            "A `weakref.ref(obj)` creates a weak reference that does not increment the target's reference count, allowing it to be garbage collected."
        ],
        "solution": {
            "explanation": "Python's primary memory management system is reference counting. When an object's reference count hits zero, it is immediately deallocated. However, circular references prevent reference counts from ever reaching zero, leaving cleanup to the generational cyclic Garbage Collector (GC). The GC runs periodically, which causes delayed reclamation. By utilizing `weakref`, we can reference a parent object without increasing its reference count. When the strong reference to the parent is deleted, its count drops to zero, and it is deallocated immediately, breaking the cycle.",
            "key_takeaways": [
                "Reference counting triggers immediate deallocation; cyclic GC runs periodically to collect stranded reference loops.",
                "Weak references enable referencing objects without preventing their collection, essential for parent-child graph nodes."
            ]
        },
        "starter_code": {
            "python": "import sys\nimport gc\nimport weakref\n\nclass Node:\n    def __init__(self, name):\n        self.name = name\n        self.parent = None\n        self.children = []\n\ndef build_leak():\n    # TODO: Build circular reference loop\n    pass\n\ndef build_fixed_leak():\n    # TODO: Build cycle broken by weakref on parent\n    pass"
        },
        "expected_output": "Prints showing reference counts remaining high in the circular reference demo, and immediately dropping to zero in the weakref demo.",
        "follow_up_questions": [
            "How does Python's generational garbage collector classify objects (Generation 0, 1, 2)?",
            "What is the cost of executing `gc.collect()` manually in high-throughput applications?"
        ],
        "references": [
            {
                "title": "Python gc module",
                "url": "https://docs.python.org/3/library/gc.html"
            }
        ]
    })
    
    return questions
