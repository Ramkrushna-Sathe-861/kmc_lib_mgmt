"""Catalogue search service functions."""

from sklearn.feature_extraction.text import TfidfVectorizer

from python_app.data.repository import get_books
from python_app.ml.similarity import calculate_cosine_similarity
from python_app.ml.tfidf import (
    create_tfidf_matrix,
    transform_query,
)
from python_app.schemas.search import Book, SearchResult


def build_book_document(book: Book) -> str:
    """Create searchable text from a catalogue book.

    Args:
        book: Catalogue book.

    Returns:
        Combined searchable text.
    """
    return " ".join(
        (
            book.title,
            book.author,
            book.subject,
            book.description,
        )
    )


def build_book_documents(books: list[Book]) -> list[str]:
    """Create searchable documents for catalogue books.

    Args:
        books: Catalogue books.

    Returns:
        List of searchable book documents.
    """
    return [
        build_book_document(book)
        for book in books
    ]


def create_search_index(
    books: list[Book],
) -> tuple[TfidfVectorizer, object]:
    """Create a TF-IDF search index for catalogue books.

    Args:
        books: Catalogue books.

    Returns:
        Tuple containing the fitted vectorizer and document matrix.
    """
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
    )

    documents = build_book_documents(books)

    document_matrix = create_tfidf_matrix(
        documents,
        vectorizer,
    )

    return vectorizer, document_matrix


def rank_search_results(
    books: list[Book],
    scores,
) -> list[SearchResult]:
    """Create ranked search results.

    Args:
        books: Catalogue books.
        scores: Cosine similarity scores.

    Returns:
        Books sorted by descending similarity.
    """
    results = [
        SearchResult(
            book=book,
            score=float(score),
        )
        for book, score in zip(books, scores)
    ]

    return sorted(
        results,
        key=lambda result: result.score,
        reverse=True,
    )


def search_books(
    query: str,
    top_k: int,
) -> list[SearchResult]:
    """Search the catalogue using TF-IDF and cosine similarity.

    Args:
        query: Natural-language search query.
        top_k: Maximum number of results.

    Returns:
        Ranked catalogue search results.
    """
    books = get_books()

    vectorizer, document_matrix = create_search_index(books)

    query_vector = transform_query(
        query,
        vectorizer,
    )

    scores = calculate_cosine_similarity(
        query_vector,
        document_matrix,
    )

    ranked_results = rank_search_results(
        books,
        scores,
    )

    return ranked_results[:top_k]