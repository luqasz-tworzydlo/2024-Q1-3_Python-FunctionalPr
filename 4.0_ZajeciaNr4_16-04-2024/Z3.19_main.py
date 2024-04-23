# funkcja check_anagrams sprawdzająca, czy dwa podane stringi są anagramami
def check_anagrams(stringNo1, stringNo2):
    # usunięcie białych znaków (spacji) oraz zmiana dużycch liter na małe
    clean_stringNo1 = ''.join(stringNo1.split()).lower()
    clean_stringNo2 = ''.join(stringNo2.split()).lower()

    # sprawdzenie, czy posortowane stringi są takie same
    return sorted(clean_stringNo1) == sorted(clean_stringNo2)

# przykładowe użycie funkcji nr 1
stringNo1 = "notes"
stringNo2 = "sonet"
are_anagrams = check_anagrams(stringNo1, stringNo2)

# wyświetlenie wyniku, czy słowa są anagramami
print(f"\n=> '{stringNo1}' i '{stringNo2}' są anagramami:", are_anagrams) # wynik: True

# przykładowe użycie funkcji nr 2
print("=> Karta - Miarka są anagramami:" ,check_anagrams("karta", "miarka")) # wynik: False
print("=> Notes - Sonet: są anagramami:", check_anagrams("karta", "tarka")) # wynik: True
