# funkcji capitalize_all_words zamieniającą pierwszą literę każdego słowa na wielką literę
def capitalize_all_words(s):
    return s.title()

# przykładowe użycie naszej funkcji
my_string = "witaj Polsko! dzień dobry!."
capitalized_string = capitalize_all_words(my_string)

# wyświetlenie wyniku końcowego
print("\n=> Słowa (stringi) po zmianie pierwszej"
      " małej litery na dużą literę: \n", capitalized_string)
