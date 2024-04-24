# zaimportowanie narzędzia 'permutations' z modułu 'intertools'
from itertools import permutations

# nasza funkcja generująca wszystkie permutacje elementów listy
def generate_permutations(lst):
    return list(permutations(lst))

# przykładowe użycie naszej funkcji
sample_list = [1, 2, 3]
all_permutations = generate_permutations(sample_list)
# wyświetlenie uzyskanych wyników
print("\n=> Pierwszy sposób wyświetlenia wszystkich permutacji:")
for perm in all_permutations:
    print(perm)

# inny sposób użycia naszej funkcji & wyświetlenie wyników
print("\n=> Drugi sposób wyświetlenia wszystkich permutacji: \n", generate_permutations([1, 2, 3]))
