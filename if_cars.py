# Команды if

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

car = 'bmw'
print(car == 'bmw')
print()

car = 'audi'
print(car == 'bmw')
print()

car = 'Audi'
print(car == 'audi')
print()

car = 'Audi'
print(car.lower() == 'audi') # Функция lower() не изменяет значение, которое изначально хранилось в car, так что сравнение не отражается на исходной переменной:

print(car)