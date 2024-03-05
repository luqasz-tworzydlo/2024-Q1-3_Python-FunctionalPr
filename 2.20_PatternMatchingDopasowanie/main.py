print("\nFunkcja, która używa dopasowania wzorców do analizy \n"
      "i reakcji na różne struktury danych (np. listy, krotki):\n")

def AnalizaStrukturyDanych_AnalyzeDataStructure(dane_data):
    match dane_data:
        case []:
            return "=> to jest pusta lista"
        case [_]:
            return "=> to jest lista z jednym elementem"
        case [_, *rest]:
            return (f"=> to jest lista z wieloma elementami, \n"
                    f"gdzie pierwszy element to: {dane_data[0]}")
        case ():
            return "=> to jest pusta krotka (tuple)"
        case (_,):
            return "=> to jest krotka z jednym elementem"
        case (_, *rest):
            return (f"=> to jest krotka z wieloma elementami, \n"
                    f"gdzie pierwszy element to: {dane_data[0]}")
        case _:
            return "=> tutaj jest inny typ danych"

print(AnalizaStrukturyDanych_AnalyzeDataStructure([]))           # to jest pusta lista
print(AnalizaStrukturyDanych_AnalyzeDataStructure([1]))          # to jest lista z jednym elementem
print(AnalizaStrukturyDanych_AnalyzeDataStructure([1, 2, 3]))    # to jest lista z wieloma elementami, gdzie pierwszy element to: 1
print(AnalizaStrukturyDanych_AnalyzeDataStructure(()))           # to jest pusta krotka (tuple)
print(AnalizaStrukturyDanych_AnalyzeDataStructure((1,)))         # to jest krotka z jednym elementem
print(AnalizaStrukturyDanych_AnalyzeDataStructure((1, 2, 3)))    # to jest krotka z wieloma elementami, gdzie pierwszy element to: 1
print(AnalizaStrukturyDanych_AnalyzeDataStructure("Witaj :>"))   # tutaj jest inny typ danych
