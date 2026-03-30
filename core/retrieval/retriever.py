from config.settings import TOP_K

def retrieve(store, query):
    return store.search(query, TOP_K)