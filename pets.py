# Удаление всех вхождений конкретного значения из списка
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
print()

# Именованные аргументы


def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(animal_type='hamster', pet_name='harry')

# Значения по умолчанию


def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='willie')

# Эквивалентные вызовы функций
# Все следующие вызовы являются допустимыми для данной функции:

# Пес по имени Вилли.
describe_pet('willie')
describe_pet(pet_name='willie')
# Хомяк по имени Гарри.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

