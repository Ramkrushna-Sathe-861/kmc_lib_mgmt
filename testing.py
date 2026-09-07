from python_app.services.search_service import search_catalogue

results = search_catalogue(
    query="computer science",
    top_k=10,
)

for book in results:
    print(
        f"{book['title']} -> "
        f"{book['relevance_score']:.3f}"
    )