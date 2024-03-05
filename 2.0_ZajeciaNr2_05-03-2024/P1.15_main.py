print("\n=> currying dla funkcji add, która przyjmuje dwa argumenty, \n"
      "dzieląc ją na dwie funkcje, z których każda przyjmuje jeden argument")

def add(x):
    def add_y(y):
        return x + y
    return add_y

# add_t5 => add to five (dodaj do pięciu)
add_t5 = add(5)

print(add_t5(7))
print(add_t5(10))
