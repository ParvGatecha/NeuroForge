import os
import json
import shutil

def main():
    print("Starting content migration to Learning Items...")
    
    # Paths
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    old_questions_dir = os.path.join(base_dir, "content", "questions")
    new_content_dir = os.path.join(base_dir, "content")
    
    if not os.path.exists(old_questions_dir):
        print(f"Error: Old questions directory not found at {old_questions_dir}")
        return
        
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
    
    # Display names
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
    
    # Group items by section
    items_by_section = {sec: [] for sec in sections}
    
    # Scan old questions
    for sec_slug in sections:
        sec_dir = os.path.join(old_questions_dir, sec_slug)
        if not os.path.exists(sec_dir):
            continue
            
        for file_name in os.listdir(sec_dir):
            if not file_name.endswith(".json") or file_name == "index.json":
                continue
                
            file_path = os.path.join(sec_dir, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    q = json.load(f)
                    items_by_section[sec_slug].append(q)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                
    # Helper functions for type inferring
    def infer_resource_type(q):
        sec_lower = q.get("section", "").lower()
        q_type = q.get("question_type", "").lower()
        
        # Check references first
        refs = q.get("references", [])
        if refs and len(refs) > 0:
            url = refs[0].get("url", "").lower()
            if "youtube.com" in url or "youtu.be" in url:
                return "youtube"
            if "kaggle.com" in url:
                return "kaggle"
            if "deep-ml.com" in url:
                return "deepml"
            if "huggingface" in url:
                return "huggingface"
            if "github.com" in url:
                return "github"
            if "arxiv.org" in url:
                return "research-paper"
                
        # Section/Type fallbacks
        if sec_lower == "system-design" or q_type == "system_design":
            return "system-design"
        if sec_lower in ["agents", "rag"] and q_type == "project":
            return "project"
        if sec_lower in ["machine-learning", "deep-learning"]:
            return "deepml"
            
        return "article"
        
    def get_fallback_url(resource_type):
        fallbacks = {
            "deepml": "https://deep-ml.com",
            "kaggle": "https://www.kaggle.com",
            "youtube": "https://www.youtube.com",
            "huggingface": "https://huggingface.co",
            "github": "https://github.com",
            "research-paper": "https://arxiv.org",
            "system-design": "https://github.com/donnemartin/system-design-primer",
            "project": "https://github.com",
            "article": "https://medium.com",
            "custom": "https://google.com"
        }
        return fallbacks.get(resource_type, "https://google.com")
        
    # Create new directories directly under content/
    for sec_slug in sections:
        os.makedirs(os.path.join(new_content_dir, sec_slug), exist_ok=True)
        
    # Migrate and write items
    total_migrated = 0
    all_migrated_items = []
    
    for sec_slug in sections:
        # Sort items in section by id to assign prerequisites sequentially
        items_by_section[sec_slug].sort(key=lambda x: x.get("id", 0))
        sec_items = items_by_section[sec_slug]
        
        for idx, q in enumerate(sec_items):
            q_id = q.get("id")
            slug = q.get("slug")
            
            # Infer properties
            res_type = infer_resource_type(q)
            
            refs = q.get("references", [])
            ext_url = refs[0].get("url") if refs else get_fallback_url(res_type)
            
            # Assign sequential prerequisites within the same section
            prereqs = []
            if idx > 0:
                prereqs = [sec_items[idx - 1].get("id")]
                
            # Build Learning Item
            learning_item = {
                "id": q_id,
                "slug": slug,
                "title": q.get("title"),
                "section": section_mapping.get(sec_slug, sec_slug),
                "difficulty": q.get("difficulty"),
                "resource_type": res_type,
                "external_url": ext_url,
                "estimated_time_minutes": q.get("estimated_time_minutes", 15),
                "tags": q.get("tags", []),
                "learning_objectives": q.get("learning_objectives", []),
                "description": q.get("problem_statement") or q.get("real_world_context") or "Brief overview of what the learner should gain",
                "prerequisites": prereqs
            }
            
            # Write new JSON
            file_name = f"{str(q_id).zfill(3)}-{slug}.json"
            new_path = os.path.join(new_content_dir, sec_slug, file_name)
            
            with open(new_path, 'w', encoding='utf-8') as out_f:
                json.dump(learning_item, out_f, indent=2, ensure_ascii=False)
                
            all_migrated_items.append(learning_item)
            total_migrated += 1
            
    print(f"Successfully migrated {total_migrated} items.")
    
    # Recreate the main content/roadmap.json directly under content/
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
    
    with open(os.path.join(new_content_dir, "roadmap.json"), 'w', encoding='utf-8') as road_f:
        json.dump(roadmap_data, road_f, indent=2, ensure_ascii=False)
        
    print("Roadmap file created.")
    
    # Delete the old content/questions folder
    try:
        shutil.rmtree(old_questions_dir)
        print("Old questions folder deleted successfully.")
    except Exception as e:
        print(f"Could not delete old questions folder: {e}")
        
    print("Migration complete!")

if __name__ == "__main__":
    main()
