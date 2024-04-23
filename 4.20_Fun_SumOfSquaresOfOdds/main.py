# funkcja obliczająca sumę kwadratów liczb nieparzystych z listy
def sum_of_squares_of_odds(numbers):
    # tutaj jest filtrowana lista, aby zostawić tylko liczby nieparzyste,
    # a następnie podnieść je do kwadratu oraz zsumuować
    return sum(x**2 for x in numbers if x % 2 != 0)

# przykładowe użycie naszej funkcji
numbers = [1, 2, 3]
result = sum_of_squares_of_odds(numbers)

# wyświetlenie naszego wyniku
print("\n=> Suma kwadratów liczb nieparzystych wynosi: ", result)
