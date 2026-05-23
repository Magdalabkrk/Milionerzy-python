import json
from pathlib import Path


def load_questions(file_path: str) -> dict:
    """Ładuje pytania z pliku JSON.

    Funkcja otwiera podany plik JSON, odczytuje jego zawartość i zwraca
    strukturę danych (słownik), która zawiera pytania pogrupowane według
    trudności.

    Args:
        file_path (str): Ścieżka do pliku JSON z pytaniami.

    Returns:
        dict: Struktura danych zawierająca pytania pogrupowane po trudności.
    """
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data