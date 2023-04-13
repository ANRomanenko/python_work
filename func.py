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

# Упражнение 8.3 (Футболка)-----(Изучаем Python (Мэтиз))


def make_shirt(size, text):
    print(f"\nРазмер футболки {size.title()}.")
    print(f"Моя футболка с размером {size.title()}, и текстом: {text.title()}")


make_shirt("l", 'Жизнь прекрасна!') # Позиционные аргументы!
make_shirt(size='l', text='Жизнь прекрасна!') # Именнованные аргументы!
print() # ------------------------------------------------------------------------

# Упражнение 8.4 (Большие футболки)-----(Изучаем Python (Мэтиз))


def make_shirt(size='l', text='i love python'): # значения по умолчанию
    print(f"\nРазмер футболки {size.title()}.")
    print(f"Моя футболка с размером {size.title()}, и текстом: {text.title()}")


make_shirt()
make_shirt(size='s', text='python')
print() # ------------------------------------------------------------------------

# Упражнение 8.5 (Города)-----(Изучаем Python (Мэтиз))


def describe_city(city, country='ukraine'):
    print(f"\n{city.title()} is in {country.title()}")


describe_city("reykjavik", "iceland")
describe_city("kiev")
describe_city("dnipro")