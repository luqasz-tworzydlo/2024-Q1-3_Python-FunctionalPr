# funkcja obliczająca sumę skumulowaną lsty, tj. sumę elementów do każdego indeksu
def cumulative_sum(lst):
    result = []
    current_sum = 0
    for item in lst:
        current_sum += item
        result.append(current_sum)
    return result

# przykładowe użycie naszej funkcji
numbers = [1, 2, 3, 4, 5, 6, 7]
cumulative_list = cumulative_sum(numbers)

# wyświetlenie wyników
print("\nObliczona suma skumulowana: ", cumulative_list)
