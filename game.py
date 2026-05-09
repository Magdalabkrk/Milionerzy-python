from lifelines import audience_help, fifty_fifty, phone_friend


def ask_question(question: dict, lifelines: dict) -> bool:
    print("\n" + question["question"])

    letters = ["A", "B", "C", "D"]
    available_answers = list(range(len(question["answers"])))

    while True:
        for index in available_answers:
            print(f"{letters[index]}. {question['answers'][index]}")

        print("\nWpisz A/B/C/D, '50', 'P' (publiczność) albo 'T' (telefon)")
        user_answer = input("Twoja odpowiedź: ").upper()

        if user_answer == "50":
            if not lifelines["50"]:
                print("Koło 50/50 już wykorzystane.")
                continue

            available_answers = fifty_fifty(question)
            lifelines["50"] = False
            print("\nUżyto koła 50/50!")
            continue

        if user_answer == "P":
            if not lifelines["audience"]:
                print("Publiczność już wykorzystana.")
                continue

            results = audience_help(question)
            lifelines["audience"] = False

            print("\nPubliczność podpowiada:")
            for index, percent in results.items():
                print(f"{letters[index]}: {percent}%")

            continue

        if user_answer == "T":
            if not lifelines["phone"]:
                print("Telefon do przyjaciela już wykorzystany.")
                continue

            suggested_index = phone_friend(question)
            lifelines["phone"] = False
            print(f"\nPrzyjaciel sugeruje odpowiedź: {letters[suggested_index]}")
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