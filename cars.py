cars = ["bmw", "toyota", "audi", "subaru"]
# cars.sort()
print(cars) # Постоянная сортировка списка методом sort()
print()

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) # Временная сортировка списка функцией sorted()

print("\nHere is the original list again:")
print(cars, "\n")

cars.reverse() # Вывод списка в обратном порядке
print(cars)
cars.reverse() # Метод reverse() осуществляет постоянное изменение порядка элементов, но вы можете легко вернуться к исходному порядку, снова применив reverse() к обратному списку.
print(cars, '\n')

countries = ['Dubai', 'America', 'China', 'Turkey', 'Portugal']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print("\nЯ бы хотел побывать в", len(countries), "странах мира!")

languages = ['Spain', 'Ukraine', 'Portugal', 'France', 'Italian']
print(f"Здесь находится спимок из", len(languages), f'языков, например {languages}')
print(f"Я бы хотел выучить {languages[0].title()} язык!")
languages.sort()
print(languages)
util = languages.pop(0)
print(f'\nМы удалили язык! {util.title()}')
print("У нас осталось", len(languages), f'языка в списке:\n{languages}')
print(languages[2])
