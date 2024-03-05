print ("\n=> Funkcja apply_twice przyjmująca inną funkcję i wartość,\n"
       "a następnie stosuje tę funkcję dwa razy do wartości:")

def apply_twice(funkcja, wartosc):
    return funkcja(funkcja(wartosc))


wynik = apply_twice(lambda x: x + 2, 3)
print(wynik)
