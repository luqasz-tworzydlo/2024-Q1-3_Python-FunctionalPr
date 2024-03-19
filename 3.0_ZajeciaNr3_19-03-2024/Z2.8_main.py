print("\n=> wyrażenie lambda, które przyjmuje trzy argumenty"
      "\ni zwraca ich średnią arytmetyczną; wydrukowanie"
      "\n(wyświetlenie) wyniku dla trzech przykładowych liczb:\n")

srednia_average = lambda x, y, z: (x + y + z) / 3

print(srednia_average(1, 3, 5))
# nasz wynik to: 3.0
print(srednia_average(5, 25, 180))
# nasz wynik to: 70.0
print(srednia_average(10, 30, 50))
# nasz wynik to: 30.0
