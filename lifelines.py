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

def phone_friend(question: dict) -> str:
    options = ["correct", "guide", "wrong_uncertain", "unknown"]

    chosen = random.choices(
        options,
        weights=[45, 30, 15, 10],
        k=1
    )[0]

    correct_answer = question["answers"][question["correct"]]

    if chosen == "correct":
        return f"Hmm... wydaje mi się, że poprawna odpowiedź to: {correct_answer}."

    if chosen == "guide":
        return "Nie dam głowy, ale spróbuj odrzucić najbardziej absurdalne odpowiedzi i pomyśl logicznie."

    if chosen == "wrong_uncertain":
        wrong_answers = [
            answer for index, answer in enumerate(question["answers"])
            if index != question["correct"]
        ]
        return f"Nie jestem pewien, ale chyba wybrałbym: {random.choice(wrong_answers)}."

    return "Kurczę, tego kompletnie nie wiem. Nie chcę Cię wprowadzić w błąd."