from questions import load_questions
from game import ask_question


def main():
    questions = load_questions("data/questions.json")

    for question in questions:
        is_correct = ask_question(question)

        if not is_correct:
            print("Koniec gry.")
            break


if __name__ == "__main__":
    main()