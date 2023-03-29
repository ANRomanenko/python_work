# Копирование списка
# Часто разработчик берет существующий список и создает на его основе совершенно новый список. Посмотрим, как работает копирование списков, и рассмотрим одну ситуацию, в которой копирование списка может принести пользу.
# Чтобы скопировать список, создайте сегмент, включающий весь исходный список без указания первого и второго индекса ([:]). Эта конструкция создает сегмент, который начинается с первого элемента и завершается последним; в результате создается копия всего списка.


my_foods = ['pizza', 'falafel', 'carrot', 'cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')


print("My favorite foods are:")
for myfood in my_foods:
    print(myfood.title())

print("\nMy friend's favorite foods are:")
for myfrends in friend_foods:
    print(myfrends.title())
print()

text_1 = "The irst three items in the list are:»"
print(text_1)
print(text_1[:15])
print()

text_2 = "Three items from the middle of the list are"
print(text_2)
print(text_2[11:][:16])
print()

text_3 = "The last three items in the list are"
print(text_3)
print(text_3[-13:])

# Копия программы пицца

my_pizza = ["paperoni", "chees", "patatas", "cremas"]
friend_pizza = my_pizza[:]

my_pizza.append("parmezan")
friend_pizza.append("salatas")

print("\nMy favorite pizzas are:")
for pizza in my_pizza:
    print(pizza.title())

print("\nMy friend’s favorite pizzas are")
for fpizza in friend_pizza:
    print(fpizza.title())
