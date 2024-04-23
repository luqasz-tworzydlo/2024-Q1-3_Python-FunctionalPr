# funkcja remove_whitespace usuwająca białe znaki z każdego elementu listy stringów
def remove_whitespace(string_list):
    return [s.strip() for s in string_list]

# przykładowe użycie naszej funkcji
my_strings = ['      Dzień ', '     dobry      ', '  Polsko!     ']
no_whitespace_list = remove_whitespace(my_strings)

# wyświetlenie efektu końcowego, po zastosowaniu funkcji
print("\n=> Nasza lista bez tzw. białych znaków: \n", no_whitespace_list)
