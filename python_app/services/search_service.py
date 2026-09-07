"""Business logic for library catalogue search."""

import pandas as pd

from python_app.ml.search import search_books
from python_app.ml.search_index import load_search_index
from python_app.data.repositories.copy_repository import get_book_copies


_books, _vectorizer, _document_vectors = load_search_index()


def _build_copy_lookup(copies: pd.DataFrame) -> dict:
    """Build a lookup of physical copies grouped by book ID."""
    copy_lookup = {}

    for book_id, book_group in copies.groupby("book_id"):
        copy_lookup[book_id] = book_group[
            [
                "book_copy_id",
                "branch_id",
                "branch_name",
                "shelf",
                "accession",
                "book_condition",
                "book_status",
            ]
        ].to_dict(orient="records")

    return copy_lookup


def search_catalogue(query: str, top_k: int = 10) -> list[dict]:
    """Search the catalogue and include physical-copy information."""
    results = search_books(
        query=query,
        books=_books,
        vectorizer=_vectorizer,
        document_vectors=_document_vectors,
        top_k=top_k,
    )

    copies = get_book_copies()
    copy_lookup = _build_copy_lookup(copies)

    for result in results:
        book_id = result["book_id"]
        result["copies"] = copy_lookup.get(book_id, [])

    return results