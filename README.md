# Process Scheduling Simulator

Projekt symuluje działanie algorytmów szeregowania procesów znanych z systemów operacyjnych. Program generuje zestaw procesów, przeprowadza symulację wybranego algorytmu, oblicza czasy oczekiwania i realizacji, a następnie zapisuje wyniki do baz danych SQLite i eksportuje je do plików CSV.

## Uruchomienie

```bash
python main.py
```

Program działa interaktywnie - kolejne kroki są prowadzone przez prompty w terminalu.

## Przebieg działania

Po uruchomieniu program tworzy trzy bazy danych (jeśli jeszcze nie istnieją), a następnie przeprowadza użytkownika przez kolejne etapy:

1. Podanie numeru zestawu danych - pozwala przechowywać i porównywać wyniki wielu uruchomień.
2. Wygenerowanie 50 procesów z losowymi parametrami (`arrival_time` w zakresie 0–49, `executing_time` w zakresie 10–59).
3. Wybór algorytmu: `fcfs`, `sjf` lub `rr`.
4. Jeśli wybrano Round Robin - podanie kwantu czasu.
5. Wykonanie symulacji, obliczenie wyników i zapis do baz danych.
6. Opcjonalny eksport danych do CSV.

## Algorytmy

**FCFS (First Come First Served)** - procesy są wykonywane w kolejności nadejścia. Algorytm niewywłaszczający, najprostszy w implementacji.

**SJF (Shortest Job First)** - spośród procesów gotowych do wykonania wybierany jest ten z najkrótszym czasem wykonywania. Algorytm niewywłaszczający.

**Round Robin** - procesy wykonywane są cyklicznie, każdy przez maksymalnie jeden kwant czasu. Po wyczerpaniu kwantu proces wraca na koniec kolejki.

Dla każdego algorytmu obliczane są `waiting_time` i `turnaround_time` dla wszystkich procesów, a następnie ich wartości średnie.

## Struktura projektu

```
main.py          # punkt wejścia, pętla główna programu
Algorithms.py    # implementacje FCFS, SJF i Round Robin
Functions.py     # ładowanie danych, zapis wyników i szczegółów procesów
Generator.py     # generowanie losowych procesów
Classes.py       # klasa Process
Dane.py          # eksport Dane.db → procesy.csv
DaneFinish.py    # eksport DaneFinish.db → wyniki.csv
DaneStartowe.py  # eksport DaneStartowe.db → dane_startowe.csv
```

## Bazy danych

Program automatycznie tworzy trzy pliki SQLite:

**DaneStartowe.db** - wygenerowane procesy wejściowe (`id`, `numer`, `arrival_time`, `executing_time`).

**DaneFinish.db** - wyniki zbiorcze dla każdego uruchomienia (`numer`, `algorytm`, średni `waiting_time`, średni `turnaround_time`).

**Dane.db** - szczegółowe dane wykonania każdego procesu (`pid`, `arrival_time`, `start_time`, `end_time`, `waiting_time`).

## Eksport do CSV

Każdą z baz danych można wyeksportować do pliku CSV za pomocą odpowiedniego modułu:

```bash
python DaneStartowe.py   # → dane_startowe.csv
python DaneFinish.py     # → wyniki.csv
python Dane.py           # → procesy.csv
```

## Znane ograniczenia

- Liczba generowanych procesów jest stała (50) - nie można jej zmienić bez modyfikacji kodu.
- Brak walidacji danych wejściowych podawanych przez użytkownika.
- Zaimportowany moduł `threading` nie jest faktycznie wykorzystywany.
- Dostępne są tylko trzy algorytmy - brak SRTF, Priority Scheduling, Multilevel Queue i podobnych.
- Brak interfejsu graficznego i wizualizacji (np. wykresy Gantta).

## Możliwe rozszerzenia

- dodanie kolejnych algorytmów (SRTF, Priority Scheduling, Multilevel Feedback Queue)
- wizualizacja w postaci wykresów Gantta
- GUI w Tkinter lub PyQt
- możliwość konfiguracji liczby procesów i zakresów parametrów
- porównanie wszystkich algorytmów w jednym uruchomieniu
- eksport wyników do PDF

