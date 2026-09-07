"""Build and persist the TF-IDF catalogue search index."""

import pickle
from pathlib import Path

from python_app.ml.search import build_search_index
from python_app.data.repositories.catalogue_repository import get_books


INDEX_DIRECTORY = Path("python_app/data/indexes")

VECTORIZER_FILE = INDEX_DIRECTORY / "tfidf_vectorizer.pkl"
DOCUMENT_VECTORS_FILE = INDEX_DIRECTORY / "tfidf_document_vectors.pkl"
CATALOGUE_FILE = INDEX_DIRECTORY / "catalogue.pkl"


def save_search_index() -> None:
    """Build and save the catalogue TF-IDF index.

    Raises:
        OSError: If the index files cannot be written.
    """
    books = get_books()

    vectorizer, document_vectors = build_search_index(books)

    INDEX_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    with VECTORIZER_FILE.open("wb") as file:
        pickle.dump(vectorizer, file)

    with DOCUMENT_VECTORS_FILE.open("wb") as file:
        pickle.dump(document_vectors, file)

    with CATALOGUE_FILE.open("wb") as file:
        pickle.dump(books, file)

    print("TF-IDF search index created successfully.")
    print(f"Books indexed: {len(books)}")
    print(f"Index directory: {INDEX_DIRECTORY}")


if __name__ == "__main__":
    save_search_index()