number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number.strip())

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
print()


# Упражнение 7.1 (Прокат машин)-----(Изучаем Python (Мэтиз))
car = input("Какую машину бы вы хотели взять на прокат? ")
print(f"\nLet me see if I can find you a {car.title()}!")
print()

# Упражнение 7.2 (Заказ стола)-----(Изучаем Python (Мэтиз))
name_user= input("Как вас зовут? ")
user_restoran = input("На сколько мест вы хотите заборонировать стол в нашем ресторане? ")
user_restoran = int(user_restoran)
if user_restoran >= 8:
    print(f"\nИзвините, {name_user.title()} но вам придётся немножко подождать!")
else:
    print(f"\n{name_user.title()}, Ваш стол готов для посищения, добро пожаловать в наш рестора Tolstiy & Tonkiy!")
print()

# Упражнение 7.3 (Числа, кратные 10)-----(Изучаем Python (Мэтиз))
num = input("Введите число: ")
num = int(num)

if num % 10 == 0:
    print('Число кратно 10')
else:
    print('Число не кратно 10')
