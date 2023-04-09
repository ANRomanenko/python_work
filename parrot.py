# Как работает функция input()

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Пользователь решает прервать работу программы

# promt = "\nTell me something, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(promt)
#
#     if message != 'quit':
#         print(message)
# Флаги

promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(promt)

    if message == 'quit':
        active = False
    else:
        print(message)