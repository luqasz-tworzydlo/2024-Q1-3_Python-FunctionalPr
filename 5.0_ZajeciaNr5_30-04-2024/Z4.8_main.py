from collections import Counter

def most_frequent_element(lst):
    if not lst:
        return None  # warunek: zwrócenie None, jeśli lista jest pusta
    # w tym miejscu tworzymy obiekt Counter z listy
    # i znajdujemy element o największej liczbie wystąpień
    counter = Counter(lst)
    # zwrócenie elementu z największą liczbą wystąpień
    return counter.most_common(1)[0][0]

# przykładowe użycie naszej funkcji
sample_list = [1, 3, 2, 3, 4, 3, 2, 2, 2, 3, 5, 7, 5, 3, 5, 7, 4, 2, 5, 5, 3, 5]
result = most_frequent_element(sample_list)

# wyświetlenie naszego wyniku
print("\nNasze liczby to: \n", sample_list)
print("\nNajczęściej występującą liczbą jest: ", result)
