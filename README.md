🎮 Milionerzy — projekt Python

📌 Opis projektu
Projekt przedstawia implementację gry „Milionerzy” napisaną w języku Python. Aplikacja posiada wersję konsolową oraz rozbudowaną wersję graficzną (GUI) stworzoną w Tkinterze. Gracz odpowiada na pytania wielokrotnego wyboru, zdobywając kolejne poziomy wygranej oraz korzystając z kół ratunkowych - podobnie jak w teleturnieju. Projekt został zaprojektowany w sposób modułowy i zgodny z dobrymi praktykami programowania.

⚙️ Funkcjonalności

🎯 Podstawowa rozgrywka

pytania wczytywane z pliku JSON

4 odpowiedzi (A/B/C/D)

jedna poprawna odpowiedź

walidacja wyboru użytkownika

zakończenie gry po błędzie

💰 System wygranej

progi pieniężne zdefiniowane w config.py

aktualna wygrana po każdym pytaniu

realistyczna progresja trudności (easy → medium → hard) powiązana z poziomami nagród

🎲 Losowość

pytania są tasowane przy każdej grze (random.shuffle)

każda rozgrywka wygląda inaczej

🛟 Koła ratunkowe

50/50 - usuwa dwie błędne odpowiedzi (random.sample)

Publiczność - generuje procentowy rozkład odpowiedzi (największa szansa dla poprawnej)

Telefon do przyjaciela - symulacja rozmowy: poprawna odpowiedź, sugestia, błędna odpowiedź z niepewnością lub brak wiedzy

💾 Zapisywanie wyników

wyniki zapisywane w pliku data/results.json

każdy wynik to końcowa wygrana

wykorzystano moduły json i pathlib

🖥️ Interfejs graficzny (GUI)

zbudowany przy użyciu Tkinter

nowoczesny ciemny motyw (kolory teleturniejowe)

przyciski odpowiedzi i kół ratunkowych

aktualna wygrana i pasek postępu (np. „Pytanie 3/12”)

dynamiczne komunikaty dla użytkownika

🎨 Ulepszenia wizualne

kolorowanie odpowiedzi: zielony (poprawna), czerwony (błędna)

opóźnienie 1 sekundy przed kolejnym pytaniem

spójny styl graficzny (ciemne tło + złote elementy)

🔁 Restart gry

przycisk „Zagraj od nowa”

reset pytań, wygranej i kół ratunkowych

📊 Historia wyników

przycisk „Historia wyników”

wyświetla ostatnie 5 wyników gracza

🧱 Struktura projektu
milionerzy-python/
├── main.py # wersja konsolowa
├── gui.py # wersja graficzna (Tkinter)
├── game.py # logika pytania
├── questions.py # wczytywanie pytań
├── lifelines.py # koła ratunkowe
├── results.py # zapis wyników
├── config.py # progi wygranej
├── data/
│ ├── questions.json
│ └── results.json

🧠 Wykorzystane elementy Pythona

instrukcje warunkowe (if / elif / else)

pętle (for, while, break, continue, enumerate)

funkcje i modularność

biblioteki standardowe: random, json, pathlib

GUI: tkinter (obsługa zdarzeń i interfejsu)

▶️ Jak uruchomić
wersja konsolowa: python main.py
wersja graficzna: python gui.py

🚀 Możliwe rozszerzenia

dźwięki

animacje

statystyki gracza

profile użytkowników

wersja webowa

🏁 Podsumowanie
Projekt stanowi kompletną implementację gry „Milionerzy” z logiką gry, systemem nagród, kołami ratunkowymi, zapisem wyników oraz interfejsem graficznym i jest gotowy do prezentacji jako rozbudowany projekt zaliczeniowy.