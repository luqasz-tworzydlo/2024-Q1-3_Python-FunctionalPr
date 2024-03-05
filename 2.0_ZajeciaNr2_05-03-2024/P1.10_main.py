print("\n=> użycie wyrażenia generatorowego do stworzenia generatora, \n"
      "produkującego nieskończoną sekwencję liczb parzystych:")

def even_numbers_generator():
    n = 0
    while True:
        yield n
        n += 2

generator = even_numbers_generator()
f5eN = [next(generator) for _ in range(5)]
print(f5eN) # first 5 even numbers [ wyświetlenie ]
