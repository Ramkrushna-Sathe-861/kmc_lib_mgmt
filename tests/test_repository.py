"""Tests for the library repository."""

from python_app.data.repository import get_books, get_loans


def test_get_books_returns_books() -> None:
    """Verify that catalogue books are returned."""
    books = get_books()

    assert books
    assert all(book.id for book in books)


def test_get_loans_returns_loans() -> None:
    """Verify that loan records are returned."""
    loans = get_loans()

    assert loans