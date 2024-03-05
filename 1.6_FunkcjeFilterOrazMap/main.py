print("\n=> (1) Wyodrębnienie słów, które zaczynają się od 'a'")
slowa = ["abecadło", "barok", "cebula", "abonament", "ananas", "domek"]
slowaPoczatekOd_a = filter(lambda slowo: slowo.startswith('a'), slowa)

print(list(slowaPoczatekOd_a))

print("\n => (2) Przekształcenie listy liczb w listę ich kwadratów")
numery = [1, 2, 3, 4, 5, 6, 7]
numeryDoKwadratu = map(lambda x: x ** 2, numery)

print(list(numeryDoKwadratu))
