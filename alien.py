# Словари
# В Python словарь заключается в фигурные скобки {}, в которых приводится последовательность пар «ключ-значение»,

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'\nYou just earned {new_points} points!\n')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print()

# Создание пустого словаря
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print()

# Изменение значений в словаре
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")
print()

# Скорость пришельца
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
print(f"Original position: {alien_0['x_position']}")

# Пришелец перемещается вправо.
# Вычесляем величину смещения на основании текущей скорости.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3

# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print()

# Удаление пар «ключ-значение»

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
print()

# Словарь с однотипными объектами

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
print()
for name in favorite_languages.keys():
    print(name.title())
print()
# print(favorite_languages['jen'])

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print("Hi", name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t {name.title()}, I see you love {language}!")
print()

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print()
# Перебор ключей словаря в определенном порядке
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")
print()
# Перебор всех значений в словаре

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following language have been mentioned:")
for language in sorted(set(favorite_languages.values())): # Избавляемся дубликатов множеством set()
    print(language.title())
print()

niles = {'dnipro': 'ukraine', 'nile': 'egypt', 'sozh': 'belarus'}
for nile, city in niles.items():
    print(f"The {nile.title()} runs through {city.title()}")

print()

# Список словарей
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print()

# Создание пустого списка для хранения пришельцев.
aliens = []

# Создание 30 зелёных пришельцев

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print("...")

# Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}")

