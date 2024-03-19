print("\nzaimplementowanie funkcji generatorowej fibonacci,"
      "\nktóra generuje nieskończony ciąg liczb Fibonacciego"
      "\ni wydrukowanie (wyświetlenie) pierwszych 10 liczb tego ciągu:\n")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# utworzenie generatora
fib_gen = fibonacci()

# wyświetlenie / wydrukowanie pierwszych 10 liczb z ciągu Fibonacciego
for _ in range(10):
    print(next(fib_gen))
