import os
import argparse

# Resolve path dynamically relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ESME_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "references", "ESME_2.6"))

def search_esme(query_str, limit=10):
    terms = [t.lower() for t in query_str.split() if len(t) > 1]
    if not terms:
        terms = [query_str.lower()]

    results = []

    # Step 1: Walk the directory and collect matches based on filename/path
    for root, dirs, files in os.walk(ESME_DIR):
        if "images" in dirs:
            dirs.remove("images")
        
        for file in files:
            if not file.endswith(".md"):
                continue

            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, ESME_DIR)
            rel_path_lower = rel_path.lower()
            filename_lower = file.lower()

            # Check if all terms appear somewhere in the path
            if not all(term in rel_path_lower for term in terms):
                continue

            score = 0
            matches = {}

            # Calculate score based on filename and directory match
            for term in terms:
                if term in filename_lower:
                    score += 150
                    matches[term] = 15
                elif term in rel_path_lower:
                    score += 50
                    matches[term] = 5

            # Step 2: Open only this matching file to refine score and get snippet
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                
                content_lower = content.lower()
                for term in terms:
                    cnt = content_lower.count(term)
                    if cnt > 0:
                        score += cnt * 10
                        matches[term] = matches.get(term, 0) + cnt

                # Snippet extraction
                snippet = ""
                first_term = next((term for term in terms if term in content_lower), None)
                if first_term:
                    pos = content_lower.find(first_term)
                    start = max(0, pos - 60)
                    end = min(len(content), pos + len(first_term) + 60)
                    raw_snippet = content[start:end].replace("\n", " ")
                    snippet = f"...{raw_snippet}..."

                results.append({
                    "abs_path": file_path,
                    "rel_path": rel_path,
                    "score": score,
                    "snippet": snippet,
                    "matches": matches
                })
            except Exception:
                # If we fail to read, still keep it as a match but with path score
                results.append({
                    "abs_path": file_path,
                    "rel_path": rel_path,
                    "score": score,
                    "snippet": "",
                    "matches": matches
                })

    # Sort results
    results.sort(key=lambda x: x["score"], reverse=True)

    print(f"\n--- ESME 2.6 Search Results for: '{query_str}' ---")
    if not results:
        print("No matching documentation found.")
        return

    for i, res in enumerate(results[:limit]):
        print(f"\n[{i+1}] {res['rel_path']} (Score: {res['score']})")
        print(f"    Path: [link](file:///{res['abs_path'].replace(os.sep, '/')})")
        if res['snippet']:
            print(f"    Snippet: {res['snippet']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search ESME 2.6 manual Markdown files.")
    parser.add_argument("--query", "-q", required=True, type=str, help="Search terms")
    parser.add_argument("--limit", "-l", default=10, type=int, help="Limit number of results")
    args = parser.parse_args()

    search_esme(args.query, args.limit)
