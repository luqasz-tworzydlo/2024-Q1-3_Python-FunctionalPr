# zdefiniowanie dwóch prostych funkcji
def doKwadratu(numer):
    return numer ** 2
def dodajLiczbePiec(numer):
    return numer + 5

# stworzenie funkcji aplikującej listę funkcji do wartości
def aplikacjaFunkcji(funkcje, wartosc):
    wynik = wartosc
    for funkcja in funkcje:
        wynik = funkcja(wynik)
    return wynik

# zastosowanie funkcji do naszej listy liczb
numery = [1, 2, 3, 4, 5]
funkcje = [doKwadratu, dodajLiczbePiec]

# użycie funkcji map() do zastosowania funkcji do każdej liczby w liście
wynik = map(lambda x: aplikacjaFunkcji(funkcje, x), numery)

print(list(wynik))
