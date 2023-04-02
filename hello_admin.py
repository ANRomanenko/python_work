people_lists = ['dimon', 'maks', 'andrey', 'admin', 'kolia']
if people_lists:
    for people_list in people_lists:
        if people_list == 'admin':
            print("admin, would you like to see a status report?")
        else:
            print(f"{people_list.title()}, thank you for logging in again")
else:
    print("We need to ind some users!")
print()

# Проверка имен пользователей
current_users = ['Katia', 'Lena', 'IRA', 'Ania', 'Marina']
current_users = ['katia', 'lena', 'ira', 'ania', 'marina']

new_users = ['Sveta', 'Tania', 'Katia', 'ksusha', 'Ira']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'Имя {new_user}, уже использовалось, выберете новое имя!')
    else:
        print(f'Это имя, {new_user} доступно')
print()

number = ['1st']