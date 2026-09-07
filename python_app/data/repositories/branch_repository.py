"""Data access functions for library branches."""

from python_app.data.dummy_data import generate_branches


def get_branches() -> list[dict]:
    """Return all library branches.

    Returns:
        A list of branch records.
    """
    return generate_branches()