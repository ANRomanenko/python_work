# Словарь с однотипными объектами

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print()


# Опрос
favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phill': 'python'}
polls = ['jen', 'sarah', 'edward', 'phill', 'nik', 'david', 'valera']

for name in polls:
    if name in favorite_languages: #проверка, прошёл ли чел из polls опрос
        print(f"{name.title()} thanks for tacking the poll!") #если прошёл - благодарит
    else:
        print(f"{name.title()}, please take the poll!") #если не прошёл - просит пройти
print()

lan_yap = {'jen': 'c', 'dron': 'python', 'nika': 'ruby', 'lena': 'python'}
name_polls = ['edvard', 'dron', 'roma', 'jen', 'lena', 'nika', 'maks', 'lena']
for name in name_polls:
    if name in lan_yap:
        print(f'{name.title()}, благодарим вас за участие в опросе!')
    else:
        print(f"{name.title()}, предлагаем вам принять участие в опросе!")
print()

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }


for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite language is: ")
        for language in languages:
            print(f"\t{language.title()}")