# podzielenie liczb z listy (na parzyste oraz nieparzyste)
def partition_list(lst, condition):
    true_list = []
    false_list = []
    for item in lst:
        if condition(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return true_list, false_list

# nasza przykładowa funkcja warunkowa
def is_even(number):
    return number % 2 == 0

# przykładowe użycie naszej funkcji
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
even_numbers, odd_numbers = partition_list(numbers, is_even)

# wyświetlenie naszych wyników
print("\n(1) Liczby parzyste / Even numbers:", even_numbers)
print("(2) Liczby nieparzyste / Odd numbers:", odd_numbers)
