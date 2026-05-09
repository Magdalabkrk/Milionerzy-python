from config import GAME_TITLE, QUESTIONS_FILE
from lifelines import Lifelines
from questions import load_questions


class Game:
    def __init__(self) -> None:
        self.title = GAME_TITLE
        self.questions_file = QUESTIONS_FILE
        self.lifelines = Lifelines()

    def run(self) -> None:
        print(self.title)
        questions = load_questions(self.questions_file)

        if not questions:
            print("Brak pytań w pliku data/questions.json.")
            return

        print(f"Załadowano {len(questions)} pytań.")
