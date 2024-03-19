print("\n=> użycie funkcji groupby z modułu itertools"
      "\ndo zgrupowania ciągu liczb całkowitych na podstawie"
      "\nich parzystości i wydrukowanie (wyświetlenie) wynikowe grupy:\n")

from itertools import groupby

# nasz ciąg liczb całkowitych
NumeryNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# funkcja do określenia klucza (parzystości)
KluczParzystosci_ParityKey = lambda x: x % 2 == 0

# grupowanie liczb (parzyste i nieparzyste)
for klucz_key, grupa_group in groupby(sorted(NumeryNumbers), KluczParzystosci_ParityKey):
    ListaGrup_GroupList = list(grupa_group)
    TypGrupy_GroupType = "=> parzyste" if klucz_key else "=> nieparzyste"
    print(f"{TypGrupy_GroupType}: {ListaGrup_GroupList}")
