# config.py — ustawienia stałych gry
# Tutaj definiujemy progi wygranej (kwoty) przypisane do kolejnych pytań.
# Lista `MONEY_LEVELS` zawiera wartości w kolejności od pierwszego pytania do ostatniego.
# Jeśli chcesz zmienić liczbę pytań/poziomów lub wartości nagród, wystarczy edytować
# tę listę. Kwoty zapisane są jako liczby całkowite (PLN) — formatowanie do wyświetlania
# robimy w kodzie (funkcja format_amount).

MONEY_LEVELS = [
    500,
    1000,
    2000,
    5000,
    10000,
    20000,
    40000,
    75000,
    125000,
    250000,
    500000,
    1000000,
]
