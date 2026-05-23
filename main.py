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


# main.py — wersja konsolowa gry
# Komentarze po polsku (ludzkim stylem) opisują krok po kroku, co się dzieje
def main():
    # Wczytujemy pytania z pliku JSON i rozdzielamy je według trudności.
    # Dzięki temu możemy wziąć po kilka pytań z każdej kategorii.
    questions_data = load_questions("data/questions.json")

    easy = questions_data["easy"]
    medium = questions_data["medium"]
    hard = questions_data["hard"]

    # Tasujemy listy pytań — każdy start ma mieć element losowości
    random.shuffle(easy)
    random.shuffle(medium)
    random.shuffle(hard)

    # Tworzymy listę pytań do gry: 4 łatwe, 4 średnie i 4 trudne
    questions = (
        easy[:4] +
        medium[:4] +
        hard[:4]
    )

    # Stan gry: ile aktualnie wygrane oraz które koła są dostępne
    current_money = 0
    lifelines = {
        "50": True,
        "audience": True,
        "phone": True
    }

    # Główna pętla gry — iterujemy przez listę pytań
    for index, question in enumerate(questions):
        # Safety: jeśli lista MONEY_LEVELS jest krótsza niż liczba pytań — przerywamy
        if index >= len(MONEY_LEVELS):
            break

        # Pokazujemy informację, o jakie pieniądze jest pytanie.
        # Używamy format_amount żeby separator tysięcy był czytelny.
        print(f"\nPytanie za {format_amount(MONEY_LEVELS[index])} zł")
        
        # Zadajemy pytanie (funkcja ask_question zwraca True/False)
        is_correct = ask_question(question, lifelines)

        # Jeśli gracz odpowie źle — koniec gry: zapisujemy wynik i wychodzimy
        if not is_correct:
            print(f"Koniec gry. Wygrywasz: {format_amount(current_money)} zł")
            save_result(current_money)
            break

        # Jeśli poprawnie — aktualizujemy aktualną wygraną i kontynuujemy
        current_money = MONEY_LEVELS[index]
        print(f"Aktualna wygrana: {format_amount(current_money)} zł")

    else:
        # Jeśli pętla zakończy się normalnie (bez break) — gracz przeszedł wszystkie pytania
        print("Gratulacje! Wygrałeś milion złotych!")
        save_result(current_money)


if __name__ == "__main__":
    main()
