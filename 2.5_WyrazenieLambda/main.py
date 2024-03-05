print("=> wyrażenia lambda tworzące anonimową funkcję, \n"
      "która podnosi liczbę do kwadratu, a następnie \n"
      "używa jej do przekształcenia listy liczb:")

wybraneLiczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]
liczbyDoKwadratu = list(map(lambda x: x ** 2, wybraneLiczby))

print(liczbyDoKwadratu)
