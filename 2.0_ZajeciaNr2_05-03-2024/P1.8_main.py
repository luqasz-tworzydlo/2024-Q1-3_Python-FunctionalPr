print("\n=> suma wszystkich liczb w liście \n"
      "(funkcja reduce z modułu functools):")

from functools import reduce

liczbyListaB = [3, 5, 4, 5, 5, 4, 5, 4.5, 5, 3.5]

sumaWszystkichLiczbB = reduce(lambda x, y: x + y, liczbyListaB)

print(sumaWszystkichLiczbB)
