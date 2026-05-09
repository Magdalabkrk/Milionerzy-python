class Lifelines:
    def __init__(self) -> None:
        self.used = set()

    def use_5050(self) -> str:
        self.used.add("50:50")
        return "50:50"

    def ask_audience(self) -> str:
        self.used.add("publiczność")
        return "publiczność"
