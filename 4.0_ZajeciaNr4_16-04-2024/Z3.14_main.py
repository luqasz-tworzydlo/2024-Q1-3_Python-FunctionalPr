# funkcja zliczająca unikalne elementy w liście
def count_unique_elements(lst):
    unique_elements = set(lst) # utworzenie zbioru z listy, co automatycznie usunie duplikaty
    return len(unique_elements) # zwrócenie liczby unikalnych elementów

# przykładowe użycie naszej funkcji
sample_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3]
unique_count = count_unique_elements(sample_list)

# wyświetlenie naszego wyniku
print("\n=> Nasz wynik: ", unique_count)
