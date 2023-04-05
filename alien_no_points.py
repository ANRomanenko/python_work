# Обращение к значениям методом get()

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.\n')
print(point_value)

oksana = {
    'first_name': 'oksana',
    'last_name': 'osadcha',
    'age': 28,
    'city': 'kiev',
    }

print(oksana)

names = {
    'dima': 35,
    'kolia': 34,
    'ira': 24,
    'andrey': 35,
    'ksuha': 28,
    }
print()

# for key, value in names.items():
#     print(f"\nKey: {key}")
#     print(f'Value: {value}')

for name, age in names.items():
    print(f"У моего друга, {name.title()} любимое число {age}")
print()
dima = names['dima']
print(f'У моего друга Димы любимое число {dima}')
kolia = names['kolia']
print(f'У моего друга Коли любимое число {kolia}')
ira = names['ira']
print(f'У моей подруги Иры любимое число {ira}')
andrey = names['andrey']
print(f'У моего друга Андрея любимое число {andrey}')
ksuha = names['ksuha']
print(f'У моей подруги Ксюши любимое число {ksuha}')


def num_sum(a, b):
    return a + b


print(num_sum(3, 7))

