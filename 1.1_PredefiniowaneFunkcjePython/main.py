# przykłady predifiniowanych funkcji

# przykłady nr 1 [ funkcja max() ]
print("\n=> (1) Zastosowanie funkcji max()")
print(max(20, 2, 2024)) # tutaj zwróci nam 2024
print(max([15, 41, 12]))  # tutaj zwróci nam wartość 41
print(max('Angelika', 'Mariusz', 'Daria'))  # tutaj zwróci nam Mariusz

# przykłady nr 2 [ funkcja min() ]
print("\n=> (2) Zastosowanie funkcji min()")
print(min(20, 2, 2024)) # tutaj zwróci nam 2
print(min([15, 41, 12]))  # tutaj zwróci nam wartość 12
print(min('Angelika', 'Mariusz', 'Daria'))  # tutaj zwróci nam Angelika

# przykłady nr 3 [ funkcja len() ]
print("\n=> (3) Zastosowanie funkcji len()")
print(len("Daria"))  # zwróci nam wartość 5 (ilość znaków)
print(len([1, 5, 4, 5]))  # tutaj nam zwróci wartość 4

# przykłady nr 4 [ funkcja type() ]
print("\n=> (4) Zastosowanie funkcji type()")
print(type(2024))  # zwróci nam informacje o typie: int
print(type([2, 0, 2, 4]))  # tutaj zwróci nam informacje: list
print(type("Python"))  # tutaj zwróci nam informacje: str

# przykłady nr 5 [ funkcja input() ]
print("\n=> (5) Zastosowanie funkcji input()")
name = input("Jak masz na imię? ;>\n* ")
print(f"Miło mi! Witaj {name}! ^_^")
