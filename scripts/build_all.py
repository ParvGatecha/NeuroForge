import os
import json
import sys

def main():
    print("Starting TensorTrack repository builder...")
    
    # Define directories
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    content_dir = os.path.join(base_dir, "content")
    
    sections = [
        "python",
        "statistics",
        "machine-learning",
        "deep-learning",
        "llm",
        "rag",
        "agents",
        "system-design"
    ]
    
    # Mapping of folder names to display names
    section_mapping = {
        "python": "Python",
        "statistics": "Statistics",
        "machine-learning": "Machine Learning",
        "deep-learning": "Deep Learning",
        "llm": "LLM",
        "rag": "RAG",
        "agents": "Agents",
        "system-design": "System Design"
    }
    
    all_items = []
    validation_errors = []
    section_counts = {sec: 0 for sec in sections}
    difficulty_counts = {sec: {"Easy": 0, "Medium": 0, "Hard": 0} for sec in sections}
    
    for sec_slug in sections:
        sec_dir = os.path.join(content_dir, sec_slug)
        if not os.path.exists(sec_dir):
            validation_errors.append(f"Missing section folder: {sec_slug}")
            continue
            
        for file_name in os.listdir(sec_dir):
            if not file_name.endswith(".json") or file_name == "index.json":
                continue
                
            file_path = os.path.join(sec_dir, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    item = json.load(f)
                    
                # Validate schema
                required_keys = [
                    "id", "slug", "title", "section", "difficulty", "theory_resource",
                    "practice_resource", "estimated_time_minutes", "tags",
                    "learning_objectives", "description", "prerequisites"
                ]
                
                for k in required_keys:
                    if k not in item:
                        validation_errors.append(f"File {file_name}: Missing required key '{k}'")
                
                # Check difficulty
                diff = item.get("difficulty")
                if diff not in ["Easy", "Medium", "Hard"]:
                    validation_errors.append(f"File {file_name}: Invalid difficulty '{diff}'")
                    
                # Check theory resource
                theory = item.get("theory_resource")
                if theory:
                    for sub_k in ["title", "url", "type"]:
                        if sub_k not in theory:
                            validation_errors.append(f"File {file_name}: theory_resource missing subkey '{sub_k}'")
                    t_type = theory.get("type")
                    valid_theory_types = ["article", "blog", "documentation", "youtube", "research-paper", "github", "course"]
                    if t_type not in valid_theory_types:
                        validation_errors.append(f"File {file_name}: Invalid theory_resource.type '{t_type}'")
                
                # Check practice resource
                practice = item.get("practice_resource")
                if practice:
                    for sub_k in ["platform", "title", "url"]:
                        if sub_k not in practice:
                            validation_errors.append(f"File {file_name}: practice_resource missing subkey '{sub_k}'")
                    p_plat = practice.get("platform")
                    valid_practice_platforms = ["DEEP_ML", "KAGGLE", "HUGGING_FACE", "GITHUB", "LANGCHAIN", "LANGGRAPH", "LLAMAINDEX", "CUSTOM", "EXTERNAL"]
                    if p_plat not in valid_practice_platforms:
                        validation_errors.append(f"File {file_name}: Invalid practice_resource.platform '{p_plat}'")
                
                section_counts[sec_slug] += 1
                if diff in difficulty_counts[sec_slug]:
                    difficulty_counts[sec_slug][diff] += 1
                    
                all_items.append(item)
            except Exception as e:
                validation_errors.append(f"Error parsing {file_name}: {e}")
                
    if validation_errors:
        print("\nValidation Failed! Errors:")
        for err in validation_errors:
            print(f" - {err}")
        sys.exit(1)
        
    print(f"\nValidation Passed! All {len(all_items)} learning items are valid.")
    
    # Sort items by ID
    all_items.sort(key=lambda x: x["id"])
    
    # Write search index
    search_index_path = os.path.join(content_dir, "search_index.json")
    with open(search_index_path, 'w', encoding='utf-8') as sf:
        json.dump(all_items, sf, indent=2, ensure_ascii=False)
    print(f"Search index built: {search_index_path}")
    
    # Write roadmap.json
    roadmap_data = {
        "section_order": sections,
        "prerequisites": {
            "python": [],
            "statistics": [],
            "machine-learning": ["python", "statistics"],
            "deep-learning": ["machine-learning"],
            "llm": ["deep-learning"],
            "rag": ["llm"],
            "agents": ["llm"],
            "system-design": ["machine-learning", "deep-learning", "llm", "rag", "agents"]
        },
        "recommended_sequence": sections
    }
    
    roadmap_path = os.path.join(content_dir, "roadmap.json")
    with open(roadmap_path, 'w', encoding='utf-8') as rf:
        json.dump(roadmap_data, rf, indent=2, ensure_ascii=False)
    print(f"Roadmap written: {roadmap_path}")
    
    # Write CONTENT_REPORT.md
    report_content = generate_report_content(all_items, section_counts, difficulty_counts)
    report_path = os.path.join(base_dir, "CONTENT_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Content report written: {report_path}")
    print("TensorTrack repository built successfully!")

def generate_report_content(all_items, section_counts, difficulty_counts):
    total = len(all_items)
    
    markdown = f"""# TensorTrack Curriculum Roadmap Content Summary
    
This report provides a comprehensive summary of the Learning Items in the TensorTrack roadmap (v2), a structured platform for AI Engineers to track and navigate external educational resources.

## Repository Overview

- **Total Learning Items**: {total}
- **Status**: Production-Ready (all items conform to the updated schema and are structured directly by section folders under `content/`)

## Section Breakdown

| Section | Target Count | Actual Count | Easy | Medium | Hard | Difficulty Split |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Python** | 20 | {section_counts['python']} | {difficulty_counts['python']['Easy']} | {difficulty_counts['python']['Medium']} | {difficulty_counts['python']['Hard']} | 30% / 50% / 20% |
| **Statistics** | 30 | {section_counts['statistics']} | {difficulty_counts['statistics']['Easy']} | {difficulty_counts['statistics']['Medium']} | {difficulty_counts['statistics']['Hard']} | 33% / 47% / 20% |
| **Machine Learning** | 40 | {section_counts['machine-learning']} | {difficulty_counts['machine-learning']['Easy']} | {difficulty_counts['machine-learning']['Medium']} | {difficulty_counts['machine-learning']['Hard']} | 30% / 50% / 20% |
| **Deep Learning** | 30 | {section_counts['deep-learning']} | {difficulty_counts['deep-learning']['Easy']} | {difficulty_counts['deep-learning']['Medium']} | {difficulty_counts['deep-learning']['Hard']} | 33% / 47% / 20% |
| **LLM** | 30 | {section_counts['llm']} | {difficulty_counts['llm']['Easy']} | {difficulty_counts['llm']['Medium']} | {difficulty_counts['llm']['Hard']} | 33% / 47% / 20% |
| **RAG** | 20 | {section_counts['rag']} | {difficulty_counts['rag']['Easy']} | {difficulty_counts['rag']['Medium']} | {difficulty_counts['rag']['Hard']} | 30% / 50% / 20% |
| **Agents** | 20 | {section_counts['agents']} | {difficulty_counts['agents']['Easy']} | {difficulty_counts['agents']['Medium']} | {difficulty_counts['agents']['Hard']} | 30% / 50% / 20% |
| **System Design** | 10 | {section_counts['system-design']} | {difficulty_counts['system-design']['Easy']} | {difficulty_counts['system-design']['Medium']} | {difficulty_counts['system-design']['Hard']} | 20% / 60% / 20% |
| **Total** | **200** | **{total}** | **{sum(d['Easy'] for d in difficulty_counts.values())}** | **{sum(d['Medium'] for d in difficulty_counts.values())}** | **{sum(d['Hard'] for d in difficulty_counts.values())}** | **30% / 50% / 20%** |

## Curriculum Track Descriptions

### 1. Python (20 Learning Items)
Curated items covering memory comparison, lazy execution, function metadata preservation, dynamic decorators, async concurrency, garbage collection, custom context managers, dataclasses, abstract base classes, descriptors, and multiprocessing performance.

### 2. Statistics (30 Learning Items)
Focuses on Skewness, probability, Bayes theorem, PDFs, CLT, MLE, MSE, FDR, metropolis-hastings MCMC, Gibbs sampling, and covariance eigenvalues.

### 3. Machine Learning (40 Learning Items)
Covers Normal Equation regression, SGD step dynamics, Gini impurity, Bayesian hyperparameter tuning, XGBoost split math, EM algorithm, t-SNE / UMAP dimensional reductions, metric calculations, and SVMs.

### 4. Deep Learning (30 Learning Items)
Includes backpropagation gradients, SGD/Adam parameter updates, CNN layer maps, LSTM cell architectures, scaled dot-product attention queries/keys/values, ZeRO distributed memory layers, activation implementations, and weight initializations.

### 5. Large Language Models (LLM) (30 Learning Items)
Covers BPE word tokenization, Temperature decoding logic, PEFT LoRA adapter matrices, Quantizations, FlashAttention SRAM tiling, Speculative decoding validation, Rotary positional embeddings (RoPE), beam search, top-p nucleus sampling, and evaluation scores (BLEU, ROUGE).

### 6. Retrieval-Augmented Generation (RAG) (20 Learning Items)
Includes semantic splits, HNSW vectors, hybrid searches (RRF), cross-encoder rerankers, RAGAs evaluation loops, Lost-in-the-Middle context compression, metadata filtering, HyDE, and knowledge graphs.

### 7. AI Agents (20 Learning Items)
Covers ReAct loop executions, function call schemas, state graph routing, task decomposition, memory systems, self-reflection refinement, human supervision gates, and exception-handling self-healing.

### 8. System Design (10 Learning Items)
Architectural case studies covering online fraud filters, low-latency LLM serving (vLLM), multi-stage recommendation pipelines, multimodal searches, and multi-agent service desks.
"""
    return markdown

if __name__ == "__main__":
    main()
