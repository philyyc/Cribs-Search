from whoosh.qparser import QueryParser
from whoosh import index

index_dir = "Index"

def search_index(query_str, index_dir):
    idx = index.open_dir(index_dir)

    qp = QueryParser("content", idx.schema)

    q = qp.parse(query_str)

    results = []

    with idx.searcher() as searcher:
        matches = searcher.search(q)
        for match in matches:
            results.append(match["title"])

    return results

search = "rigid"

print(search_index(search, index_dir))