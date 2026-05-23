def format_amount(amount: int) -> str:
    """Return amount with thousands grouped by a visible regular space.

    Normalize common thousands separators (comma, non-breaking spaces) to a regular
    ASCII space so the separator is visible in console/GUI output.
    """
    return f"{amount:,}".replace(",", " ").replace("\u00A0", " ").replace("\u202F", " ")
