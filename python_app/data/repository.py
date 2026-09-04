"""Functions for accessing library data."""

from python_app.data.dummy_data import BOOKS, LOANS
from python_app.schemas.search import Book


def get_books() -> list[Book]:
    """Return all books available in the local catalogue.

    Returns:
        A list containing catalogue books.
    """
    return BOOKS.copy()


def get_loans() -> list[dict[str, int]]:
    """Return all local borrowing records.

    Returns:
        A list of borrowing records.
    """
    return LOANS.copy()