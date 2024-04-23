# funkcja zamieniająca danej macierzy wiersze na kolumny (bądź odwrotne)
# uwaga: macierz musi być tych samych rozmiarów, mieć tą samą długóść
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# przykładowe użycie naszej funkcji
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n=> Pierwotna macierz")
for row in matrix:
    print(row)

print("\n=> Odwrócona macierz: ")
transposed = transpose_matrix(matrix)
for row in transposed:
    print(row)

# nasz wynik powinien
# wyglądać następująco:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
