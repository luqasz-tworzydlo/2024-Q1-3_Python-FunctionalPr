print("\n=> przykład użycia leniwego obliczania \n"
      "(lazy evaluation), na przykładzie generatorów")

def liczDo(max):
    count = 1
    while count <= max:
        yield count
        count += 1

licznik = liczDo(7)
for liczba in licznik:
    print(liczba)
