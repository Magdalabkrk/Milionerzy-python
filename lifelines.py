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
    
def audience_help(question: dict) -> dict:
    correct = question["correct"]

    percentages = [0, 0, 0, 0]

    remaining = 100

    for i in range(4):
        if i == correct:
            continue

        value = random.randint(5, remaining // 2)
        percentages[i] = value
        remaining -= value

    percentages[correct] = remaining

    return {i: percentages[i] for i in range(4)}

def phone_friend(question: dict) -> int:
    correct = question["correct"]
    answers_count = len(question["answers"])

    if random.randint(1, 100) <= 75:
        return correct

    wrong_answers = [
        i for i in range(answers_count)
        if i != correct
    ]

    return random.choice(wrong_answers)