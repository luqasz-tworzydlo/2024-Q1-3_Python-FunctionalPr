# Funkcja dodająca indeksy (numery) do danych elementów
def zip_with_index(lst):
    return [(index, item) for index, item in enumerate(lst)]

# przykładowe użycie funkcji
my_list = ['mango', 'borowka', 'wisnia', 'mango', 'marakuja']
indexed_list = zip_with_index(my_list)

# wyświetlenie naszych danych z numerami
print("\nNasza liczba z indeksami (numerami): ", indexed_list)
