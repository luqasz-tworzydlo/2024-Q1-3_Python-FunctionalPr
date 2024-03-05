# generator - ciąg liczb Fibonacciego
print("\n(1) Generator produkujący nieskończony ciąg liczb Fibonacciego: ")

def CiagFibonacciego():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

GeneratorFibonacciego = CiagFibonacciego()
for _ in range(12): # dla wyświetlenia pierwszych 12 liczb z ciągu
    print(next(GeneratorFibonacciego))

print("\n(2) Generator czytający duży plik tekstowy linia po linii: \n")

SciezkPliku = "C:\\Users\\luqasz\\Desktop\\DuzyPlik.txt"

def WczytaniePlikuLiniPoLinii(SciezkPliku):
    with open(SciezkPliku, 'r') as file:
        for line in file:
            yield line

GeneratorDlaPliku = WczytaniePlikuLiniPoLinii(SciezkPliku)
for liniaPoLinii in GeneratorDlaPliku:
    print(liniaPoLinii)
