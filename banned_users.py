# Проверка отсутствия значения в списке

banned_users =  ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Логические выражения

car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')
print()
# ----------------------------------------
# True
# 1 - Условие (True)
pets = ['cats', 'dogs', 'rebbit']
name_pets = 'bonia'

if name_pets not in pets:
    print(f'{name_pets.title()}, Not here this list! True\n')

# 2 - Условие (True)
age_0 = 35
age_1 = 28
print(age_0 >= 34 or age_1 >= 34)
print()

# 3 - Условие (True)
pizza = ['peperoni', 'parmezan', 'chees']
print('peperoni' in pizza)
print()

# 4 - Условие (True)
number = 35
print(number == 35)
print()

# 5 - Условие (True)