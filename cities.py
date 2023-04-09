# Команда break и выход из цикла

promt = "\nPlease enter the name of a city you have visited:"
promt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(promt)

    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Команда continue и продолжение цикла

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)