# Проверка неравенства

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age = 18
print(age == 18)
print()

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'peperoni' in requested_toppings:
    print('Adding peperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print("\nFinished making your pizza!")
print()

alien_color = 'green'
if alien_color == 'green':
    print(f'Игрок {alien_color.title()} заработал 5 очков!')
print()

x = 9
if x == 9:
    print('Text')
y = 7
if y == 8:
    print()
print()

gree_color = 'gree'
if gree_color == 'green':
    print(f'Игрок {gree_color.title()} заработал 5 очков!')
else:
    print(f'Игрок {gree_color.title()} заработал 14 очков!')
print()

alien_color = 'green'
if alien_color == 'green':
    print(f'Игрок {alien_color.title()} заработал 5 очков!')
elif alien_color == 'yellow':
    print(f'Игрок {alien_color.title()} заработал 10 очков!')
else:
    print(f'Игрок {alien_color.title()} заработал 15 очков!')
print()

age = 4
if age < 2:
    print("младенец")
elif age >= 2 and age < 4:
    print("малыш")
elif age >= 4 and age < 13:
    print("ребенок")
elif age >= 13 and age < 20:
    print("подросток")
elif age >= 20 and age < 65:
    print("взрослый")
else:
    print("пожилой")

print()

favorite_fruits = ['bananas', 'orange', 'limon']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'kivi' in favorite_fruits:
    print("You really like kivi!")
if 'orange' in favorite_fruits:
    print("You really like orange")
if 'limon' in favorite_fruits:
    print("You really like limon")
if 'kokos' in favorite_fruits:
    print("You really like kokos")

print("\nFinish happy fruits")