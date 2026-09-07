"""Data access functions for the library catalogue."""

import pandas as pd

from python_app.data.real_data.data_store import get_library_data


def get_books() -> pd.DataFrame:
    """Return the library catalogue.

    Returns:
        DataFrame containing unique catalogue records.
    """
    return get_library_data()["books"]