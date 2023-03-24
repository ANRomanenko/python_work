# Списки

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])
print()
print(bicycles[-1]) # Если запросить элемент с индексом –1, Python всегда возвращает последний элемент в списке:
print()

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
print()
my_lists = ['Audi', 'Volkswagen', 'Toyota', 'Mercedes']
auto = f'My first auto {my_lists[0].title()} my next auto {my_lists[2].title()}'
print(auto)
print()
names = ['Maxim', 'Dima', 'Olia', 'Sergey']
print(names)
names[1] = 'Katia'
print(names)
names.append('Ira') # Присоединение элементов в конец списка
print(names)
# print(names[0:4])
print()
text = f'This name: {names[0].title()}'
text = f'This name: {names[1].title()}'
text = f'This name: {names[2].title()}'
text = f'This name: {names[3].title()}'
print(text)
print()
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)

motos = ['honda', 'yamaha', 'suzuki']
motos.insert(0, 'ducati') # Вставка элементов в список
print(motos)
print()
motos = ['honda', 'yamaha', 'suzuki']
print(motos)
motos = ['honda', 'yamaha', 'suzuki']
del motocycles[0] # Удаление элемента с использованием команды del
print(motocycles)
print()
motos = ['honda', 'yamaha', 'suzuki']
print(motos)
popped_motos = motos.pop() # Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления. Удалим мотоцикл из списка:
print(motos)
print(popped_motos)
print()
motos = ['honda', 'yamaha', 'suzuki']
last_owned = motos.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motos.pop(0) # Извлечение элементов из произвольной позиции списка
print(f"The last motorcycle I owned was a {first_owned.title()}.")
print()
motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motos)
motos = ['honda', 'yamaha', 'suzuki', 'ducati']
motos.remove('ducati') # Удаление элементов по значению! Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение элемента, используйте метод remove().
print(motos)
print()
motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motos)
too_expensive = 'ducati'
motos.remove(too_expensive)
print(motos)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print()
peoples = ['ira', 'katia', 'anastasia', 'alexandra']
print(f'Сегодня придти не сможет {peoples[1].title()}')
del peoples[1]
peoples.append('lera')
for people in peoples:
    print(f"Приглашаю, Вас {people.title()} сегодня восетить мой дом и угоститься прекрасным ужином")