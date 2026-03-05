def normalize_query(query: str):
    """
    Clean and normalize search queries.
    """
    if not query:
        return ""
    return query.strip().lower()