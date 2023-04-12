# Возвращение словаря


def build_person(first_name, last_name):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    return person


name = build_person('lera', 'hendrix')
print(name)
print()


def build_person(first_name, last_name, age=None):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)