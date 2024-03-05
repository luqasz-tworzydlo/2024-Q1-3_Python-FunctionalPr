global_variable = "Python 3.x jako zmienna globalna"

def przykladowaFunkcja():
    local_variable = "Python 3.11 jako zmienna lokalna"

    print("\n=> Wyswietlenie funkcji globalnej")
    print(global_variable)

    print("\n=> Wyswietlenie funkcji lokalnej \n",
          local_variable)

przykladowaFunkcja() # wywolanie funkcji

def ZmianaWartosciFunkcjiGlobalnej():
    global new_global_variable
    new_global_variable = "Python 4.x jako nowa zmienna globalna"
    # print("\n=> Nowa wartosc zmiennej globalnej: ", new_global_variable)

ZmianaWartosciFunkcjiGlobalnej()
print("\n=> Nowa wartosc zmiennej globalnej: \n",
      new_global_variable)
