# funkcja przyjmująca listę krotek i zwracająca listę, w której
# każdy element jest wynikiem zastosowania funkcji do elementów krotek
def map_tuples(lst, func):
    return [func(*tpl) for tpl in lst]


# przykładowe użycia funkcji & wyświetlenie wyniku końcowego
print("\nWynik po zastosowaniu funkcji: ", map_tuples([(1, 2), (3, 4), (5,6), (7,8), (9,10), (11,12)], lambda x, y: x * y))
