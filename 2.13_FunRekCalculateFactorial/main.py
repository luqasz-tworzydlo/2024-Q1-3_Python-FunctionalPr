print("\n=> funkcja rekurencyjna calculate_factorial, \n"
      "która oblicza silnię podanej liczby:")

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

print(calculate_factorial(0))
print(calculate_factorial(1))
print(calculate_factorial(2))
print(calculate_factorial(3))
print(calculate_factorial(4))
print(calculate_factorial(5))
print(calculate_factorial(6))
print(calculate_factorial(7))
print(calculate_factorial(8))
print(calculate_factorial(9))
