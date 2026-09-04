"""Tests for similarity functions."""

from python_app.ml.similarity import calculate_cosine_similarity
from python_app.ml.tfidf import create_tfidf_matrix, create_vectorizer, transform_query


def test_calculate_cosine_similarity() -> None:
    """Verify that similar documents receive higher scores."""
    vectorizer = create_vectorizer()

    documents = [
        "python programming",
        "machine learning",
    ]

    document_matrix = create_tfidf_matrix(
        documents,
        vectorizer,
    )

    query_vector = transform_query(
        "python",
        vectorizer,
    )

    scores = calculate_cosine_similarity(
        query_vector,
        document_matrix,
    )

    assert len(scores) == 2
    assert scores[0] > scores[1]