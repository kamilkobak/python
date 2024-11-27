#!/bin/python3
# Autor: Kamil Kobak
# Wymagane:
# pip3 install pyfiglet --break-system-packages

import os
import time
import pyfiglet

def clear_console():
    """Funkcja do czyszczenia konsoli."""
    os.system('cls' if os.name == 'nt' else 'clear')

def blinking_text(text, iterations=10, delay=0.5):
    """Funkcja wyświetlająca migający tekst."""
    figlet = pyfiglet.Figlet(font='big')  # Możesz zmienić font na inny
    for _ in range(iterations):
        # Wyświetlenie tekstu
        clear_console()
        print(figlet.renderText(text))
        time.sleep(delay)
        
        # Ukrycie tekstu (czyszczenie ekranu)
        clear_console()
        time.sleep(delay)

def countdown(minutes):
    """Funkcja odliczająca czas w minutach i sekundach."""
    total_seconds = minutes * 60  # Całkowita liczba sekund
    initial_seconds = total_seconds  # Zapamiętujemy początkowy czas dla proporcji paska
    bar_length = 30  # Długość paska w znakach #

    while total_seconds:
        # Oblicz pozostałe minuty i sekundy
        mins, secs = divmod(total_seconds, 60)

        # Generowanie paska postępu
        filled_length = int(bar_length * total_seconds / initial_seconds)
        progress_bar = '#' * filled_length + '-' * (bar_length - filled_length)

        # Wyświetlanie czasu w dużej czcionce
        time_text = f" {mins:02d}:{secs:02d}"
        ascii_art = pyfiglet.figlet_format(time_text)
        
        print("\033c", end="")  # Czyści ekran konsoli
        print(f"\n Koniec przerwy za:\n")
        print(ascii_art)
        print(f" Progress: [{progress_bar}]")
        
        time.sleep(1)
        total_seconds -= 1

if __name__ == "__main__":
    try:
        czas = int(input("Podaj czas w minutach: "))
        countdown(czas)
        
        # Po zakończeniu odliczania wyświetl migający napis "KONIEC!"
        blinking_text(" KONIEC!", iterations=15, delay=0.5)
    except ValueError:
        print("Proszę podać poprawną liczbę minut.")


