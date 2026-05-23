Milionerzy — projekt w Pythonie

**Opis projektu**
To prosta i przyjemna implementacja gry "Milionerzy" w Pythonie. Są dwie wersje: konsolowa i graficzna (Tkinter). Wiesz — odpowiadasz na pytania wielokrotnego wyboru, zdobywasz kolejne progi wygranej i możesz używać kół ratunkowych, tak jak w teleturnieju. Projekt jest podzielony na moduły i napisany z myślą o przejrzystości.

**Funkcjonalności**

**Podstawowa rozgrywka**
- Pytania wczytywane z pliku JSON
- Cztery odpowiedzi (A/B/C/D)
- Jedna poprawna odpowiedź
- Sprawdzenie poprawności odpowiedzi
- Gra kończy się po pomyłce

**System wygranej**
- Progi nagród w `config.py`
- Wygrana aktualizowana po każdym pytaniu
- Trudność rośnie stopniowo (łatwe → średnie → trudne)

**Losowość**
- Pytania tasowane przy każdej grze (`random.shuffle`)
- Dzięki temu każda rozgrywka jest trochę inna

**Koła ratunkowe**
- 50/50 — usuwa dwie błędne odpowiedzi
- Publiczność — generuje procentowy rozkład odpowiedzi (najbardziej prawdopodobna jest poprawna)
- Telefon do przyjaciela — symulowana podpowiedź (może trafić, może być niepewna)

**Zapisywanie wyników**
- Wyniki zapisywane do `data/results.json`
- Każdy wpis to końcowa wygrana gracza
- Do zapisu użyto `json` i `pathlib`

**Interfejs graficzny (GUI)**
- Zrobione w Tkinter
- Ciemny, stonowany motyw z akcentami
- Przyciski odpowiedzi, koła ratunkowe i pasek postępu (np. "Pytanie 3/12")
- Komunikaty dla gracza dostosowujące się do sytuacji

**Ulepszenia wizualne**
- Kolory: zielony = poprawna odpowiedź, czerwony = błędna
- Krótkie opóźnienie przed przejściem dalej, żeby wszystko było czytelne
- Spójny wygląd aplikacji

**Restart gry**
- Przycisk "Zagraj od nowa" resetuje stan gry i koła ratunkowe

**Historia wyników**
- Możliwość podglądu ostatnich wyników (na przykład 5 ostatnich)

**Struktura projektu**

```
milionerzy-python/
├── main.py           # wersja konsolowa
├── gui.py            # wersja graficzna (Tkinter)
├── game.py           # logika gry
├── questions.py      # wczytywanie pytań
├── lifelines.py      # koła ratunkowe
├── results.py        # zapis wyników
├── config.py         # progi wygranej
└── data/
    ├── questions.json
    └── results.json
```

**Wykorzystane elementy Pythona**
- Instrukcje warunkowe (`if` / `elif` / `else`)
- Pętle (`for`, `while`) i `enumerate`
- Funkcje i moduły
- Biblioteki standardowe: `random`, `json`, `pathlib`
- GUI: `tkinter`

**Jak uruchomić**
- Wersja konsolowa: `python main.py`
- Wersja graficzna: `python gui.py`



