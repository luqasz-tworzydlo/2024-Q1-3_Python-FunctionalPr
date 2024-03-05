print("\n=> funkcja compose, która przyjmuje dwie funkcje jako \n"
      "argumenty i zwraca nową funkcję, będącą ich kompozycją")

def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def multiplyB2_mnozeniePrzezDwa(x):
    return x * 2

def add3_dodajTrzy(x):
    return x + 3

composed = compose(multiplyB2_mnozeniePrzezDwa, add3_dodajTrzy)

print(composed(7))
# pierwsza operacja to 7+3 = 10,
# druga operacja to 10*2 = 20
# u nas wynik to wtedy 20
