"""Repository functions for library catalogue data."""

import pandas as pd

from python_app.database.mysql_connection import get_database_connection


def get_books() -> pd.DataFrame:
    """Fetch active books from the library catalogue."""
    query = """
        SELECT
            book_id,
            book_name,
            author_name,
            publisher,
            isbn_no,
            published_year,
            genre,
            pages,
            book_language,
            synopsis,
            edition,
            dewey_class,
            subject_tags
        FROM book_details
        WHERE deleted_date IS NULL
    """

    connection = get_database_connection()

    try:
        return pd.read_sql(query, connection)
    finally:
        connection.close()