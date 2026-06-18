import os
import argparse
import subprocess
import shlex

ESME_DIR = r"C:\Users\Alfre\.gemini\antigravity\scratch\ESME_2.6"

def get_candidates_via_findstr(term):
    """Run findstr to find files containing the term."""
    try:
        # Run findstr in ESME_DIR
        cmd = f'findstr /s /i /m "{term}" *.md'
        # We use shell=True to easily handle wildcards and redirection on Windows
        res = subprocess.run(
            cmd,
            shell=True,
            cwd=ESME_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=5
        )
        if res.returncode == 0:
            lines = res.stdout.splitlines()
            return [os.path.join(ESME_DIR, line.strip()) for line in lines if line.strip()]
    except Exception:
        pass
    return []

def search_esme(query_str, limit=10):
    terms = [t.lower() for t in query_str.split() if len(t) > 1]
    if not terms:
        terms = [query_str.lower()]

    candidates = set()

    # Step 1: Collect candidates where filename matches any term
    for root, dirs, files in os.walk(ESME_DIR):
        if "images" in dirs:
            dirs.remove("images")
        for file in files:
            if file.endswith(".md"):
                file_lower = file.lower()
                if any(term in file_lower for term in terms):
                    candidates.add(os.path.join(root, file))

    # Step 2: Use findstr to get content-based candidates for the most specific (longest) term
    longest_term = max(terms, key=len)
    if len(longest_term) >= 3:
        findstr_files = get_candidates_via_findstr(longest_term)
        candidates.update(findstr_files)

    # Step 3: Score the candidates
    results = []
    for file_path in candidates:
        try:
            filename = os.path.basename(file_path)
            filename_lower = filename.lower()
            score = 0
            matches = {}

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            content_lower = content.lower()

            for term in terms:
                # Filename match bonus
                if term in filename_lower:
                    score += 150
                    matches[term] = matches.get(term, 0) + 15
                
                cnt = content_lower.count(term)
                if cnt > 0:
                    score += cnt * 10
                    matches[term] = matches.get(term, 0) + cnt

            if score > 0:
                # Extract snippet
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
                    "score": score,
                    "snippet": snippet,
                    "matches": matches
                })
        except Exception:
            pass

    # Sort results
    results.sort(key=lambda x: x["score"], reverse=True)

    print(f"\n--- ESME 2.6 Search Results for: '{query_str}' ---")
    if not results:
        print("No matching documentation found.")
        return

    for i, res in enumerate(results[:limit]):
        rel_path = os.path.relpath(res["abs_path"], ESME_DIR)
        print(f"\n[{i+1}] {rel_path} (Score: {res['score']})")
        print(f"    Path: [link](file:///{res['abs_path'].replace(os.sep, '/')})")
        if res['snippet']:
            print(f"    Snippet: {res['snippet']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search ESME 2.6 manual Markdown files.")
    parser.add_argument("--query", "-q", required=True, type=str, help="Search terms")
    parser.add_argument("--limit", "-l", default=10, type=int, help="Limit number of results")
    args = parser.parse_args()

    search_esme(args.query, args.limit)
