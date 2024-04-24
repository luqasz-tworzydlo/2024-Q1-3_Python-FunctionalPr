# funkcja podmieniająca duże litery na małe oraz małe na duże
def swap_case_manual(s):
    new_string = []
    for char in s:
        if char.islower():
            new_string.append(char.upper())
        else:
            new_string.append(char.lower())
    return ''.join(new_string)

# przykładowe użycie funkcji
sample_text = "Witam Was ;P"
result_manual = swap_case_manual(sample_text)

# wyświetlenie wyniku końcowego
print("\n=> Oryginalny wygląd naszego tekstu: ", sample_text)
print("=> Nowy wygląd tekstu po zamianie: ", result_manual)
