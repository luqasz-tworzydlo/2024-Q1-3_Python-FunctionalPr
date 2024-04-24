# funkcja filtrująca liczby, pozostawiająca wyłącznie liczby parzyste
def filter_even_values(dictionary):
    return {key: value for key, value in dictionary.items() if value % 2 == 0}

# przykładowe użycie naszej funkcji
sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12
}
filtered_dict = filter_even_values(sample_dict)

# wyświetlenie naszego wyniku
print("\n=> Wyświetlenie oryginalnych liczb: \n", sample_dict)
print("\n=> Wyświetlenie przefiltrowanych liczb: \n", filtered_dict)
