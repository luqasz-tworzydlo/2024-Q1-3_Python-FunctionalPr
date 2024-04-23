def flatten_list(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            # warunek: jeżeli element jest listą, rekurencyjnie spłaszcz listę
            result.extend(flatten_list(element))
        else:
            # warunek: jeśli element nie jest listą, dodaj go bezpośrednio do wynikowej listy
            result.append(element)
    return result

# nasza przykładowa zagnieżdżona lista
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, [10, 11], 12]]]

# użycie naszej funkcji flatten_list
flat_list = flatten_list(nested_list)

# wyświetlenie wyników
print("\n(1) Nasza pierwotna, zagnieżdzona lista: ", nested_list)
print("(2) Nasza spłaszczona lista (flat list): ", flat_list)
