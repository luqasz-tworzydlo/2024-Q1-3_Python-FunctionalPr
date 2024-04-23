# funkcja obracająca listę o zadaną liczbę kroków w prawo
def rotate_list(lst, steps):
    if not lst:
        return lst  # warunek: jeżeli lista jest pusta, zwróć ją bez zmian
    steps = steps % len(lst)  # ten fragment umożliwia na rotację
                              # o liczbę kroków większą niż długość listy
    return lst[-steps:] + lst[:-steps]

# przykładowe użycie naszej funkcji
original_list = [1, 2, 3, 4, 5, 6, 7]
rotated_list = rotate_list(original_list, 3)

print("\n(1) Oryginalna lista: ", original_list)
print("(2.1) Obrócona lista: ", rotated_list)

# Przykład z większą liczbą kroków niż długość listy
rotated_list_large_steps = rotate_list(original_list, 9)
print("(2.2) Obrócona lista z większą liczbą kroków,"
      "\nniż długość listy", rotated_list_large_steps)
