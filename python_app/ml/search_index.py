"""Load the persisted catalogue search index."""

import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


INDEX_DIRECTORY = Path("python_app/data/indexes")

VECTORIZER_FILE = INDEX_DIRECTORY / "tfidf_vectorizer.pkl"
DOCUMENT_VECTORS_FILE = INDEX_DIRECTORY / "tfidf_document_vectors.pkl"
CATALOGUE_FILE = INDEX_DIRECTORY / "catalogue.pkl"


def load_search_index() -> tuple[
    pd.DataFrame,
    TfidfVectorizer,
    object,
]:
    """Load the persisted TF-IDF search index.

    Returns:
        A tuple containing the catalogue, TF-IDF vectorizer,
        and document vectors.

    Raises:
        FileNotFoundError: If an index file is missing.
    """
    required_files = [
        VECTORIZER_FILE,
        DOCUMENT_VECTORS_FILE,
        CATALOGUE_FILE,
    ]

    missing_files = [
        file_path
        for file_path in required_files
        if not file_path.exists()
    ]

    if missing_files:
        raise FileNotFoundError(
            f"Search index files are missing: {missing_files}"
        )

    with VECTORIZER_FILE.open("rb") as file:
        vectorizer = pickle.load(file)

    with DOCUMENT_VECTORS_FILE.open("rb") as file:
        document_vectors = pickle.load(file)

    with CATALOGUE_FILE.open("rb") as file:
        catalogue = pickle.load(file)

    return catalogue, vectorizer, document_vectors