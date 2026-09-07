"""Business logic for library catalogue search."""

from python_app.ml.search import search_books
from python_app.ml.search_index import load_search_index


_books, _vectorizer, _document_vectors = load_search_index()


def search_catalogue(
    query: str,
    top_k: int = 10,
) -> list[dict]:
    """Search the library catalogue.

    Args:
        query: Natural-language search query.
        top_k: Maximum number of results to return.

    Returns:
        Catalogue records ranked by relevance.
    """
    return search_books(
        query=query,
        books=_books,
        vectorizer=_vectorizer,
        document_vectors=_document_vectors,
        top_k=top_k,
    )