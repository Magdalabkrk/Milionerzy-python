import random


def fifty_fifty(question: dict) -> list:
    # Zwracamy listę indeksów odpowiedzi, które pozostają po usunięciu dwóch błędnych.
    correct_index = question["correct"]

    wrong_answers = [
        i for i in range(len(question["answers"]))
        if i != correct_index
    ]

    # Losowo wybieramy dwie odpowiedzi do usunięcia
    removed = random.sample(wrong_answers, 2)
    return [
        i for i in range(len(question["answers"]))
        if i not in removed
    ]
    
def audience_help(question: dict) -> dict:
    # Symulacja głosowania publiczności — zwraca procenty dla każdej opcji
    correct = question["correct"]

    percentages = [0, 0, 0, 0]

    remaining = 100

    # Przydzielamy losowe wartości do odpowiedzi błędnych, a na końcu resztę
    # zostawiamy dla poprawnej odpowiedzi (dzięki temu poprawna ma największy udział)
    for i in range(4):
        if i == correct:
            continue

        value = random.randint(5, remaining // 2)
        percentages[i] = value
        remaining -= value

    percentages[correct] = remaining

    # Zwracamy w formie słownika {index: percent}
    return {i: percentages[i] for i in range(4)}

def phone_friend(question: dict) -> str:
    # Symulacja telefonu do przyjaciela — czasem pewna odpowiedź, czasem wskazówka
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