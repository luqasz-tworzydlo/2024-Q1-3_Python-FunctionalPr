print("\n=> przykład funkcji, która operuje na niemutowalnych \n"
      "strukturach danych, takich jak krotki (tuple)")

def sumaKrotki_SumOfTuple(liczbyKrotki):
    lacznie = 0
    for liczba in liczbyKrotki:
        lacznie += liczba
    return lacznie

liczby = (1, 2, 3, 4, 5, 6, 7)
print("-> suma krotki: ", sumaKrotki_SumOfTuple(liczby))
