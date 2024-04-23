# funkcja dzieląca listę na podlisty o zadanej długości
def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# przykładowe użycie naszej funkcji
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
chunk_size = 5
splitted_list = split_list(original_list, chunk_size)

# wyświetlenie naszych wyników
print("\n(1) Oryginalna lista: ", original_list)
print("(2) Podzielona lista: ", splitted_list)
