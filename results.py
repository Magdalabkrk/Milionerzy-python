import json
from pathlib import Path


def save_result(amount: int):
    path = Path("data/results.json")

    # jeśli plik istnieje → wczytaj
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            results = json.load(f)
    else:
        results = []

    # dodaj nowy wynik
    results.append({"score": amount})

    # zapisz z powrotem
    with path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)