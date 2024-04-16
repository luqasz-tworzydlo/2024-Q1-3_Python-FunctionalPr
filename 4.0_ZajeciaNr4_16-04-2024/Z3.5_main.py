# Zdefiniowanie funkcji generate_fibonacci
def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generatorFibonacci_fibonacciGenerator = generate_fibonacci()

# Użycie generatora do wygenerowania pierwszych (wybranych) liczb ciągu Fibonacciego
pierwsze10liczbFibb_first10fibonacciNumbers = [next(generatorFibonacci_fibonacciGenerator) for _ in range(10)]
pierwsze20liczbFibb_first10fibonacciNumbers = [next(generatorFibonacci_fibonacciGenerator) for _ in range(20)]
pierwsze30liczbFibb_first10fibonacciNumbers = [next(generatorFibonacci_fibonacciGenerator) for _ in range(30)]

# Wyświetlenie naszych wyników (ciąg Fibonacciego)
print("\nWyniki naszych ciągów Fibonacciego:"
      "\n(1) Pierwsze 10 liczb ciągu Fibonacciego:", pierwsze10liczbFibb_first10fibonacciNumbers,
      "\n(2) Pierwsze 20 liczb ciągu Fibonacciego:", pierwsze20liczbFibb_first10fibonacciNumbers,
      "\n(3) Pierwsze 30 liczb ciągu Fibonacciego:", pierwsze30liczbFibb_first10fibonacciNumbers)