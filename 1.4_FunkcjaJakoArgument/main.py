# => Funkcja A, ktora bedzie u nas przekazana jako argument
def WielokrotnoscLiczbyPrzezTrzy(naszNumer):
    return naszNumer * 2

# => Funkcja B, ktora bedzie u nas przekazana jako argument
def PomnozenieLiczbyDoKwadratu(naszNumer):
    return naszNumer ** 2

# => Funkcja, ktora przyjmuje funkcje jako argument
# ( jest to tzw. funkcja wyzszego rzedu )
def NaszaFunkcja(funkcja, numer):
    wynik = funkcja(numer)
    print(f"=> Nasz wynik wynosi: {wynik}")

# przekazanie naszej funkcji jako argumentu
NaszaFunkcja(WielokrotnoscLiczbyPrzezTrzy, 10) # nasz wynik: 20
NaszaFunkcja(PomnozenieLiczbyDoKwadratu, 10) # nasz wynik: 100
