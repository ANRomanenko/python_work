# Определение функции
# Вот простая функция с именем greet_user (), которая выводит приветствие:

# Передача информации функции
def greet_user(username):
    """Выводит простое приветсвие"""
    print(f"Hello, {username.title()}")


greet_user("jesse!")
print()

# Упражнение 8.1 (Сообщение:)-----(Изучаем Python (Мэтиз))


def display_message():
    print('Аргументы и параметры')


display_message()
print()

# Упражнение 8.2 (Любимая книга:)-----(Изучаем Python (Мэтиз))


def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book("alice in wonderland»")