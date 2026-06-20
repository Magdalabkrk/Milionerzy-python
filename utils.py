def format_amount(amount: int) -> str:
    return f"{amount:,}".replace(",", " ").replace("\u00A0", " ").replace("\u202F", " ")
