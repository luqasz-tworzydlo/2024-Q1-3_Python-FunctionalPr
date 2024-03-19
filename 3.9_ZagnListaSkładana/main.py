print("\n=> stworzenie i wydrukowanie (wyświetlenie) macierzy 3x3 za pomocą"
      "\nzagnieżdżonej listy składanej, wypełnioną wartościami od 1 do 9:\n")

Macierz_Matrix = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]

for Rzad_Row in Macierz_Matrix:
    print(Rzad_Row)
