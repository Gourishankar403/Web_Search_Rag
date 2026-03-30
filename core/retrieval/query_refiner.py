def refine_query(query, history):
    if not history:
        return query

    last_turn = history.strip().split("\n")[-1]
    return f"{query} (context: {last_turn})"