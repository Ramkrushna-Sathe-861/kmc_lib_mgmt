"""Tests for TF-IDF functions."""

import pytest

from python_app.ml.tfidf import (
    create_tfidf_matrix,
    create_vectorizer,
    transform_query,
)


def test_create_vectorizer() -> None:
    """Verify that a vectorizer can be created."""
    vectorizer = create_vectorizer()

    assert vectorizer is not None


def test_create_tfidf_matrix() -> None:
    """Verify that documents are converted to TF-IDF vectors."""
    vectorizer = create_vectorizer()

    documents = [
        "python programming",
        "machine learning",
    ]

    matrix = create_tfidf_matrix(
        documents,
        vectorizer,
    )

    assert matrix.shape[0] == 2


def test_transform_query() -> None:
    """Verify that a query can be transformed."""
    vectorizer = create_vectorizer()

    documents = [
        "python programming",
        "machine learning",
    ]

    create_tfidf_matrix(
        documents,
        vectorizer,
    )

    query_vector = transform_query(
        "python",
        vectorizer,
    )

    assert query_vector.shape[0] == 1


def test_transform_query_before_fit_raises_error() -> None:
    """Verify that an unfitted vectorizer raises an error."""
    vectorizer = create_vectorizer()

    with pytest.raises(Exception):
        transform_query(
            "python",
            vectorizer,
        )