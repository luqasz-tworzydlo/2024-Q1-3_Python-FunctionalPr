print("\n=> (1) Funkcja zwracajaca tylko liczby parzyste")
def liczbyParzysteWyswietl(listaNumerow):
    return [numer for numer in listaNumerow if numer % 2 == 0]

przykladowaLista = [2, 3, 5, 7, 10, 12, 15, 17, 18, 19, 20, 21]
print(liczbyParzysteWyswietl(przykladowaLista))

print("\n=> (2) Funkcja obliczajaca pole prostokata na podstawie dlugosci bokow")

obszarProstokata = lambda dlugosc, szerokosc: dlugosc * szerokosc
print(obszarProstokata(2, 3))
