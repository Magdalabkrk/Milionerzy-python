def ask_question(question: dict) -> bool:
    print("\n" + question["question"])

    letters = ["A", "B", "C", "D"]

    for index, answer in enumerate(question["answers"]):
        print(f"{letters[index]}. {answer}")

    while True:  # 👈 TO DODAJEMY
        user_answer = input("Twoja odpowiedź (A/B/C/D): ").upper()

        if user_answer in letters:
            break

        print("Niepoprawny wybór, spróbuj ponownie.")

    selected_index = letters.index(user_answer)

    if selected_index == question["correct"]:
        print("Dobrze!")
        return True

    print(f"Źle! Poprawna odpowiedź to: {letters[question['correct']]}")
    return False