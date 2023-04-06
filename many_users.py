# Словарь в словаре

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
print()

# Словарь

name_1 = {'oksana': 28}
name_2 = {'dima': 35}
name_3 = {'diana': 19}

people = [name_1, name_2, name_3]
for peop in people:
    print(peop)

print()
print()

cities = {
    'kiev': {
        'country': 'ukraine',
        'population': 52000000,
        'fact': 'mother country',
        },

    'madrid': {
        'country': 'spain',
        'population': 47420000,
        'fact': 'prado museum',
        },

    'new-york': {
        'country': 'usa',
        'population': 331000000,
        'fact': 'statue of liberty'
        }
    }

for city, country_info in cities.items():
    print(f"\nCity name: {city.title()}")
    full_country = f"{country_info['country']}"
    population = f"{country_info['population']}"
    fact = country_info['fact']
    print(f"\tFull country: {full_country.title()}")
    print(f"\tFull population: {population.title()}")
    print(f"\tFull fact: {fact.title()}")