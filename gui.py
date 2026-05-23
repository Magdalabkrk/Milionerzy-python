import tkinter as tk
import random
import json
from pathlib import Path

from config import MONEY_LEVELS
from questions import load_questions
from lifelines import fifty_fifty, audience_help, phone_friend
from results import save_result
from utils import format_amount


BG = "#101820"
CARD = "#1f2a36"
GOLD = "#f2c94c"
WHITE = "#ffffff"
BLUE = "#2f80ed"
GREEN = "#27ae60"
RED = "#eb5757"


class MillionairesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Milionerzy")
        # ustaw większy domyślny rozmiar i minimalny rozmiar okna
        self.root.geometry("900x750")
        self.root.minsize(900, 750)
        # po ustawieniu rozmiaru wypośrodkuj okno na ekranie
        self.center_window()
        self.root.config(bg=BG)

        self.start_new_game()

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
        self.question_label.pack(pady=30)

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

        self.money_label = tk.Label(
            root,
            text="",
            font=("Arial", 14, "bold"),
            bg=BG,
            fg=GOLD
        )
        self.money_label.pack(pady=15)

        self.progress_label = tk.Label(
            root,
            text="",
            font=("Arial", 12, "bold"),
            bg=BG,
            fg=WHITE
        )
        self.progress_label.pack(pady=5)

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

        self.info_label = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            wraplength=760,
            bg=BG,
            fg=WHITE
        )
        self.info_label.pack(pady=10)

        self.load_question()

    def center_window(self):
        """Center the main window on the screen after widgets/layout are initialized."""
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        if w == 1 and h == 1:
            # jeśli jeszcze nie zainicjowano wymiarów, użyj zadeklarowanego rozmiaru
            w, h = 900, 750
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def show_modal_message(self, title: str, message: str, width: int = 600, height: int = 200):
        """Show a centered modal dialog with the given message.

        This avoids needing to resize the main window to see long messages
        (phone / audience results).
        """
        modal = tk.Toplevel(self.root)
        modal.title(title)
        modal.transient(self.root)
        modal.grab_set()

        # Calculate center position relative to parent
        self.root.update_idletasks()
        rx = self.root.winfo_rootx()
        ry = self.root.winfo_rooty()
        rw = self.root.winfo_width()
        rh = self.root.winfo_height()

        x = rx + (rw // 2) - (width // 2)
        y = ry + (rh // 2) - (height // 2)
        modal.geometry(f"{width}x{height}+{x}+{y}")

        label = tk.Label(modal, text=message, wraplength=width-40, justify="left", bg=BG, fg=WHITE, font=("Arial", 12))
        label.pack(padx=20, pady=20, expand=True, fill="both")

        btn = tk.Button(modal, text="OK", command=modal.destroy, bg=WHITE, fg=BG)
        btn.pack(pady=(0, 15))

        # Wait for dialog to close
        self.root.wait_window(modal)

    def start_new_game(self):
        questions_data = load_questions("data/questions.json")

        easy = questions_data["easy"]
        medium = questions_data["medium"]
        hard = questions_data["hard"]

        random.shuffle(easy)
        random.shuffle(medium)
        random.shuffle(hard)

        self.questions = easy[:4] + medium[:4] + hard[:4]
        self.current_index = 0
        self.current_money = 0

        self.lifelines = {
            "50": True,
            "audience": True,
            "phone": True
        }

    def load_question(self):
        question = self.questions[self.current_index]

        self.question_label.config(
            text=f"Pytanie za {format_amount(MONEY_LEVELS[self.current_index])} zł\n\n{question['question']}"
        )

        letters = ["A", "B", "C", "D"]

        for index, answer in enumerate(question["answers"]):
            self.answer_buttons[index].config(
                text=f"{letters[index]}. {answer}",
                state="normal",
                bg=BLUE,
                fg=WHITE
            )

        self.money_label.config(text=f"Aktualna wygrana: {format_amount(self.current_money)} zł")
        self.progress_label.config(
            text=f"Pytanie {self.current_index + 1} / {len(self.questions)}"
        )
        self.info_label.config(text="")

    def check_answer(self, selected_index):
        question = self.questions[self.current_index]
        correct_index = question["correct"]

        if selected_index == correct_index:
            self.answer_buttons[selected_index].config(bg=GREEN)

            self.current_money = MONEY_LEVELS[self.current_index]
            self.current_index += 1

            if self.current_index >= len(self.questions):
                self.question_label.config(text="Gratulacje! Wygrałeś milion złotych!")
                save_result(self.current_money)
                self.disable_buttons()
            else:
                self.root.after(1000, self.load_question)

        else:
            self.answer_buttons[selected_index].config(bg=RED)
            self.answer_buttons[correct_index].config(bg=GREEN)

            self.question_label.config(
                text=f"Koniec gry! Wygrywasz: {format_amount(self.current_money)} zł"
            )
            save_result(self.current_money)
            self.disable_buttons()

    def use_fifty_fifty(self):
        if not self.lifelines["50"]:
            return

        question = self.questions[self.current_index]
        remaining = fifty_fifty(question)

        for index, button in enumerate(self.answer_buttons):
            if index not in remaining:
                button.config(state="disabled")

        self.lifelines["50"] = False
        self.fifty_button.config(state="disabled")
        self.info_label.config(text="Użyto koła 50/50.")

    def use_audience(self):
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
        # show message in a modal dialog so it is always visible
        try:
            self.show_modal_message("Publiczność", text, width=500, height=220)
        except Exception:
            self.info_label.config(text=text)

    def use_phone(self):
        if not self.lifelines["phone"]:
            return

        question = self.questions[self.current_index]
        message = phone_friend(question)

        self.lifelines["phone"] = False
        self.phone_button.config(state="disabled")
        # show message in a modal dialog so it is always visible
        try:
            self.show_modal_message("Telefon", f"Przyjaciel mówi:\n{message}", width=500, height=160)
        except Exception:
            self.info_label.config(text=f"Przyjaciel mówi:\n{message}")

    def restart_game(self):
        self.start_new_game()

        self.fifty_button.config(state="normal")
        self.audience_button.config(state="normal")
        self.phone_button.config(state="normal")
        self.restart_button.config(state="normal")
        self.results_button.config(state="normal")

        self.load_question()

    def show_results(self):
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
        for button in self.answer_buttons:
            button.config(state="disabled")

        self.fifty_button.config(state="disabled")
        self.audience_button.config(state="disabled")
        self.phone_button.config(state="disabled")

        self.restart_button.config(state="normal")
        self.results_button.config(state="normal")


root = tk.Tk()
app = MillionairesGUI(root)
root.mainloop()