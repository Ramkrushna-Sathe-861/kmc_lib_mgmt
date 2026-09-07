"""Data access functions for library members."""

import pandas as pd

from python_app.data.real_data.data_store import get_library_data


def get_members() -> pd.DataFrame:
    """Return library members.

    Returns:
        DataFrame containing unique library members.
    """
    return get_library_data()["members"]