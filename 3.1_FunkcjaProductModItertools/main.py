print("\n=> użycie funkcji product z modułu itertools,"
      "\ngenerujący i wyświetlający wszystkie możliwe"
      "\nkombinacje liter z dwóch list: ['A', 'B'] i ['C', 'D']:\n")

# importowanie funkcji itertools
import itertools

listaA = ['A', 'B']
listaB = ['C', 'D']

# poniżej są generowane kombinacje
combinations_kombinacje = itertools.product(listaA, listaB)

# wyświetlanie wygenerowanych kombinacji
for kombinacja_combo in combinations_kombinacje:
    print(kombinacja_combo)
