"""Data access functions for library policies."""

from python_app.data.dummy_data import generate_library_policies


def get_library_policies() -> dict:
    """Return the current library policies.

    Returns:
        A dictionary containing library policy configuration.
    """
    return generate_library_policies()