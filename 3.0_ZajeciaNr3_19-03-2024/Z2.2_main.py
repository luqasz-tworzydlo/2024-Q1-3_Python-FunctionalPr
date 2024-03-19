print("\n=> funkcja przyjmująca listę elementów"
      "\ni zwracająca listę wszystkich możliwych"
      "\n2-elementowych kombinacji tych elementów:\n")

from itertools import combinations

def WygenerowanieKombinacji_GenerateCombinations(lista_lst):
    return list(combinations(lista_lst, 2))

elementy_elements = ['A', 'B', 'C', 'D', 'E']
print(WygenerowanieKombinacji_GenerateCombinations(elementy_elements))
