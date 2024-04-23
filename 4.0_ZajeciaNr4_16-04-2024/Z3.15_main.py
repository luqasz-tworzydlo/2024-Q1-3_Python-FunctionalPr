# funkcja sortująca listę według zadanej funkcji klucza
def custom_sort(lst, key_function):
    return sorted(lst, key=key_function)

# nasza przykładowa funkcja klucza
def get_length(item):
    return len(item)

# przykładowe użycie nasze funkcji (słowa)
words = ["Gdańsk", "Gdynia", "Sopot", "Wejherowo"]
sorted_words = custom_sort(words, get_length)

# wyświetlenie wyniku posegregowanych słów
print("\n(1) Posegregowane słowa: ", sorted_words)

# posortowanie liczb na podstawie ich wartości bezwzględnej
numbers = [-25, -5, -3, 1, 9]
sorted_numbers = custom_sort(numbers, key_function=abs)

# wyświetlenie wyniku posegregowanych liczb
print("\n(2) Posegregowane liczby: ", sorted_numbers)
