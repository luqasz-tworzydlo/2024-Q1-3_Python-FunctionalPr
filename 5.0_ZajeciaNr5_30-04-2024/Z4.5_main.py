# funkcja dzielaca listę na części o określonej maksymalnej długości
# [ nasza funkcja zwraca listę podlist, gdzie każda
# podlista ma maksymalną długość max_length ]
def chunk_list(lst, max_length):
    return [lst[i:i + max_length] for i in range(0, len(lst), max_length)]

# przykładowe wykorzystanie naszej funkcji
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
max_part_length = 5
chunked_list = chunk_list(numbers, max_part_length)

# wyświetlenie naszego wyniku
print("\nNasze liczby: ", numbers,
      "\nNasza maksymalna długość: ", max_part_length)
print("\n=> Nasza podzielona lista na podlisty: \n", chunked_list)

print("\n=> Inne przykładowe wykorzystanie listy [z długością 7]: \n",
      chunk_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],7))
