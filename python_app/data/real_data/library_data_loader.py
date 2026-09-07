"""Load and normalize the real public library dataset."""

from pathlib import Path

import pandas as pd


DEFAULT_DATASET_PATH = (
    Path(__file__).resolve().parent / "datasetPublicLib.csv"
)

COLUMN_MAPPING = {
    "Membership Number": "member_id",
    "Book ID Number": "book_id",
    "Book Title": "title",
    "Location Code": "location_code",
    "Place of Birth": "place_of_birth",
    "Date of Birth": "date_of_birth",
    "Gender": "gender",
    "Member type": "member_type",
    "Join Year": "join_year",
    "BIBID": "bib_id",
    "ISBN": "isbn",
    "DDC Number": "ddc_number",
    "Author": "author",
    "Publisher Name": "publisher",
    "Trx at the year of": "transaction_year",
    "Borrow Duration (days)": "borrow_duration_days",
    "Borrow Date": "borrow_date",
    "Return Date": "return_date",
}


def load_library_dataset(
    file_path: Path = DEFAULT_DATASET_PATH,
) -> pd.DataFrame:
    """Load the library CSV dataset.

    Args:
        file_path: Path to the library CSV file.

    Returns:
        A DataFrame containing the raw library transactions.

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If the dataset is empty or missing required columns.
    """
    if not file_path.exists():
        raise FileNotFoundError(
            f"Library dataset not found: {file_path}"
        )

    dataframe = pd.read_csv(
        file_path,
        sep=";",
        low_memory=False,
    )

    if dataframe.empty:
        raise ValueError("Library dataset is empty.")

    missing_columns = set(COLUMN_MAPPING) - set(dataframe.columns)

    if missing_columns:
        raise ValueError(
            f"Dataset is missing required columns: {missing_columns}"
        )

    return dataframe


def normalize_library_dataset(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Normalize column names and common data fields.

    Args:
        dataframe: Raw library dataset.

    Returns:
        A cleaned DataFrame with normalized column names.
    """
    normalized = dataframe.rename(columns=COLUMN_MAPPING).copy()

    normalized["member_id"] = (
        normalized["member_id"]
        .astype("Int64")
        .astype(str)
    )

    normalized["book_id"] = (
        normalized["book_id"]
        .astype("Int64")
        .astype(str)
    )

    normalized["title"] = normalized["title"].fillna("").str.strip()
    normalized["author"] = normalized["author"].fillna("").str.strip()
    normalized["publisher"] = (
        normalized["publisher"]
        .fillna("")
        .str.strip()
    )

    normalized["isbn"] = (
        normalized["isbn"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    normalized["ddc_number"] = (
        normalized["ddc_number"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    normalized["borrow_date"] = pd.to_datetime(
        normalized["borrow_date"],
        format="%d/%m/%y",
        errors="coerce",
    )

    normalized["return_date"] = pd.to_datetime(
        normalized["return_date"],
        format="%d/%m/%y",
        errors="coerce",
    )

    return normalized


def load_and_normalize_library_dataset(
    file_path: Path = DEFAULT_DATASET_PATH,
) -> pd.DataFrame:
    """Load and normalize the complete library dataset.

    Args:
        file_path: Path to the library CSV file.

    Returns:
        A cleaned and normalized library DataFrame.
    """
    dataframe = load_library_dataset(file_path)

    return normalize_library_dataset(dataframe)



def extract_books(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Extract unique book catalogue records.

    Args:
        dataframe: Normalized library transaction data.

    Returns:
        A DataFrame containing unique books.
    """
    book_columns = [
        "book_id",
        "title",
        "isbn",
        "ddc_number",
        "author",
        "publisher",
        "location_code",
    ]

    books = dataframe[book_columns].copy()

    return books.drop_duplicates(
        subset=["book_id"],
    ).reset_index(drop=True)


def extract_members(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Extract unique library members.

    Args:
        dataframe: Normalized library transaction data.

    Returns:
        A DataFrame containing unique members.
    """
    member_columns = [
        "member_id",
        "place_of_birth",
        "date_of_birth",
        "gender",
        "member_type",
        "join_year",
    ]

    members = dataframe[member_columns].copy()

    return members.drop_duplicates(
        subset=["member_id"],
    ).reset_index(drop=True)


def extract_loans(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Extract borrowing transaction records.

    Args:
        dataframe: Normalized library transaction data.

    Returns:
        A DataFrame containing loan transactions.
    """
    loan_columns = [
        "member_id",
        "book_id",
        "borrow_date",
        "return_date",
        "borrow_duration_days",
        "transaction_year",
    ]

    return dataframe[loan_columns].copy()



def load_library_data(
    file_path: Path = DEFAULT_DATASET_PATH,
) -> dict[str, pd.DataFrame]:
    """Load the dataset and return logical library data tables.

    Args:
        file_path: Path to the library CSV file.

    Returns:
        Dictionary containing books, members, and loans DataFrames.
    """
    dataframe = load_and_normalize_library_dataset(file_path)

    return {
        "books": extract_books(dataframe),
        "members": extract_members(dataframe),
        "loans": extract_loans(dataframe),
    }