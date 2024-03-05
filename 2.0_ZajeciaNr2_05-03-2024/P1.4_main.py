print("\nDekorator timeit, który mierzy i wypisuje \n"
      "czas wykonania dekorowanej funkcji:")

import time

def timeit(funkcja):
    def wrapper(*args, **kwargs):
        czasPoczatek = time.time()
        wynik = funkcja(*args, **kwargs)
        czasKoniec = time.time()
        print(f"=> funkcja '{funkcja.__name__}' została \nwykonana w {czasKoniec - czasPoczatek} sekund.")
        return wynik
    return wrapper

@timeit
def przykladowaFunkcja():
    time.sleep(3)

przykladowaFunkcja()
