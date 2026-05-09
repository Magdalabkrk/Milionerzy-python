def ask_question(question: dict) -> bool:
    print("\n" + question["question"])

    letters = ["A", "B", "C", "D"]

    for index, answer in enumerate(question["answers"]):
        print(f"{letters[index]}. {answer}")

    user_answer = input("Twoja odpowiedź: ").upper()

    if user_answer not in letters:
        print("Niepoprawna odpowiedź.")
        return False

    selected_index = letters.index(user_answer)

    if selected_index == question["correct"]:
        print("Dobrze!")
        return True

    print("Źle!")
    return False