# GUI aplikacji Milionerzy (wersja Tkinter)
# Tutaj znajdują się wszystkie elementy interfejsu: etykiety, przyciski,
# obsługa kół ratunkowych i wyświetlanie komunikatów. Komentarze napisane
# prostym, "ludzkim" stylem — tak jakby opisywał to kolega z projektu.

import tkinter as tk
import random
import json
from pathlib import Path

from config import MONEY_LEVELS
from questions import load_questions
from lifelines import fifty_fifty, audience_help, phone_friend
from results import save_result
from utils import format_amount


# Kolory i stałe wyglądu używane w całym GUI — łatwo je zmienić w jednym miejscu
BG = "#101820"
CARD = "#1f2a36"
GOLD = "#f2c94c"
WHITE = "#ffffff"
BLUE = "#2f80ed"
GREEN = "#27ae60"
RED = "#eb5757"


class MillionairesGUI:
    # Klasa, która odpowiada za cały interfejs gry.
    # Tworzymy okno, przyciski odpowiedzi, etykiety z pytaniem, paskiem postępu
    # i przyciskami kół ratunkowych. Wszystko w jednym miejscu, żeby łatwo było
    # zmienić wygląd lub zachowanie GUI.
    def __init__(self, root):
        # root — główne okno tkintera przekazane przy uruchomieniu
        self.root = root
        self.root.title("Milionerzy")

        # Ustawiamy domyślny rozmiar okna oraz minimalny rozmiar — tak, żeby
        # elementy miały wystarczająco miejsca i nie trzeba było manualnie
        # zmieniać rozmiaru przy uruchomieniu.
        self.root.geometry("900x750")
        self.root.minsize(900, 750)
        # Wypośrodkuj okno na ekranie po ustawieniu rozmiaru
        self.center_window()
        self.root.config(bg=BG)

        # Przy starcie ustawiamy stan gry, mieszamy pytania itd.
        self.start_new_game()

        # Etykieta na samo pytanie + tytuł z kwotą
        # wraplength dopasowuje szerokość zawijania tekstu — ważne przy dłuższych pytaniach
        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 18, "bold"),
            wraplength=760,
            bg=CARD,
            fg=WHITE,
            padx=25,
            pady=25
        )
        # Odstęp wokół etykiety, żeby nie przyklejała się do górnej krawędzi
        self.question_label.pack(pady=30)

        # Przyciski odpowiedzi (A/B/C/D)
        # Trzymając je w liście łatwo manipulować (wyłączać, zmieniać kolor)
        self.answer_buttons = []

        for i in range(4):
            button = tk.Button(
                root,
                text="",
                font=("Arial", 13, "bold"),
                width=55,
                bg=BLUE,
                fg=WHITE,
                activebackground=GOLD,
                activeforeground=BG,
                command=lambda index=i: self.check_answer(index)
            )
            button.pack(pady=6)
            self.answer_buttons.append(button)

        # Etykieta pokazująca aktualną wygraną — aktualizowana po poprawnej odpowiedzi
        self.money_label = tk.Label(
            root,
            text="",
            font=("Arial", 14, "bold"),
            bg=BG,
            fg=GOLD
        )
        self.money_label.pack(pady=15)

        # Pasek postępu (np. "Pytanie 3/12") — informacyjny
        self.progress_label = tk.Label(
            root,
            text="",
            font=("Arial", 12, "bold"),
            bg=BG,
            fg=WHITE
        )
        self.progress_label.pack(pady=5)

        # Przyciski kół ratunkowych — od razu przypisane metody obsługi
        self.fifty_button = tk.Button(
            root,
            text="50/50",
            bg=GOLD,
            fg=BG,
            font=("Arial", 11, "bold"),
            command=self.use_fifty_fifty
        )
        self.fifty_button.pack(pady=3)

        self.audience_button = tk.Button(
            root,
            text="Publiczność",
            bg=GOLD,
            fg=BG,
            font=("Arial", 11, "bold"),
            command=self.use_audience
        )
        self.audience_button.pack(pady=3)

        self.phone_button = tk.Button(
            root,
            text="Telefon",
            bg=GOLD,
            fg=BG,
            font=("Arial", 11, "bold"),
            command=self.use_phone
        )
        self.phone_button.pack(pady=3)

        # Restart i historia wyników — przyciski pomocnicze umieszczone niżej
        self.restart_button = tk.Button(
            root,
            text="Zagraj od nowa",
            bg=WHITE,
            fg=BG,
            font=("Arial", 11, "bold"),
            command=self.restart_game
        )
        self.restart_button.pack(pady=10)

        self.results_button = tk.Button(
            root,
            text="Historia wyników",
            bg=WHITE,
            fg=BG,
            font=("Arial", 11, "bold"),
            command=self.show_results
        )
        self.results_button.pack(pady=5)

        # Pole informacyjne — gdy chcemy wyświetlić tekstowe informacje lub krótkie podpowiedzi
        # (fallback, gdy modal nie może być użyty)
        self.info_label = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            wraplength=760,
            bg=BG,
            fg=WHITE
        )
        self.info_label.pack(pady=10)

        # Załaduj pierwsze pytanie do widoku
        self.load_question()

    def center_window(self):
        # Prosta funkcja wyśrodkowująca okno na ekranie. Przydatne, żeby aplikacja
        # nie zawsze startowała w lewym górnym rogu.
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        if w == 1 and h == 1:
            # Na niektórych platformach wymiary nie są jeszcze ustawione —
            # użyj wartości domyślnych, które ustawiliśmy wcześniej.
            w, h = 900, 750
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def show_modal_message(self, title: str, message: str, width: int = 600, height: int = 200):
        # Tworzy proste modalne okienko (Toplevel) wyświetlające tekst i przycisk OK.
        # Używamy go dla lifelines (publiczność / telefon), żeby dłuższe wiadomości
        # były zawsze widoczne niezależnie od rozmiaru głównego okna.
        modal = tk.Toplevel(self.root)
        modal.title(title)
        modal.transient(self.root)
        modal.grab_set()

        # Center dialog relative to parent window — ładniej to wygląda niż lewy górny róg
        self.root.update_idletasks()
        rx = self.root.winfo_rootx()
        ry = self.root.winfo_rooty()
        rw = self.root.winfo_width()
        rh = self.root.winfo_height()

        x = rx + (rw // 2) - (width // 2)
        y = ry + (rh // 2) - (height // 2)
        modal.geometry(f"{width}x{height}+{x}+{y}")

        # Etykieta wewnątrz modala — wraplength = width-40 żeby tekst się ładnie łamał
        label = tk.Label(modal, text=message, wraplength=width-40, justify="left", bg=BG, fg=WHITE, font=("Arial", 12))
        label.pack(padx=20, pady=20, expand=True, fill="both")

        # Przycisk zamykający dialog
        btn = tk.Button(modal, text="OK", command=modal.destroy, bg=WHITE, fg=BG)
        btn.pack(pady=(0, 15))

        # Czekamy na zamknięcie modala, dzięki czemu użytkownik musi kliknąć OK
        # zanim wróci do gry — to dobre dla krótkich podpowiedzi.
        self.root.wait_window(modal)

    def start_new_game(self):
        # Przygotuj nową talię pytań i zresetuj licznik oraz koła ratunkowe.
        questions_data = load_questions("data/questions.json")

        easy = questions_data["easy"]
        medium = questions_data["medium"]
        hard = questions_data["hard"]

        # Mieszamy sekcje, żeby gra za każdym razem była inna
        random.shuffle(easy)
        random.shuffle(medium)
        random.shuffle(hard)

        # Bierzemy po 4 pytania z każdej trudności (łatwe/średnie/trudne)
        self.questions = easy[:4] + medium[:4] + hard[:4]
        self.current_index = 0
        self.current_money = 0

        # Stan dostępności kół ratunkowych — True = dostępne
        self.lifelines = {
            "50": True,
            "audience": True,
            "phone": True
        }

    def load_question(self):
        # Załaduj bieżące pytanie do widoku — aktualizujemy etykiety i przyciski
        question = self.questions[self.current_index]

        # Wyświetl nagłówek z kwotą i samo pytanie
        self.question_label.config(
            text=f"Pytanie za {format_amount(MONEY_LEVELS[self.current_index])} zł\n\n{question['question']}"
        )

        letters = ["A", "B", "C", "D"]

        # Ustaw teksty przycisków odpowiedzi i włącz je (na wypadek restartu)
        for index, answer in enumerate(question["answers"]):
            self.answer_buttons[index].config(
                text=f"{letters[index]}. {answer}",
                state="normal",
                bg=BLUE,
                fg=WHITE
            )

        # Zaktualizuj wygraną i pasek postępu
        self.money_label.config(text=f"Aktualna wygrana: {format_amount(self.current_money)} zł")
        self.progress_label.config(
            text=f"Pytanie {self.current_index + 1} / {len(self.questions)}"
        )
        # Wyczyść pole informacyjne (jeśli wcześniej było coś pokazane)
        self.info_label.config(text="")

    def check_answer(self, selected_index):
        # Sprawdź czy wybrana odpowiedź jest poprawna. Jeśli tak -> zwiększamy index
        # i ustawiamy aktualną wygraną, jeśli nie -> pokazujemy koniec gry.
        question = self.questions[self.current_index]
        correct_index = question["correct"]

        if selected_index == correct_index:
            # Gdy odpowiedź poprawna, pokoloruj na zielono i przejdź dalej po krótkim opóźnieniu
            self.answer_buttons[selected_index].config(bg=GREEN)

            self.current_money = MONEY_LEVELS[self.current_index]
            self.current_index += 1

            if self.current_index >= len(self.questions):
                # Gracz odpowiedział na wszystkie pytania — koniec gry, zapis wyniku
                self.question_label.config(text="Gratulacje! Wygrałeś milion złotych!")
                save_result(self.current_money)
                self.disable_buttons()
            else:
                # Poczekaj 1s i załaduj kolejne pytanie — daje to czas na zobaczenie koloru
                self.root.after(1000, self.load_question)

        else:
            # Błędna odpowiedź — pokaż czerwoną podświetloną odpowiedź i poprawną
            self.answer_buttons[selected_index].config(bg=RED)
            self.answer_buttons[correct_index].config(bg=GREEN)

            # Wyświetl komunikat o końcu gry i zapisz wynik
            self.question_label.config(
                text=f"Koniec gry! Wygrywasz: {format_amount(self.current_money)} zł"
            )
            save_result(self.current_money)
            self.disable_buttons()

    def use_fifty_fifty(self):
        # Obsługa 50/50: usuwamy dwie błędne odpowiedzi (przycisk wyłącza się)
        if not self.lifelines["50"]:
            return

        question = self.questions[self.current_index]
        remaining = fifty_fifty(question)

        for index, button in enumerate(self.answer_buttons):
            if index not in remaining:
                button.config(state="disabled")

        self.lifelines["50"] = False
        self.fifty_button.config(state="disabled")
        # Krótkie info w dolnym polu, w razie gdy modal nie jest preferowany
        self.info_label.config(text="Użyto koła 50/50.")

    def use_audience(self):
        # Publiczność: generuje procentowy rozkład i wyświetla go w modalnym oknie
        if not self.lifelines["audience"]:
            return

        question = self.questions[self.current_index]
        results = audience_help(question)

        letters = ["A", "B", "C", "D"]
        text = "Publiczność podpowiada:\n"

        for index, percent in results.items():
            text += f"{letters[index]}: {percent}%\n"

        self.lifelines["audience"] = False
        self.audience_button.config(state="disabled")
        # Preferujemy modalne okno, bo zawsze będzie w całości widoczne
        try:
            self.show_modal_message("Publiczność", text, width=500, height=220)
        except Exception:
            # Fallback: jeśli modal się nie wykona (rzadko), pokaż w dolnym polu
            self.info_label.config(text=text)

    def use_phone(self):
        # Telefon do przyjaciela: pokazujemy wiadomość (czasem pewna, czasem niepewna)
        if not self.lifelines["phone"]:
            return

        question = self.questions[self.current_index]
        message = phone_friend(question)

        self.lifelines["phone"] = False
        self.phone_button.config(state="disabled")
        # Preferujemy modal, żeby wiadomość była od razu widoczna w całości
        try:
            self.show_modal_message("Telefon", f"Przyjaciel mówi:\n{message}", width=500, height=160)
        except Exception:
            self.info_label.config(text=f"Przyjaciel mówi:\n{message}")

    def restart_game(self):
        # Reset stanu gry i przywrócenie dostępności kół ratunkowych
        self.start_new_game()

        self.fifty_button.config(state="normal")
        self.audience_button.config(state="normal")
        self.phone_button.config(state="normal")
        self.restart_button.config(state="normal")
        self.results_button.config(state="normal")

        self.load_question()

    def show_results(self):
        # Pokaż historię wyników (ostatnie 5) w dolnym polu informacyjnym
        path = Path("data/results.json")

        if not path.exists():
            self.info_label.config(text="Brak zapisanych wyników.")
            return

        with path.open("r", encoding="utf-8") as file:
            results = json.load(file)

        if not results:
            self.info_label.config(text="Brak zapisanych wyników.")
            return

        text = "Historia wyników:\n"

        for index, result in enumerate(results[-5:], start=1):
            text += f"{index}. {format_amount(result['score'])} zł\n"

        self.info_label.config(text=text)

    def disable_buttons(self):
        # Ustaw wszystkie przyciski odpowiedzi i koła na nieaktywne — używane po końcu gry
        for button in self.answer_buttons:
            button.config(state="disabled")

        self.fifty_button.config(state="disabled")
        self.audience_button.config(state="disabled")
        self.phone_button.config(state="disabled")

        # Po zakończeniu gry przyciski restart/historia nadal dostępne
        self.restart_button.config(state="normal")
        self.results_button.config(state="normal")


# Punkt wejścia aplikacji GUI — tworzymy root i instancję klasy
root = tk.Tk()
app = MillionairesGUI(root)
root.mainloop()