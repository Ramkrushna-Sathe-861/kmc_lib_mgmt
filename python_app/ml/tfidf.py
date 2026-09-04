"""TF-IDF vectorization functions."""

from sklearn.feature_extraction.text import TfidfVectorizer


def create_vectorizer() -> TfidfVectorizer:
    """Create and configure a TF-IDF vectorizer.

    Returns:
        Configured TF-IDF vectorizer.
    """
    return TfidfVectorizer(
        lowercase=True,
        stop_words="english",
    )


def create_tfidf_matrix(
    documents: list[str],
    vectorizer: TfidfVectorizer,
):
    """Create a TF-IDF matrix from documents.

    Args:
        documents: Collection of text documents.
        vectorizer: TF-IDF vectorizer.

    Returns:
        Sparse TF-IDF document matrix.
    """
    return vectorizer.fit_transform(documents)


def transform_query(
    query: str,
    vectorizer: TfidfVectorizer,
):
    """Transform a search query into a TF-IDF vector.

    Args:
        query: User search query.
        vectorizer: Fitted TF-IDF vectorizer.

    Returns:
        Sparse TF-IDF query vector.
    """
    return vectorizer.transform([query])