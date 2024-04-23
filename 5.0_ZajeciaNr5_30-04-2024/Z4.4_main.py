# funkcja przyjmujaca exponent i zwracajaca funkcję, która podnosi
# podaną liczbę do potęgi określonej przez ten exponent
def create_exponential_function(exponent):
    return lambda x: x ** exponent


# przykładowe użycie funkcji
square = create_exponential_function(2)

# wyświetlenie wyniku
print("\nNasz wynik wynosi: ", square(5))
