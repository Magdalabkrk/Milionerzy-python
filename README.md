🎮 Milionerzy — projekt Python
📌 Opis projektu
Projekt przedstawia konsolową implementację gry „Milionerzy” napisaną w języku Python.
Gracz odpowiada na pytania wielokrotnego wyboru, zdobywając kolejne poziomy wygranej.

Aplikacja została zaprojektowana w sposób modułowy, z podziałem na pliki odpowiadające za konkretne elementy logiki gry.

⚙️ Funkcjonalności
🎯 Podstawowa rozgrywka
pytania wczytywane z pliku JSON

4 odpowiedzi (A/B/C/D)

jedna poprawna odpowiedź

sprawdzanie odpowiedzi użytkownika

zakończenie gry po błędzie

💰 System wygranej
rosnące progi pieniężne (config.py)

aktualna wygrana wyświetlana po każdej poprawnej odpowiedzi

zakończenie gry z odpowiednią kwotą

🎲 Losowość
pytania są losowane przy każdym uruchomieniu (random.shuffle)

🛟 Koła ratunkowe
Zaimplementowane trzy koła:

1. 50/50
usuwa dwie błędne odpowiedzi

wykorzystuje random.sample()

2. Publiczność
generuje procentowe rozkłady odpowiedzi

poprawna odpowiedź ma największe prawdopodobieństwo

3. Telefon do przyjaciela
symuluje podpowiedź

~75% szans na poprawną odpowiedź

💾 Zapisywanie wyników
wyniki zapisywane są w pliku data/results.json

każdy wynik to zapis końcowej wygranej

wykorzystano moduły json oraz pathlib

🧱 Struktura projektu
milionerzy-python/
│
├── main.py         # główna logika gry
├── game.py         # obsługa pojedynczego pytania
├── questions.py    # wczytywanie pytań z JSON
├── lifelines.py    # koła ratunkowe
├── results.py      # zapis wyników
├── config.py       # progi wygranej
│
├── data/
│   ├── questions.json
│   └── results.json
🧠 Wykorzystane elementy Pythona (zgodne z materiałami)
Projekt wykorzystuje zagadnienia omawiane na zajęciach:

K2 — instrukcje warunkowe
if / elif / else

walidacja danych użytkownika

logika gry

K3 — pętle
for, while

break, continue

enumerate()

K4 — funkcje
podział na małe funkcje

przekazywanie argumentów

zwracanie wartości

K5 — moduły i biblioteka standardowa
import

random

json

pathlib

podział projektu na pliki

▶️ Jak uruchomić
python main.py
🚀 Co planujemy dalej
Możliwe rozszerzenia projektu:

📊 wyświetlanie historii wyników

🎨 poprawa wyglądu (kolory w terminalu)

🖥️ wersja GUI (np. Tkinter)

🔊 dodanie dźwięków

📈 statystyki gracza

💡 Sugestie (na + do zaliczenia)
Możecie jeszcze podbić ocenę:

dodać komentarze/docstringi do funkcji

zrobić README po angielsku (opcjonalnie)

pokazać przykładową sesję gry

dodać walidację pliku JSON

użyć type hints (już częściowo macie 👍)