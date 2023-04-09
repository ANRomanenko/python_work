# Перемещение элементов между списками

# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


cities = {
    'kiev': {
        'country': 'ukraine',
        'people': 5200000,
        'population': 'lavra',
        },

    'madrid':{
        'country': 'spain',
        'people': 4200000,
        'population': 'bernabeu',
        },
    }

for city, user_info in cities.items():
    print(f'\nThis cities: {city.title()}')
    country = f"{user_info['country']}"
    people = f"{user_info['people']}"
    population = user_info['population']
    print(f"\tFull country: {country.title()}")
    print(f'\tFull people: {people.title()}')
    print(f'\tFull population: {population.title()}')
