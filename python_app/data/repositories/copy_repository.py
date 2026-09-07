"""Data access functions for physical library copies."""

from python_app.data.dummy_data import generate_books, generate_copies


def get_copies() -> list[dict]:
    """Return all physical book copies.

    Returns:
        A list of physical copy records.
    """
    books = generate_books()
    return generate_copies(books)