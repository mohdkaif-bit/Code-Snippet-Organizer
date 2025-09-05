from rapidfuzz import process

def search_snippets(query, snippets, key="title", limit=5):
    titles = [s[key] for s in snippets]
    results = process.extract(query, titles, limit=limit)
    return [snippets[idx] for _, score, idx in results if score > 50]
