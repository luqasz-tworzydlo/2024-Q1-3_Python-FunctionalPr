print("\n=> zaimplementowanie dekorator safe_function,"
      "\nktóry łapie wyjątki podczas wywołania funkcji"
      "\ni zamiast przerywać program, wypisuje informację"
      "\no błędzie i zwraca None; oraz przetestowanie"
      "\ndekorator na funkcji dzielącej dwie liczby:\n")

def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"=> Wystąpił błąd: {e}")
            return None
    return wrapper

# użycie dekoratora (dzielenie)
@safe_function
def PodzielDivide(a, b):
    return a / b

# przetestowanie funkcję dzielącą
print(PodzielDivide(24, 2))
# będzie u nas wynik 12
print(PodzielDivide(24, 0))
# będzie u nas informacja o błędzie
# oraz zostanie zwrócona wartość None
print(PodzielDivide(24, 3))
# będzie u nas wynik 8
print(PodzielDivide(24, 4))
# będzie u nas wynik 6
print(PodzielDivide(24, 8))
# będzie u nas wynik 3
