def rerank(results, query):
    query_words=set(query.lower().split())

    scored=[]
    for r in results:
        text=r["content"].lower()
        score=sum(1 for word in query_words if word in text)
        scored.append((score,r))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [r for _,r in scored]