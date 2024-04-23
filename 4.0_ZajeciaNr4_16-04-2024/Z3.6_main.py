def map_nested(func, nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            # warunek: jeżeli element jest listą, rekurencyjnie zastosuj map_nested
            result.append(map_nested(func, item))
        else:
            # warunek: jeżeli element nie jest listą, zastosuj funkcję func
            result.append(func(item))
    return result

# przykład funkcji do zastosowania
def square(x):
    return x * x

# przykładowa zagnieżdżona lista [nested_list]
nested_list = [1, 2, [3, 4, [5, 6]], 7]

# zastosowanie funkcji map_nested
mapped_list = map_nested(square, nested_list)

# wyświetlenie wyników
print("\n(1) Nasza zagnieżdżona lista: ", nested_list)
print("(2) Lista po zastosowaniu funkcji: ", mapped_list)
