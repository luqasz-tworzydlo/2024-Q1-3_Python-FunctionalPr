# funkcja łącząca dowolną liczbę słowników w jeden słownik,
# gdzie wartości dla powtarzających się kluczy są sumowane
def merge_and_sum_dictionaries(*dicts):
    result = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

# przykładowe użycie naszej funkcji
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 7}
dict2 = {'a': 2, 'b': 1, 'd': 5}
dict3 = {'a': 3, 'e': 1, 'f': 3}
dict4 = {'b': 3, 'c': 9, 'e': 5}
dict5 = {'a': 1, 'c': 3,}

merged_dict = merge_and_sum_dictionaries(dict1, dict2, dict3)

# nasze pierwotne słowniki
print("\nSłownik nr 1: ", dict1)
print("Słownik nr 2: ", dict2)
print("Słownik nr 3: ", dict3)
print("Słownik nr 4: ", dict4)
print("Słownik nr 5: ", dict5)

# wyświetlenie naszego wyniku
print("\nNasze połączone słowniki: \n", merged_dict)
