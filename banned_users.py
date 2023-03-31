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

x = 0
if x == 0:
    x += 1

print(100/x, 'True')
print()

# ----------------------------------------
# False
# 1 - Условие (False)

sums = 18
print(sums == 17)

# 2 - Условие (False)
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

# 3 - Условие (False)
auto = ['audi', 'bmw', 'toyota']
print('ford' in auto)
print()

# 4 - Условие (False)
eat = ['peperoni', 'chees', 'salat']
eats = 'peperoni'
if eats not in eat:
    print(f'{eats.title()}, Hello')
else:
    print(False)

# 5 - Условие (False)
y = 0
if y == 1:
    y =+ 1
else:
    print(False)

print()

mashina = 'Audi'
print(mashina.lower() == 'audi')
print(mashina)