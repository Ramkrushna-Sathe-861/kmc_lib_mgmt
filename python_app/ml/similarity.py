"""Similarity calculation functions."""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def calculate_cosine_similarity(
    query_vector,
    document_matrix,
) -> np.ndarray:
    """Calculate cosine similarity between query and documents.

    Args:
        query_vector: TF-IDF vector representing the query.
        document_matrix: TF-IDF matrix representing documents.

    Returns:
        Similarity score for each document.
    """
    return cosine_similarity(
        query_vector,
        document_matrix,
    )[0]