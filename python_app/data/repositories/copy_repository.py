"""Repository functions for physical book copies."""

import pandas as pd

from python_app.database.mysql_connection import get_database_connection


def get_book_copies() -> pd.DataFrame:
    """Fetch physical book copy and branch information."""
    query = """
        SELECT
            bc.book_copy_id,
            bc.book_id,
            bc.branch_id,
            bm.branch_name,
            bc.shelf,
            bc.accession,
            bc.book_condition,
            bc.book_status
        FROM book_copies AS bc
        LEFT JOIN branch_master AS bm
            ON bc.branch_id = bm.branch_id
    """

    connection = get_database_connection()

    try:
        return pd.read_sql(query, connection)
    finally:
        connection.close()