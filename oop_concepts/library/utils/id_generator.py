"""
ID Generator Utility
====================
Generates unique IDs for library entities.
"""

import uuid

def generate_id(prefix):
    """
    Generates a unique ID with a given prefix.

    Args:
        prefix (str): Prefix for the ID (e.g., "BK" for books, "MG" for magazines).

    Returns:
        str: A unique ID in the format <prefix>-<8-character UUID>.
    """
    return f"{prefix}-{uuid.uuid4().hex[:8]}"
