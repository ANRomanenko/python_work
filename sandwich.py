# Упражнение 7.8 (Сэндвичи)-----(Изучаем Python (Мэтиз))
sandwich_orders = ['burger', 'marakuya', 'chitos', 'peperoni', 'mac'] # Заполненый список сендвичей
finished_sandwiches = [] # Пустой список сендвичей

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your tuna sandwich: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nВсе изготовленный сендвичи")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
print()

# Упражнение 7.9 (Без пастрами)-----(Изучаем Python (Мэтиз))
sandwich_orders = ['burger', 'marakuya', 'pastrami',  'chitos', 'pastrami', 'peperoni', 'mac', 'pastrami']
print(sandwich_orders)
print("\nВ списке 'pastrami' больше нет!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# Упражнение 7.10 (Отпуск мечты)-----(Изучаем Python (Мэтиз))
responses = {}

polling_activa = True

while polling_activa:
    name = input("\nКак вас зовут? ")
    responce = input("Где бы вы хотели побывать в отпуске? ")

    # Сохраняем ответы в словаре
    responses[name] = responce

    # Проверка продолжения опроса
    repeat = input("Желаете продолжить опрос? да/ нет? ")
    if repeat == 'нет':
        polling_activa = False

print("\n--- Результаты опроса! ---")
for name, responce in responses.items():
    print(f"{name}, Вы выбрали отпуск: {responce}")