print("\n=> użycie funkcji functools.partial do stworzenia \n"
      "funkcji, która zawsze dodaje 5 do swojego argumentu")

from functools import partial

def add_dodaj(x, y):
    return x + y

add5_dodaj5 = partial(add_dodaj, 5)

print(add5_dodaj5(0))
print(add5_dodaj5(7))
