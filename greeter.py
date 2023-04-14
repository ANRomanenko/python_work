# Содержательные подсказки

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")
# print()
#
# promt = "If you tell us who you are, we can personalize the messages you see."
# promt += "\nWhat is your first name? "
#
# name = input(promt)
# print(f"\nHello, {name}!")
# print()

# Использование int() для получения числового ввода
age = input("How old are you? ")
age = int(age)
print(age >= 18)
print()


def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Бесконечный цикл!


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
print()


# Упражнение 8.6 (Название городов)


def city_country(city, country):
    full_city_country = f"{city} {country}"
    return full_city_country.title()


names = city_country("santiago", "chile")
print(names)

names = city_country("kiev", "ukraine")
print(names)
print()

# Упражнение 8.7 (Альбом)


def make_album(name, album_name, dorogka=None):
    musicant = {'name': name, 'album': album_name}
    if dorogka:
        musicant['num'] = dorogka
    return musicant


music = make_album('jimi', 'henx', dorogka=28)
print(music)

music = make_album('asti', 'pervuy')
print(music)
print()

# Упражнение 8.8 (Пользовательские альбомы)


def make_album(name, album_name, dorogka=None):
    musicant = {'name': name, 'album': album_name}
    if dorogka:
        musicant['num'] = dorogka
    return musicant


while True:
    print("\nНапишите исполнителя и название альбома: ")
    print("Для выхода нажмите 'q' ")

    i_name = input("Введите исполнителя: ")
    if i_name == 'q':
        break

    a_name = input("Введите название альбома: ")
    if a_name == 'q':
        break

    make = make_album(i_name, a_name)
    print(f"\nИмя исполнителя и альбом: {make}")