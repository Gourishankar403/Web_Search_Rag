from core.retrieval.retriever import retrieve
from core.retrieval.reranker import rerank
from core.retrieval.query_refiner import refine_query
from core.retrieval.context_builder import build_context


def route_query(store, memory, question):
    history = memory.get_context()
    from core.adaptive.query_analyzer import analyze_query
    analysis = analyze_query(question)

    if not analysis["is_complex"]:
        results = retrieve(store, question)
        context = build_context(results)
        return context

    refined_query = refine_query(question, history)
    results = retrieve(store, refined_query)
    results = rerank(results, refined_query)
    context = build_context(results)
    return context