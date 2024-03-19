print("\n=> jednolinijkowa funkcja is_palindrome, która sprawdza,"
      "\nczy dany ciąg znaków (bez uwzględniania wielkości liter"
      "\ni białych znaków) jest palindromem (czyli wyrażeniem brzmiącym"
      "\ntak samo czytane od lewej do prawej i od prawej do lewej):\n")

is_palindrome = lambda s: (cleaned := ''.join(c for c in s.lower() if c.isalnum())) == cleaned[::-1]

print(is_palindrome("Czlowiek tot keiwolzc"))  # True ( prawda )
print(is_palindrome("Noteton"))                # True ( prawda )
print(is_palindrome("przyklad"))               # False ( fałsz )
print(is_palindrome("Nowy Targ, góry,"
                    "Zakopane – na pokazy róg,"
                    "graty won"))              # True ( prawda )
