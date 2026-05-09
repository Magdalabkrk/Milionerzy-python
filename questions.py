import json
from pathlib import Path


def load_questions(file_path: str) -> list:
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data