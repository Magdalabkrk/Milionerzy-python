import random
from config import MONEY_LEVELS
from game import ask_question
from questions import load_questions


def main():
    questions = load_questions("data/questions.json")
    random.shuffle(questions)  # 👈 TUTAJ

    current_money = 0

    for index, question in enumerate(questions):
        if index >= len(MONEY_LEVELS):
            break

        print(f"\nPytanie za {MONEY_LEVELS[index]} zł")

        is_correct = ask_question(question)

        if not is_correct:
            print(f"Koniec gry. Wygrywasz: {current_money} zł")
            break

        current_money = MONEY_LEVELS[index]
        print(f"Aktualna wygrana: {current_money} zł")

    else:
        print("Gratulacje! Wygrałeś milion złotych!")


if __name__ == "__main__":
    main()