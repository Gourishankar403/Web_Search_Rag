def build_context(results):
    return "\n".join([r["content"] for r in results])