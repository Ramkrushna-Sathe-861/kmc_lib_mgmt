"""Machine learning functions for catalogue search."""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SEARCH_FIELDS = [
    "title",
    "author",
    "publisher",
    "ddc_number",
]


def _build_search_documents(
    books: pd.DataFrame,
) -> pd.Series:
    """Build searchable text for each catalogue record.

    Args:
        books: Catalogue DataFrame.

    Returns:
        A Series containing searchable text for each book.
    """
    available_fields = [
        field for field in SEARCH_FIELDS
        if field in books.columns
    ]

    return (
        books[available_fields]
        .fillna("")
        .astype(str)
        .agg(" ".join, axis=1)
    )


def build_search_index(
    books: pd.DataFrame,
) -> tuple[TfidfVectorizer, object]:
    """Build a TF-IDF index for the catalogue.

    Args:
        books: Catalogue DataFrame.

    Returns:
        A tuple containing the fitted TF-IDF vectorizer and
        document matrix.

    Raises:
        ValueError: If the catalogue is empty.
    """
    if books.empty:
        raise ValueError("Books cannot be empty.")

    documents = _build_search_documents(books)

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
    )

    document_vectors = vectorizer.fit_transform(documents)

    return vectorizer, document_vectors



def _deduplicate_results(
    results: list[dict],
) -> list[dict]:
    """Keep only the highest-scoring result for each book.

    Args:
        results: Ranked catalogue search results.

    Returns:
        Deduplicated ranked results.
    """
    best_results: dict[str, dict] = {}

    for result in results:
        book_id = str(result["book_id"])

        existing_result = best_results.get(book_id)

        if (
            existing_result is None
            or result["relevance_score"]
            > existing_result["relevance_score"]
        ):
            best_results[book_id] = result

    return sorted(
        best_results.values(),
        key=lambda result: result["relevance_score"],
        reverse=True,
    )

def search_books(
    query: str,
    books: pd.DataFrame,
    vectorizer: TfidfVectorizer,
    document_vectors: object,
    top_k: int = 10,
) -> list[dict]:
    """Search catalogue using a pre-built TF-IDF index.

    Args:
        query: Natural-language search query.
        books: Catalogue DataFrame.
        vectorizer: Fitted TF-IDF vectorizer.
        document_vectors: TF-IDF matrix for catalogue records.
        top_k: Maximum number of results to return.

    Returns:
        Catalogue records ranked by relevance.

    Raises:
        ValueError: If the query is empty or top_k is invalid.
    """
    if not query.strip():
        raise ValueError("Search query cannot be empty.")

    if top_k < 1:
        raise ValueError("top_k must be greater than zero.")

    query_vector = vectorizer.transform([query])

    similarity_scores = cosine_similarity(
        query_vector,
        document_vectors,
    ).flatten()

    ranked_indexes = similarity_scores.argsort()[::-1]

    results = []

    for index in ranked_indexes:
        score = similarity_scores[index]

        if score <= 0:
            break

        result = books.iloc[index].to_dict()
        result["relevance_score"] = float(score)

        results.append(result)

        if len(results) >= top_k:
            break

    return _deduplicate_results(results)[:top_k]