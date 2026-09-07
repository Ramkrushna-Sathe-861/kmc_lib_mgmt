"""Tests for library dummy data generation."""

import pytest

from python_app.data.dummy_data import (
    RESERVATION_STATUSES,
    date,
    generate_books,
    generate_copies,
    generate_loans,
    generate_members,
    generate_reservations,
    generate_branches,
    generate_library_policies,
    
)

from python_app.data.repositories.catalogue_repository import get_books

def test_generate_books_returns_requested_count() -> None:
    """Verify that the requested number of books is generated."""
    books = generate_books(count=100)

    assert len(books) == 100


def test_generate_books_has_required_fields() -> None:
    """Verify that generated books contain required catalogue fields."""
    books = generate_books(count=10)

    required_fields = {
        "book_id",
        "title",
        "author",
        "isbn",
        "publisher",
        "year",
        "genre",
        "classification",
        "pages",
        "language",
        "synopsis",
        "keywords",
    }

    for book in books:
        assert required_fields.issubset(book.keys())


def test_generate_books_is_reproducible() -> None:
    """Verify that the same seed generates the same data."""
    first_result = generate_books(count=10, seed=42)
    second_result = generate_books(count=10, seed=42)

    assert first_result == second_result


def test_generate_books_rejects_invalid_count() -> None:
    """Verify that an invalid book count raises ValueError."""
    with pytest.raises(ValueError):
        generate_books(count=0)

def test_generate_copies_returns_requested_count() -> None:
    """Verify that the requested number of copies is generated."""
    books = generate_books(count=10)
    copies = generate_copies(books, count=50)

    assert len(copies) == 50


def test_generate_copies_reference_existing_books() -> None:
    """Verify that every copy references an existing book."""
    books = generate_books(count=10)
    copies = generate_copies(books, count=50)

    book_ids = {book["book_id"] for book in books}

    for copy in copies:
        assert copy["book_id"] in book_ids


def test_generate_copies_has_required_fields() -> None:
    """Verify that generated copies contain required fields."""
    books = generate_books(count=10)
    copies = generate_copies(books, count=20)

    required_fields = {
        "copy_id",
        "book_id",
        "branch_id",
        "shelf_location",
        "condition",
        "status",
    }

    for copy in copies:
        assert required_fields.issubset(copy.keys())


def test_generate_copies_rejects_empty_books() -> None:
    """Verify that copy generation rejects an empty book collection."""
    with pytest.raises(ValueError):
        generate_copies([], count=10)


def test_generate_members_returns_requested_count() -> None:
    """Verify that the requested number of members is generated."""
    members = generate_members(count=100)

    assert len(members) == 100


def test_generate_members_has_required_fields() -> None:
    """Verify that generated members contain required fields."""
    members = generate_members(count=10)

    required_fields = {
        "member_id",
        "name",
        "status",
    }

    for member in members:
        assert required_fields.issubset(member.keys())


def test_generate_members_is_reproducible() -> None:
    """Verify that the same seed generates the same members."""
    first_result = generate_members(count=10, seed=42)
    second_result = generate_members(count=10, seed=42)

    assert first_result == second_result


def test_generate_members_rejects_invalid_count() -> None:
    """Verify that an invalid member count raises ValueError."""
    with pytest.raises(ValueError):
        generate_members(count=0)






def test_generate_loans_returns_requested_count() -> None:
    """Verify that the requested number of loans is generated."""
    books = generate_books(count=20)
    copies = generate_copies(books, count=40)
    members = generate_members(count=10)

    loans = generate_loans(
        members,
        books,
        copies,
        count=100,
    )

    assert len(loans) == 100


def test_generate_loans_reference_existing_entities() -> None:
    """Verify that loans reference valid members, books, and copies."""
    books = generate_books(count=20)
    copies = generate_copies(books, count=40)
    members = generate_members(count=10)

    loans = generate_loans(
        members,
        books,
        copies,
        count=100,
    )

    member_ids = {member["member_id"] for member in members}
    book_ids = {book["book_id"] for book in books}
    copy_ids = {copy["copy_id"] for copy in copies}

    for loan in loans:
        assert loan["member_id"] in member_ids
        assert loan["book_id"] in book_ids
        assert loan["copy_id"] in copy_ids


def test_generate_loans_have_valid_dates() -> None:
    """Verify that loan dates follow the expected order."""
    books = generate_books(count=20)
    copies = generate_copies(books, count=40)
    members = generate_members(count=10)

    loans = generate_loans(
        members,
        books,
        copies,
        count=100,
    )

    for loan in loans:
        assert loan["issue_date"] < loan["due_date"]
        assert loan["return_date"] >= loan["issue_date"]


def test_generate_loans_rejects_empty_members() -> None:
    """Verify that loans cannot be generated without members."""
    books = generate_books(count=20)
    copies = generate_copies(books, count=40)

    with pytest.raises(ValueError):
        generate_loans(
            [],
            books,
            copies,
            count=100,
        )

def test_generate_reservations_returns_requested_count() -> None:
    """Verify that the requested number of reservations is generated."""
    books = generate_books(count=20)
    members = generate_members(count=10)

    reservations = generate_reservations(
        members,
        books,
        count=100,
    )

    assert len(reservations) == 100


def test_generate_reservations_reference_existing_entities() -> None:
    """Verify that reservations reference valid members and books."""
    books = generate_books(count=20)
    members = generate_members(count=10)

    reservations = generate_reservations(
        members,
        books,
        count=100,
    )

    member_ids = {member["member_id"] for member in members}
    book_ids = {book["book_id"] for book in books}

    for reservation in reservations:
        assert reservation["member_id"] in member_ids
        assert reservation["book_id"] in book_ids


def test_generate_reservations_have_valid_status() -> None:
    """Verify that reservation statuses are valid."""
    books = generate_books(count=20)
    members = generate_members(count=10)

    reservations = generate_reservations(
        members,
        books,
        count=100,
    )

    for reservation in reservations:
        assert reservation["status"] in RESERVATION_STATUSES


def test_generate_reservations_have_valid_dates() -> None:
    """Verify that reservation dates are valid."""
    books = generate_books(count=20)
    members = generate_members(count=10)

    reservations = generate_reservations(
        members,
        books,
        count=100,
    )

    for reservation in reservations:
        assert date(2025, 1, 1) <= reservation["reservation_date"] <= date(
            2026, 8, 31
        )


def test_generate_reservations_rejects_empty_members() -> None:
    """Verify that reservations cannot be generated without members."""
    books = generate_books(count=20)

    with pytest.raises(ValueError):
        generate_reservations(
            [],
            books,
            count=100,
        )


def test_generate_reservations_rejects_empty_books() -> None:
    """Verify that reservations cannot be generated without books."""
    members = generate_members(count=10)

    with pytest.raises(ValueError):
        generate_reservations(
            members,
            [],
            count=100,
        )


def test_generate_reservations_rejects_invalid_count() -> None:
    """Verify that invalid reservation counts are rejected."""
    books = generate_books(count=20)
    members = generate_members(count=10)

    with pytest.raises(ValueError):
        generate_reservations(
            members,
            books,
            count=0,
        )

def test_generate_branches_returns_requested_count() -> None:
    """Verify that the requested number of branches is generated."""
    branches = generate_branches(count=5)

    assert len(branches) == 5


def test_generate_branches_have_unique_ids() -> None:
    """Verify that branch IDs are unique."""
    branches = generate_branches(count=5)

    branch_ids = [branch["branch_id"] for branch in branches]

    assert len(branch_ids) == len(set(branch_ids))


def test_generate_branches_have_required_fields() -> None:
    """Verify that branches contain required fields."""
    branches = generate_branches(count=5)

    required_fields = {
        "branch_id",
        "name",
        "location",
        "opening_time",
        "closing_time",
    }

    for branch in branches:
        assert required_fields.issubset(branch.keys())


def test_generate_branches_rejects_invalid_count() -> None:
    """Verify that invalid branch counts are rejected."""
    with pytest.raises(ValueError):
        generate_branches(count=0)


def test_generate_branches_rejects_excessive_count() -> None:
    """Verify that branch counts beyond available definitions are rejected."""
    with pytest.raises(ValueError):
        generate_branches(count=6)


def test_generate_library_policies_returns_expected_values() -> None:
    """Verify that library policies contain the expected values."""
    policies = generate_library_policies()

    assert policies["loan_period_days"] == 14
    assert policies["overdue_fine_per_day"] == 2
    assert policies["membership_required"] is True


def test_generate_library_policies_contains_required_fields() -> None:
    """Verify that all required policy fields are present."""
    policies = generate_library_policies()

    required_fields = {
        "loan_period_days",
        "overdue_fine_per_day",
        "membership_required",
    }

    assert required_fields.issubset(policies.keys())



"""Tests for the catalogue repository."""




def test_get_books_returns_books() -> None:
    """Verify that the repository returns catalogue records."""
    books = get_books()

    assert books
    assert isinstance(books, list)


def test_get_books_returns_valid_book_records() -> None:
    """Verify that returned records contain required catalogue fields."""
    books = get_books()

    required_fields = {
        "book_id",
        "title",
        "author",
        "isbn",
        "publisher",
        "year",
        "genre",
        "classification",
        "pages",
        "language",
        "synopsis",
        "keywords",
    }

    for book in books:
        assert required_fields.issubset(book.keys())


def test_get_books_returns_expected_catalogue_size() -> None:
    """Verify that the complete dummy catalogue is returned."""
    books = get_books()

    assert len(books) == 1_500