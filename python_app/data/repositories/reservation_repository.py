"""Data access functions for library reservations."""

from python_app.data.dummy_data import (
    generate_books,
    generate_members,
    generate_reservations,
)


def get_reservations() -> list[dict]:
    """Return all library reservation records.

    Returns:
        A list of reservation records.
    """
    books = generate_books()
    members = generate_members()

    return generate_reservations(
        members=members,
        books=books,
    )