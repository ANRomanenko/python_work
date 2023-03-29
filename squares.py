# С помощью функции range() можно создать практически любой диапазон чисел. Например, как бы вы создали список квадратов всех целых чисел от 1 до 10? В языке Python операция возведения в степень обозначается двумя звездочками (**). Один из возможных вариантов выглядит так:

# squares = []
# for value in range(1, 11):
#     square = value**2 # возведения в степень
#     squares.append(square)
#
# print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2) # возведения в степень

print(squares)
print()

# Некоторые функции Python предназначены для работы с числовыми списками. Например, вы можете легко узнать минимум, максимум и сумму числового списка:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print()

spisok = [val**2 for val in range(1, 11)] # Генераторы списков
print(spisok)

for numbers in range(1, 21):
    print(numbers)
print()


millions = []
for mill in range(1, 10001):
    millions.append(mill)
print(millions)
print(min(millions))
print(max(millions))
print(sum(millions))
print()

for chisla in range(1, 20, 2):
    print(chisla)
print()
for kratnost in range(3, 30):
    print(kratnost)
print()

for kub in range(1, 10):
    print(kub**3)
print()

kubik = [spik**3 for spik in range(1, 10)]
print(kubik)