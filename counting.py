# Цикл While в действии

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print()

# Предотвращение зацикливания
x = 1
while x <= 5:
    print(x)
    x += 1

# Упражнение 7.4 (Топпинг для пиццы)
topping = "\nВыбирете топпинг для пиццы:"
topping += "\nПосле завершения выбора нажмире 'quit' "
top_2 = []
while True:
    pizza = input(topping)
    top_2.append(pizza.title())
    if pizza == "quit":
        print(f"\nВаш заказ: \n{top_2}")
        break
    else:
        print(f"Дополнение, {pizza.title()} включено в ваш заказ!")
print()

# Упражнение 7.5 (Билеты в кино)
kino = "\nВы узнаете стоимость билета после того как скажите какой возраст у вас или вашего ребёнка!"
kino += "\nСколько вам лет: "
# kino += "\nДля выхода нажмите 'quit'"
while True:
    # возраст уже ввели в message, не нужно его спрашивать для age1 ещё раз
    message = input(kino)
    # но перед тем, как перевести message в kino1, проверим, не ввели ли quit
    # если сначала попробовать перенести значение в kino1, будет вызвано исключение, в результате попытки использовать оператор int('quit')
    if message == "quit":
        break
    kino1 = int(message)
    if kino1 <= 3:
        print("Вход бесплатный для, Вашего ребёнка")
    elif kino1 > 3 and kino1 <= 12:
        print("Билет стоит 10$")
    else:
        print("Билет стоит 15$")

print()

count = 0
while count <= 20:
    print(count)
    count += 1