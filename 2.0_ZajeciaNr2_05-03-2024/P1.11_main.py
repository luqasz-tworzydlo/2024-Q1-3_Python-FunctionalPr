print("\n=> funkcja przyjmująca listę stringów, sortująca je \n"
      "w porządku rosnącym według długości z użyciem funkcji anonimowej:")

def sortowanieStringowDlugosc(listaSlowString):
    return sorted(listaSlowString, key=lambda s: len(s))

slowa = ["Polska", "Hiszpania", "Irlandia", "Anglia", "Australia", "Singapur"]
dlugoscSlow = sortowanieStringowDlugosc(slowa)

print(dlugoscSlow)
