print("\n=> Funkcja filter do wybrania słów z listy, "
      "które są dłuższe niż 5 znaków (liter):")


listaSlow = ["niedziela", "poniedzialek", "wtorek",
             "sroda", "czwartek", "piatek", "sobota"]
dlugieSlowa = list(filter(lambda slowo: len(slowo) > 5, listaSlow))

print(dlugieSlowa)
