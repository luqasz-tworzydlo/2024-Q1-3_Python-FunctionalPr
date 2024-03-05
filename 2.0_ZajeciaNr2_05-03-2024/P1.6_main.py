print("\nFunkcji map przekształcająca listę liczb w listę ich kwadratów: ")

def funkcja_LiczbaDoKw(x):
    return x * x

wybraneLiczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
liczbyDoKwadratu = list(map(funkcja_LiczbaDoKw, wybraneLiczby))

print(liczbyDoKwadratu)
