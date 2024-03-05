print ("\n=> Zaimplementowana funkcja make_multiplier, \n"
       "która zwraca inną funkcję, służącą do mnożenia \n"
       "liczby przez ustalony mnożnik:")

def make_multiplier(x):
    def multipliter(n):
        return x * n

    return multipliter

double = make_multiplier(3)
print(double(10))
