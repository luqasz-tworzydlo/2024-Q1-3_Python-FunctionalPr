# stworzenie listy zawierającej piersze 10 liczb kwadratowych (1,4,9...)

print("\n(1) Lista pierwszych 10 liczb do kwadratu:")
liczbyDoKwadratu = [x ** 2 for x in range(1, 11)]
print(liczbyDoKwadratu)

# stworzenie listy długości słów ( z użyciem list comprehensions )

print("\n(2) Lista długości wybranych słów\n[dzien, noc, poczatek, koniec]:")
wybraneSlowa = ["dzien", "noc", "poczatek", "koniec"]
dlugoscSlowa = [len(slowo) for slowo in wybraneSlowa]
print(dlugoscSlowa)
