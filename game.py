from lifelines import audience_help, fifty_fifty, phone_friend


def ask_question(question: dict, lifelines: dict) -> bool:
    # Wyświetlamy treść pytania w konsoli
    print("\n" + question["question"])

    letters = ["A", "B", "C", "D"]
    # available_answers trzyma indeksy odpowiedzi, które są nadal widoczne
    available_answers = list(range(len(question["answers"])))

    # Pętla przyjmuje wejście od użytkownika dopóki nie padnie prawidłowa lub błędna odpowiedź
    while True:
        # Wyświetl dostępne odpowiedzi (pomijamy te usunięte przez 50/50)
        for index in available_answers:
            print(f"{letters[index]}. {question['answers'][index]}")

        print("\nWpisz A/B/C/D, '50', 'P' (publiczność) albo 'T' (telefon)")
        user_answer = input("Twoja odpowiedź: ").upper()

        # Obsługa 50/50 — usuwa dwie błędne odpowiedzi
        if user_answer == "50":
            if not lifelines["50"]:
                print("Koło 50/50 już wykorzystane.")
                continue

            available_answers = fifty_fifty(question)
            lifelines["50"] = False
            print("\nUżyto koła 50/50!")
            continue

        # Obsługa publiczności — wyświetlamy procenty
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

        # Obsługa telefonu do przyjaciela — symulowana wiadomość
        if user_answer == "T":
            if not lifelines["phone"]:
                print("Telefon do przyjaciela już wykorzystany.")
                continue

            message = phone_friend(question)
            lifelines["phone"] = False

            print("\nPrzyjaciel mówi:")
            print(message)
            continue

        # Jeśli odpowiedź to jedna z liter — sprawdzamy ją
        if user_answer in letters:
            selected_index = letters.index(user_answer)

            # Jeśli odpowiedź została wcześniej usunięta (50/50), informujemy
            if selected_index not in available_answers:
                print("Ta odpowiedź została usunięta.")
                continue

            # Zwracamy True/False w zależności od poprawności
            if selected_index == question["correct"]:
                print("Dobrze!")
                return True

            print(f"Źle! Poprawna odpowiedź to: {letters[question['correct']]}")
            return False

        # Nieznane wejście — pytamy ponownie
        print("Niepoprawny wybór.")