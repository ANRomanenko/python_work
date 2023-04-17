# Сохранение информации о заказанной пицце.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Описание заказа.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
print()


# Передача произвольного набора аргументов
def make_pizza(size, *toppings):
    """Вывод списка заказных топпингов."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')