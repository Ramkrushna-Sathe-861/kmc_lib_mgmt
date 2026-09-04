"""Dummy library data used during local development."""

from python_app.schemas.search import Book


BOOKS = [
    Book(
        id=1,
        title="Python Crash Course",
        author="Eric Matthes",
        subject="Python Programming",
        description=(
            "A practical introduction to Python programming "
            "with projects and examples."
        ),
        isbn="9781593279288",
    ),
    Book(
        id=2,
        title="Hands-On Machine Learning",
        author="Aurélien Géron",
        subject="Machine Learning",
        description=(
            "Machine learning using Python with practical "
            "examples and algorithms."
        ),
        isbn="9781098125974",
    ),
    Book(
        id=3,
        title="Learning Python",
        author="Mark Lutz",
        subject="Python Programming",
        description=(
            "A comprehensive guide to Python programming "
            "language and its features."
        ),
        isbn="9781449355739",
    ),
    Book(
        id=4,
        title="Clean Code",
        author="Robert C. Martin",
        subject="Software Engineering",
        description=(
            "Principles and practices for writing clean, "
            "maintainable software."
        ),
        isbn="9780132350884",
    ),
    Book(
        id=5,
        title="Deep Learning",
        author="Ian Goodfellow",
        subject="Artificial Intelligence",
        description=(
            "Introduction to deep learning, neural networks, "
            "and artificial intelligence."
        ),
        isbn="9780262035613",
    ),
]


LOANS = [
    {"user_id": 101, "book_id": 1},
    {"user_id": 101, "book_id": 2},
    {"user_id": 102, "book_id": 1},
    {"user_id": 102, "book_id": 3},
    {"user_id": 103, "book_id": 2},
    {"user_id": 103, "book_id": 5},
    {"user_id": 104, "book_id": 1},
    {"user_id": 104, "book_id": 2},
    {"user_id": 104, "book_id": 5},
]