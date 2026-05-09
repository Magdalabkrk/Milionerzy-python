from lifelines import fifty_fifty

def ask_question(question: dict, lifelines: dict) -> bool:
    print("\n" + question["question"])

    letters = ["A", "B", "C", "D"]

    available_answers = list(range(len(question["answers"])))

    while True:
        for index in available_answers:
            print(f"{letters[index]}. {question['answers'][index]}")

        print("\nWpisz A/B/C/D lub '50' dla koła 50/50")

        user_answer = input("Twoja odpowiedź: ").upper()

        if user_answer == "50":
            if not lifelines["50"]:
                print("Koło 50/50 już wykorzystane.")
                continue

            available_answers = fifty_fifty(question)
            lifelines["50"] = False
            print("\nUżyto koła 50/50!")
            continue

        if user_answer in letters:
            selected_index = letters.index(user_answer)

            if selected_index not in available_answers:
                print("Ta odpowiedź została usunięta.")
                continue

            if selected_index == question["correct"]:
                print("Dobrze!")
                return True

            print(f"Źle! Poprawna odpowiedź to: {letters[question['correct']]}")
            return False

        print("Niepoprawny wybór.")