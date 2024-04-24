# funkcja przyjmujaca listę i funkcję, a następnie zwracajaca nową liste,
# gdzie każdy element jest wynikiem zastosowania funkcji do dotychczasowych elementów
def map_list(lst, func):
    return [func(x) for x in lst]

# przykładowe wykorzystanie funkcji & wyświetlenie wyniku
print("\n(1) Pierwszy przykład: ", map_list([1, 2, 3, 4, 5, 6, 7], lambda x: x * 2))
print("\n(2) Drugi przykład: ", map_list([1, 2, 3, 4, 5], lambda x: x ** 2))
