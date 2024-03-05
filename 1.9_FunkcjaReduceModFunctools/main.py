# wyszukanie najwiekszej liczby w danej liscie

print("\n(1) Największa liczba z listy A")

from functools import reduce
liczbyListaA = [1, 3, 24, 9, 7, 5, 13]

najwiekszaLiczba = reduce(lambda x, y: x if x > y else y, liczbyListaA)
print(najwiekszaLiczba)

# obliczenie sredniej z danej listy liczb

print("\n(2) Średnia z listy liczb B: ")

liczbyListaB = [3, 5, 4, 5, 5, 4, 5, 4.5, 5, 3.5]

sumaWszystkichLiczbB = reduce(lambda x, y: x + y, liczbyListaB)

sredniaLiczbB = sumaWszystkichLiczbB / len(liczbyListaB)
print(sredniaLiczbB)
