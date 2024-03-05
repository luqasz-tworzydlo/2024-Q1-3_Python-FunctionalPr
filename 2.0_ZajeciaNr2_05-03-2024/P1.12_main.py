print("\n=> użycie functools.partial do stworzenia \n"
      "nowej funkcji, która mnoży dowolną liczbę przez 3")

from functools import partial

def mnozenie(x, y):
    return x * y

mnozeniePrzezTrzy = partial(mnozenie, 3)

print("\n[Test 1]: " + str(mnozeniePrzezTrzy(3)))
print("\n[Test 2]:")
print(mnozeniePrzezTrzy(9))
