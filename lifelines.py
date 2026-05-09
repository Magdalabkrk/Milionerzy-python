import random


def fifty_fifty(question: dict) -> list:
    correct_index = question["correct"]

    wrong_answers = [
        i for i in range(len(question["answers"]))
        if i != correct_index
    ]

    removed = random.sample(wrong_answers, 2)
    return [
        i for i in range(len(question["answers"]))
        if i not in removed
    ]