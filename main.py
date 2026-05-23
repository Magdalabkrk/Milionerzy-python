from results import save_result
import random
from config import MONEY_LEVELS
from game import ask_question
from questions import load_questions


def format_amount(amount: int) -> str:
    """Return amount with thousands grouped by a visible regular space.

    Some environments or locales may use commas or non-breaking spaces as
    thousands separators. Normalize any of those to a regular ASCII space
    so the separator is always visible in console/GUI output.
    """
    return f"{amount:,}".replace(",", " ").replace("\u00A0", " ").replace("\u202F", " ")


def main():
    questions_data = load_questions("data/questions.json")

    easy = questions_data["easy"]
    medium = questions_data["medium"]
    hard = questions_data["hard"]

    random.shuffle(easy)
    random.shuffle(medium)
    random.shuffle(hard)

    questions = (
        easy[:4] +
        medium[:4] +
        hard[:4]
    )

    current_money = 0
    lifelines = {
        "50": True,
        "audience": True,
        "phone": True
    }

    for index, question in enumerate(questions):
        if index >= len(MONEY_LEVELS):
            break

        print(f"\nPytanie za {format_amount(MONEY_LEVELS[index])} zł")
        
        is_correct = ask_question(question, lifelines)

        if not is_correct:
            print(f"Koniec gry. Wygrywasz: {format_amount(current_money)} zł")
            save_result(current_money)
            break

        current_money = MONEY_LEVELS[index]
        print(f"Aktualna wygrana: {format_amount(current_money)} zł")

    else:
        print("Gratulacje! Wygrałeś milion złotych!")
        save_result(current_money)


if __name__ == "__main__":
    main()
