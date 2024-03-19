print("\n=> funkcja concat_strings, która przyjmuje nieokreśloną"
      "\nliczbę argumentów typu string i łączy je w jeden ciąg znaków,"
      "\nrozdzielając spacją. Przetestuj funkcję na kilku zestawach stringów:\n")

# funkcja concat_strings
def concat_strings(*args):
    return ' '.join(args)

# testowanie naszej funkcji
print(concat_strings("Dzień", "dobry!", ";>"))
print(concat_strings("Python", "jest", "super!"))
print(concat_strings("Dzisiaj", "jest", "rok", "2024..."))
print(concat_strings("Kwiecień", "plecień", "bo", "przeplata:",
                     "trochę", "zimy,", "trochę", "lata..."))
