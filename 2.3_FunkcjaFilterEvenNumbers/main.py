print("\n=> Funkcja filter_even_numbers, przyjmująca listę liczb \n"
      "i zwracająca nową listę, zawierającą tylko parzyste liczby:")

def filter_even_numbers(numery):
    return list(filter(lambda x: x % 2 == 0, numery))


print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9,
                           10, 11, 12, 13, 14, 15, 16, 17, 18,
                           19, 20, 21, 22, 23, 24, 25, 26, 27]))
