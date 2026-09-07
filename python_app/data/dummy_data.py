"""Generate realistic dummy data for the library management system."""

import random


BOOK_COUNT = 1_500

title_variations = [
    "Fundamentals",
    "Practical Guide",
    "Advanced Concepts",
    "A Complete Guide",
    "Modern Approaches",
    "Applications and Techniques",
    "Theory and Practice",
]



BOOK_TOPICS = {
    "Computer Science": [
        {
            "title": "Python Programming for Beginners",
            "keywords": ["python", "programming", "software development"],
            "description": (
                "A practical introduction to Python programming, "
                "covering variables, functions, data structures, "
                "modules, and object-oriented programming."
            ),
        },
        {
            "title": "Advanced Python Programming",
            "keywords": ["python", "programming", "advanced programming"],
            "description": (
                "Advanced Python concepts including decorators, "
                "generators, concurrency, testing, and application design."
            ),
        },
        {
            "title": "Database Management Systems",
            "keywords": ["database", "sql", "data management"],
            "description": (
                "Fundamentals of database systems, relational databases, "
                "SQL, normalization, transactions, and database design."
            ),
        },
        {
            "title": "Web Application Development",
            "keywords": ["web", "development", "programming"],
            "description": (
                "Principles of modern web application development, "
                "including APIs, application architecture, and deployment."
            ),
        },
    ],
    "Data Science": [
        {
            "title": "Introduction to Data Science",
            "keywords": ["data science", "statistics", "python"],
            "description": (
                "Introduction to data science using statistical methods, "
                "Python programming, data analysis, and visualization."
            ),
        },
        {
            "title": "Practical Data Analysis with Python",
            "keywords": ["data analysis", "python", "pandas"],
            "description": (
                "Practical techniques for cleaning, transforming, "
                "analysing, and visualizing data with Python."
            ),
        },
        {
            "title": "Statistics for Data Science",
            "keywords": ["statistics", "data science", "probability"],
            "description": (
                "Statistical concepts required for data science, "
                "including probability, distributions, and hypothesis testing."
            ),
        },
    ],
    "Artificial Intelligence": [
        {
            "title": "Machine Learning with Python",
            "keywords": ["machine learning", "python", "artificial intelligence"],
            "description": (
                "Machine learning concepts including supervised learning, "
                "unsupervised learning, model evaluation, and Python implementation."
            ),
        },
        {
            "title": "Deep Learning Fundamentals",
            "keywords": ["deep learning", "neural networks", "artificial intelligence"],
            "description": (
                "Fundamentals of neural networks, deep learning architectures, "
                "training techniques, and practical artificial intelligence applications."
            ),
        },
        {
            "title": "Natural Language Processing",
            "keywords": ["nlp", "natural language processing", "machine learning"],
            "description": (
                "Techniques for processing and analysing human language "
                "using machine learning and statistical methods."
            ),
        },
    ],
    "History": [
        {
            "title": "Ancient Indian Civilization",
            "keywords": ["india", "ancient history", "civilization"],
            "description": (
                "An overview of ancient Indian civilizations, "
                "their culture, society, economy, and historical development."
            ),
        },
        {
            "title": "Medieval Indian History",
            "keywords": ["india", "medieval history", "history"],
            "description": (
                "Major events, kingdoms, societies, and cultural developments "
                "in medieval Indian history."
            ),
        },
        {
            "title": "Modern Indian History",
            "keywords": ["india", "modern history", "independence"],
            "description": (
                "Important events and political developments in modern "
                "Indian history and the independence movement."
            ),
        },
    ],
    "Literature": [
        {
            "title": "Introduction to English Literature",
            "keywords": ["english literature", "literature", "poetry"],
            "description": (
                "An introduction to major literary movements, authors, "
                "poetry, drama, and fiction in English literature."
            ),
        },
        {
            "title": "Indian Literature",
            "keywords": ["indian literature", "literature", "fiction"],
            "description": (
                "A study of major Indian literary traditions, authors, "
                "themes, languages, and cultural influences."
            ),
        },
    ],
}

LANGUAGES = [
    "English",
    "Marathi",
    "Hindi",
]



PUBLISHERS = [
    "Oxford University Press",
    "Pearson",
    "McGraw Hill",
    "Cambridge University Press",
    "O'Reilly Media",
    "Penguin Books",
]

AUTHORS = [
    "James Wilson",
    "Robert Smith",
    "David Brown",
    "Michael Johnson",
    "William Taylor",
    "Daniel Anderson",
    "Thomas Martin",
    "Christopher Thomas",
    "John Jackson",
    "Richard White",
]


def validate_book(book: dict) -> None:
    """Validate the required fields of a generated book.

    Args:
        book: Book record to validate.

    Raises:
        ValueError: If a required field is missing or invalid.
    """
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

    missing_fields = required_fields - book.keys()

    if missing_fields:
        raise ValueError(
            f"Book is missing required fields: {sorted(missing_fields)}"
        )

    if not book["title"].strip():
        raise ValueError("Book title cannot be empty.")

    if not book["author"].strip():
        raise ValueError("Book author cannot be empty.")

    if book["pages"] <= 0:
        raise ValueError("Book pages must be greater than zero.")

def generate_books(
    count: int = BOOK_COUNT,
    seed: int = 42,
) -> list[dict]:
    """Generate deterministic and realistic library catalogue data.

    Args:
        count: Number of books to generate.
        seed: Random seed used for reproducible data generation.

    Returns:
        A list of generated book records.

    Raises:
        ValueError: If count is less than one.
    """
    if count < 1:
        raise ValueError("Book count must be greater than zero.")

    random_generator = random.Random(seed)

    topics = [
        (genre, book)
        for genre, books in BOOK_TOPICS.items()
        for book in books
    ]

    books = []
    

    for book_number in range(1, count + 1):
        genre, topic = random_generator.choice(topics)

        book = {
            "book_id": f"B{book_number:05d}",
            "title": (
                f"{topic['title']}: "
                f"{random_generator.choice(title_variations)} "
                f"{book_number}"
            ),
            "author": random_generator.choice(AUTHORS),
            "isbn": f"978000{book_number:07d}",
            "publisher": random_generator.choice(PUBLISHERS),
            "year": random_generator.randint(2000, 2026),
            "genre": genre,
            "classification": genre,
            "series": None,
            "pages": random_generator.randint(150, 700),
            "language": random_generator.choice(LANGUAGES),
            "synopsis": topic["description"],
            "keywords": topic["keywords"],
        }
        validate_book(book)
        books.append(book)      

    return books



COPY_COUNT = 3_000

BRANCH_IDS = [
    "BR001",
    "BR002",
    "BR003",
    "BR004",
    "BR005",
]

COPY_CONDITIONS = [
    "NEW",
    "GOOD",
    "FAIR",
    "DAMAGED",
]

COPY_STATUSES = [
    "AVAILABLE",
    "ON_LOAN",
    "LOST",
    "DAMAGED",
]




def _generate_shelf_location(
    random_generator: random.Random,
) -> str:
    """Generate a realistic library shelf location.

    Args:
        random_generator: Random generator used for reproducibility.

    Returns:
        A shelf location such as ``A-12``.
    """
    section = random_generator.choice(["A", "B", "C", "D", "E"])
    shelf_number = random_generator.randint(1, 50)

    return f"{section}-{shelf_number:02d}"

def generate_copies(
    books: list[dict],
    count: int = COPY_COUNT,
    seed: int = 42,
) -> list[dict]:
    """Generate physical copies associated with catalogue books.

    Args:
        books: Catalogue books that the copies belong to.
        count: Number of physical copies to generate.
        seed: Random seed used for reproducible data generation.

    Returns:
        A list of physical copy records.

    Raises:
        ValueError: If the book list is empty or count is less than one.
    """
    if not books:
        raise ValueError("At least one book is required.")

    if count < 1:
        raise ValueError("Copy count must be greater than zero.")

    random_generator = random.Random(seed)

    copies = []

    for copy_number in range(1, count + 1):
        book = random_generator.choice(books)
        branch_id = random_generator.choice(BRANCH_IDS)

        copy = {
            "copy_id": f"C{copy_number:05d}",
            "book_id": book["book_id"],
            "branch_id": branch_id,
            "shelf_location": _generate_shelf_location(
                random_generator
            ),
            "condition": random_generator.choice(COPY_CONDITIONS),
            "status": random_generator.choice(COPY_STATUSES),
        }

        copies.append(copy)

    return copies




MEMBER_COUNT = 750

MEMBER_STATUSES = [
    "ACTIVE",
    "INACTIVE",
    "SUSPENDED",
]

FIRST_NAMES = [
    "Aarav",
    "Aditya",
    "Akash",
    "Amit",
    "Ananya",
    "Anjali",
    "Deepak",
    "Karan",
    "Neha",
    "Priya",
    "Rahul",
    "Rohan",
    "Sneha",
    "Suresh",
    "Vikram",
]

LAST_NAMES = [
    "Sharma",
    "Patil",
    "Deshmukh",
    "Joshi",
    "Kulkarni",
    "Pawar",
    "More",
    "Jadhav",
    "Shinde",
    "Kadam",
]



def generate_members(
    count: int = MEMBER_COUNT,
    seed: int = 42,
) -> list[dict]:
    """Generate deterministic dummy library member records.

    Args:
        count: Number of members to generate.
        seed: Random seed used for reproducible data generation.

    Returns:
        A list of generated member records.

    Raises:
        ValueError: If count is less than one.
    """
    if count < 1:
        raise ValueError("Member count must be greater than zero.")

    random_generator = random.Random(seed)

    members = []

    for member_number in range(1, count + 1):
        first_name = random_generator.choice(FIRST_NAMES)
        last_name = random_generator.choice(LAST_NAMES)

        member = {
            "member_id": f"M{member_number:05d}",
            "name": f"{first_name} {last_name}",
            "status": random_generator.choice(MEMBER_STATUSES),
        }

        members.append(member)

    return members



BORROWING_PROFILES = {
    "technology": [
        "Computer Science",
        "Data Science",
        "Artificial Intelligence",
    ],
    "history": [
        "History",
    ],
    "literature": [
        "Literature",
    ],
    "science": [
        "Science",
        "Mathematics",
    ],
    "business": [
        "Business",
        "Economics",
    ],
}




def _group_books_by_genre(
    books: list[dict],
) -> dict[str, list[dict]]:
    """Group catalogue books by their genre.

    Args:
        books: Catalogue books to group.

    Returns:
        A dictionary mapping each genre to its books.
    """
    books_by_genre: dict[str, list[dict]] = {}

    for book in books:
        genre = book["genre"]
        books_by_genre.setdefault(genre, []).append(book)

    return books_by_genre



def _get_books_for_profile(
    profile_genres: list[str],
    books_by_genre: dict[str, list[dict]],
) -> list[dict]:
    """Return books matching a member's borrowing preferences.

    Args:
        profile_genres: Genres preferred by the member.
        books_by_genre: Books grouped by genre.

    Returns:
        Books that match the member's preferred genres.
    """
    matching_books = []

    for genre in profile_genres:
        matching_books.extend(books_by_genre.get(genre, []))

    return matching_books


LOAN_COUNT = 15_000
LOAN_PERIOD_DAYS = 14

from datetime import date, timedelta

def _group_copies_by_book(
    copies: list[dict],
) -> dict[str, list[dict]]:
    """Group physical copies by their catalogue book ID.

    Args:
        copies: Physical library copies to group.

    Returns:
        A dictionary mapping each book ID to its copies.
    """
    copies_by_book: dict[str, list[dict]] = {}

    for copy in copies:
        book_id = copy["book_id"]

        copies_by_book.setdefault(book_id, []).append(copy)

    return copies_by_book


def _assign_member_profiles(
    members: list[dict],
    random_generator: random.Random,
) -> dict[str, list[str]]:
    """Assign a borrowing preference profile to each member.

    Args:
        members: Library members.
        random_generator: Random generator used for reproducibility.

    Returns:
        A mapping of member IDs to preferred genres.
    """
    profile_names = list(BORROWING_PROFILES)

    return {
        member["member_id"]: BORROWING_PROFILES[
            random_generator.choice(profile_names)
        ]
        for member in members
    }

def _generate_return_date(
    issue_date: date,
    due_date: date,
    random_generator: random.Random,
) -> date:
    """Generate a realistic return date for a completed loan.

    Args:
        issue_date: Date when the book was issued.
        due_date: Date when the book was due.
        random_generator: Random generator used for reproducibility.

    Returns:
        A return date that may be before, on, or after the due date.
    """
    return_offset = random_generator.randint(
        3,
        LOAN_PERIOD_DAYS + 7,
    )

    return issue_date + timedelta(days=return_offset)

def generate_loans(
    members: list[dict],
    books: list[dict],
    copies: list[dict],
    count: int = LOAN_COUNT,
    seed: int = 42,
) -> list[dict]:
    """Generate realistic historical library loan records.

    Args:
        members: Library members who borrow books.
        books: Catalogue books available for borrowing.
        copies: Physical copies belonging to catalogue books.
        count: Number of loan records to generate.
        seed: Random seed used for reproducible data generation.

    Returns:
        A list of generated historical loan records.

    Raises:
        ValueError: If required collections are empty or count is invalid.
    """
    if not members:
        raise ValueError("At least one member is required.")

    if not books:
        raise ValueError("At least one book is required.")

    if not copies:
        raise ValueError("At least one copy is required.")

    if count < 1:
        raise ValueError("Loan count must be greater than zero.")

    random_generator = random.Random(seed)

    books_by_genre = _group_books_by_genre(books)
    copies_by_book = _group_copies_by_book(copies)
    member_profiles = _assign_member_profiles(
        members,
        random_generator,
    )

    loans = []

    for loan_number in range(1, count + 1):
        member = random_generator.choice(members)

        preferred_genres = member_profiles[
            member["member_id"]
        ]

        preferred_books = _get_books_for_profile(
            preferred_genres,
            books_by_genre,
        )

        if not preferred_books:
            preferred_books = books

        available_books = [
            book
            for book in preferred_books
            if book["book_id"] in copies_by_book
        ]

        if not available_books:
            available_books = list(copies_by_book)

        book = random_generator.choice(available_books)

        book_copies = copies_by_book[book["book_id"]]
        copy = random_generator.choice(book_copies)

        copy = random_generator.choice(book_copies)

        issue_date = date(
            2025,
            1,
            1,
        ) + timedelta(
            days=random_generator.randint(0, 364),
        )

        due_date = issue_date + timedelta(
            days=LOAN_PERIOD_DAYS,
        )

        return_date = _generate_return_date(
            issue_date,
            due_date,
            random_generator,
        )

        loan = {
            "loan_id": f"L{loan_number:05d}",
            "member_id": member["member_id"],
            "book_id": book["book_id"],
            "copy_id": copy["copy_id"],
            "issue_date": issue_date,
            "due_date": due_date,
            "return_date": return_date,
        }

        loans.append(loan)

    return loans



RESERVATION_COUNT = 3_000

RESERVATION_STATUSES = [
    "ACTIVE",
    "FULFILLED",
    "CANCELLED",
    "EXPIRED",
]


def generate_reservations(
    members: list[dict],
    books: list[dict],
    count: int = RESERVATION_COUNT,
    seed: int = 42,
) -> list[dict]:
    """Generate deterministic reservation records.

    Reservations reference existing members and books and contain
    realistic reservation dates and statuses.

    Args:
        members: List of library member records.
        books: List of catalogue book records.
        count: Number of reservations to generate.
        seed: Random seed used for reproducible data generation.

    Returns:
        A list of generated reservation records.

    Raises:
        ValueError: If members or books are empty, or count is invalid.
    """
    if not members:
        raise ValueError("Members cannot be empty.")

    if not books:
        raise ValueError("Books cannot be empty.")

    if count < 1:
        raise ValueError("Reservation count must be greater than zero.")

    random_generator = random.Random(seed)

    member_ids = [member["member_id"] for member in members]
    book_ids = [book["book_id"] for book in books]

    reservations = []

    start_date = date(2025, 1, 1)
    end_date = date(2026, 8, 31)
    date_range_days = (end_date - start_date).days

    for reservation_number in range(1, count + 1):
        reservation_date = start_date + timedelta(
            days=random_generator.randint(0, date_range_days)
        )

        status = random_generator.choice(RESERVATION_STATUSES)

        reservation = {
            "reservation_id": f"R{reservation_number:05d}",
            "member_id": random_generator.choice(member_ids),
            "book_id": random_generator.choice(book_ids),
            "reservation_date": reservation_date,
            "status": status,
        }

        reservations.append(reservation)

    return reservations


BRANCH_COUNT = 5

BRANCH_NAMES = [
    "Central Library",
    "North Branch",
    "South Branch",
    "East Branch",
    "West Branch",
]

BRANCH_LOCATIONS = [
    "Main Campus",
    "North Campus",
    "South Campus",
    "East Campus",
    "West Campus",
]

def generate_branches(
    count: int = BRANCH_COUNT,
) -> list[dict]:
    """Generate library branch records.

    Args:
        count: Number of branches to generate.

    Returns:
        A list of branch records.

    Raises:
        ValueError: If count is less than one or exceeds available
            branch definitions.
    """
    if count < 1:
        raise ValueError("Branch count must be greater than zero.")

    if count > len(BRANCH_NAMES):
        raise ValueError("Branch count exceeds available branch definitions.")

    branches = []

    for branch_number in range(count):
        branch = {
            "branch_id": f"BR{branch_number + 1:03d}",
            "name": BRANCH_NAMES[branch_number],
            "location": BRANCH_LOCATIONS[branch_number],
            "opening_time": "09:00",
            "closing_time": "18:00",
        }

        branches.append(branch)

    return branches

LOAN_PERIOD_DAYS = 14
OVERDUE_FINE_PER_DAY = 2

OVERDUE_FINE_PER_DAY = 2

def generate_library_policies() -> dict:
    """Generate library policy configuration.

    Returns:
        A dictionary containing the library's operational policies.
    """
    return {
        "loan_period_days": LOAN_PERIOD_DAYS,
        "overdue_fine_per_day": OVERDUE_FINE_PER_DAY,
        "membership_required": True,
    }
