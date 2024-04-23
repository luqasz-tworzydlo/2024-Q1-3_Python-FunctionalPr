# Zdefiniowana funkcja double_list_elements
def double_list_elements(liczby):
    return [liczba_x * 2 for liczba_x in liczby]

# Obliczenia wykonane za pomocą powyższej funkcji
pierwotnaLista_oryginalList = [1, 2, 3, 4, 5, 6, 7]
podwojonaLista_doubledList = double_list_elements(pierwotnaLista_oryginalList)

# Wyświetlenie wyników (oryginalna oraz po zastosowaniu funkcji)
print("\n=> Wyświetlenie wyniku (oryginalnych oraz podwojonych liczb):")
print("*** Oryginalna (piertowna) lista:", pierwotnaLista_oryginalList)
print("*** Lista po podwojeniu (doubled):", podwojonaLista_doubledList)
