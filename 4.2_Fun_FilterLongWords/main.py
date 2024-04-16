# Definicja funkcji filter_long_words
def filter_long_words(strings):
    average_length = sum(len(s) for s in strings) / len(strings)
    return [s for s in strings if len(s) > average_length]

# Lista słów
ListaSlow = ["witaj", "Python", "Java", "PHP", "University"]
PrzefiltrowanieSlowa = filter_long_words(ListaSlow)

# Wyświetlenie wyników (listy słów):
print("\nWyświetlenie listy słów (oryginalna i przefiltrowana):")
print("(1) Oryginalna lista słów:", ListaSlow)
print("(2) Filtrowana lista słów:", PrzefiltrowanieSlowa)
