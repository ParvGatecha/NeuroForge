import os
import json

def get_new_theory_type(old_type, url):
    url_lower = url.lower()
    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        return "youtube"
    if "arxiv.org" in url_lower or "researchgate.net" in url_lower:
        return "research-paper"
    if "github.com" in url_lower:
        return "github"
    
    old_type_lower = old_type.lower()
    if old_type_lower in ["youtube", "research-paper", "github", "article"]:
        return old_type_lower
    if old_type_lower == "project":
        return "github"
    if old_type_lower == "system-design":
        return "documentation"
    if old_type_lower in ["deepml", "kaggle"]:
        return "course"
    if old_type_lower == "huggingface":
        return "documentation"
    
    return "article"

def get_practice_platform(old_type, url):
    url_lower = url.lower()
    if "deep-ml.com" in url_lower or "deepml" in url_lower:
        return "DEEP_ML"
    if "kaggle.com" in url_lower:
        return "KAGGLE"
    if "huggingface.co" in url_lower:
        return "HUGGING_FACE"
    if "langchain" in url_lower:
        return "LANGCHAIN"
    if "langgraph" in url_lower:
        return "LANGGRAPH"
    if "llamaindex" in url_lower:
        return "LLAMAINDEX"
    if "github.com" in url_lower:
        return "GITHUB"
    
    old_type_lower = old_type.lower()
    if old_type_lower == "deepml":
        return "DEEP_ML"
    if old_type_lower == "kaggle":
        return "KAGGLE"
    if old_type_lower == "huggingface":
        return "HUGGING_FACE"
    if old_type_lower in ["github", "project"]:
        return "GITHUB"
    
    return "EXTERNAL"

def main():
    print("Starting Content Migration v2...")
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    content_dir = os.path.join(base_dir, "content")
    
    if not os.path.exists(content_dir):
        print(f"Error: Content directory not found at {content_dir}")
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
    
    total_migrated = 0
    for sec in sections:
        sec_dir = os.path.join(content_dir, sec)
        if not os.path.exists(sec_dir):
            continue
            
        for file_name in os.listdir(sec_dir):
            if not file_name.endswith(".json") or file_name == "index.json":
                continue
                
            file_path = os.path.join(sec_dir, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    item = json.load(f)
                
                # Check if already migrated
                if "theory_resource" in item and "practice_resource" in item:
                    continue
                
                old_type = item.get("resource_type", "custom")
                old_url = item.get("external_url", "https://google.com")
                title = item.get("title", "Topic")
                
                # Infer values
                theory_type = get_new_theory_type(old_type, old_url)
                practice_plat = get_practice_platform(old_type, old_url)
                
                item["theory_resource"] = {
                    "title": f"Theory: {title}",
                    "url": old_url,
                    "type": theory_type
                }
                
                item["practice_resource"] = {
                    "platform": practice_plat,
                    "title": f"Practice: {title}",
                    "url": old_url
                }
                
                # Delete old keys
                if "resource_type" in item:
                    del item["resource_type"]
                if "external_url" in item:
                    del item["external_url"]
                    
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(item, f, indent=2, ensure_ascii=False)
                total_migrated += 1
                
            except Exception as e:
                print(f"Error migrating {file_path}: {e}")
                
    print(f"Migration v2 complete! Migrated {total_migrated} items.")

if __name__ == "__main__":
    main()
