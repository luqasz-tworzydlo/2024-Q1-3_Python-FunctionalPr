# Definicja funkcji recursive_sum
def recursive_sum(liczby):
    LacznieSuma_TotalSum = 0
    for elementy in liczby:
        if isinstance(elementy, list):
            LacznieSuma_TotalSum += recursive_sum(elementy)
        else:
            LacznieSuma_TotalSum += elementy
    return LacznieSuma_TotalSum

zagniezdzonaLista_nestedList = [1, 2, [3, 4], [5, [6, 7]], 8]
LacznieSuma_TotalSum = recursive_sum(zagniezdzonaLista_nestedList)

# Wyświetlenie wyniku (działanie funkcji)
print("\nNasze wyniki (zagnieżdzona lista i jego suma):")
print("(1) Zagnieżdżona lista:", zagniezdzonaLista_nestedList)
print("(2) Suma wszystkich liczb:", LacznieSuma_TotalSum)
