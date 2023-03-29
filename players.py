players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:]) # Аналогичный синтаксис работает и для сегментов, включающих конец списка. Например, если вам нужны все элементы с третьего до последнего, начните с индекса 2 и не указывайте второй индекс:
print(players[-3:])
print()
# Перебор содержимого сегмента


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())