# funkcja znajdująca różnicę między maksymalną, a minimalną wartością w liście
def find_max_min_diff(numbers):
    if not numbers:  # sprawdzenie, czy lista nie jest pusta
        return None  # zwrócenie None, jeśli lista jest pusta
    max_value = max(numbers)  # znajdź maksymalną wartość w liście
    min_value = min(numbers)  # znajdź minimalną wartość w liście
    return max_value - min_value  # oblicz oraz zwróć różnicę

# przykładowe użycie naszej funkcji
numbers_list = [4, 15, 26, 75, 9, 69, 65, 70, 94]
difference = find_max_min_diff(numbers_list)
print("\n(1) Różnica między wartością max, a min: ", difference) # nasz wynik: 90 (94 - 4)

# przykłądowe użycie funkcji z pustą listą
empty_list = []
difference_empty = find_max_min_diff(empty_list)
print("\n(2) Przykład z pustą tablicą: ", difference_empty) # nasz wynik: None
