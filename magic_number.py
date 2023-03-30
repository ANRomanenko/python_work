# Оператор if

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
print()
# Использование and проверки нескольких условий
# Чтобы проверить, что два условия истинны одновременно, объедините их ключевым словом and; если оба условия истинны, то и все выражение тоже истинно. Если хотя бы одно (или оба) условие ложно, то и результат всего выражения равен False.

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False (Ложь)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21) # True (Истина)
print()
# Использование or для проверки нескольких условий
# Ключевое слово or тоже позволяет проверить несколько условий, но результат общей проверки является истинным в том случае, когда истинно хотя бы одно или оба условия. Ложный результат достигается только в том случае, если оба условия ложны.

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
print()

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)
print()

# Проверка вхождения значений в список
requested_topping = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

