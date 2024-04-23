# funkcja filtrująca wszystkie liczby w celu pozostawiania
# wyłącznie liczb parzystych, a następnie ich zsumowanie
def sum_of_evens(numbers):
    return sum(x for x in numbers if x % 2 == 0)

# przykładowe użycie funkcji
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = sum_of_evens(numbers_list)

# wyświetlenie wyniku
print("\n=> Suma wszystkich liczb parzystych wynosi: ", result)
# wykonana operacja to (2 + 4 + 6 + 8 + 10 + 12 = 42),
# z czego wynik końcowy wynosi 42 [suma liczb parzystych]
