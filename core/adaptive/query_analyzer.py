def analyze_query(query):
    """
    Analyze query complexity and intent
    """

    length = len(query.split())


    is_complex = length > 8
    needs_context = any(word in query.lower() for word in [
        "explain", "how", "why", "compare", "difference"
    ])

    return {
        "is_complex": is_complex,
        "needs_context": needs_context
    }