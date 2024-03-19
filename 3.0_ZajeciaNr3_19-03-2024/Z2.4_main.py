print("\n=> użycie wyrażenia walrus operator (:=)"
      "\nwewnątrz list comprehension do stworzenia"
      "\ni wydrukowania (wyświetlenia) listy kwadratów"
      "\nliczb z podanej listy, które są większe niż 10:\n")

numeryNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# użycie operatora walrus w list comprehension
ListaKwadratowWiekszaNiz10_SquaresGreaterThan10 = [square for number in numeryNumbers if (square := number ** 2) > 10]

# wyrukowanie (wyświetlenie) wyniku
print(ListaKwadratowWiekszaNiz10_SquaresGreaterThan10)
