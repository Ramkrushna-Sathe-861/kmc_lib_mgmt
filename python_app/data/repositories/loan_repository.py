"""Data access functions for library loans."""

import pandas as pd

from python_app.data.real_data.data_store import get_library_data


def get_loans() -> pd.DataFrame:
    """Return library borrowing transactions.

    Returns:
        DataFrame containing loan transactions.
    """
    return get_library_data()["loans"]