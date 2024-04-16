# Definicja funkcji remove_duplicates
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Wykorzystanie funkcji remove_duplicates
oryginalnaLista_originalList = [1, 2, 3, 3, 4, 3, 1, 5, 6, 6, 7, 7, 5]
listaBezPowtorzen_uniqueList = remove_duplicates(oryginalnaLista_originalList)

# Wyświetlenie wszystkich wyników
print("\nWyświetlenie wyników:")
print("(1) Pierwotna (oryginalna) lista: ", oryginalnaLista_originalList)
print("(2) Lista po usunieciu wszystkich powtorzeń: ", listaBezPowtorzen_uniqueList)