"""In-memory access to the loaded library dataset."""

from pathlib import Path

import pandas as pd

from python_app.data.real_data.library_data_loader import load_library_data


_DATA_CACHE: dict[str, pd.DataFrame] | None = None


def get_library_data(
    file_path: Path | None = None,
) -> dict[str, pd.DataFrame]:
    """Load library data once and reuse it.

    Args:
        file_path: Optional path to the library dataset.

    Returns:
        Dictionary containing books, members, and loans DataFrames.
    """
    global _DATA_CACHE

    if _DATA_CACHE is None:
        if file_path is None:
            _DATA_CACHE = load_library_data()
        else:
            _DATA_CACHE = load_library_data(file_path)

    return _DATA_CACHE