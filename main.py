import random

"""Генератор паролей"""

list1 = []
count_passwords = int(input("Сколько паролей будем создавать?:: "))
length = int(input("Длина пароля?:: "))
while True:
    if input("Включать ли цифры?:: ").lower() == "да":
        list1.append([chr(i) for i in range(48, 58)])  # Генератор символов ASCII
    if input("Включать ли заглавные буквы?:: ").lower() == "да":
        list1.append([chr(i) for i in range(65, 91)])  # Генератор символов ASCII
    if input("Включать ли строчные буквы?:: ").lower() == "да":
        list1.append([chr(i) for i in range(97, 123)])  # Генератор символов ASCII
    if input("Включать ли символы?:: ").lower() == "да":
        list1.append([i for i in "!#$%&*+-=?@^_ "])
    if len(list1) == 0:
        print("Ответить нужно: 'да', хотябы один вопрос.")
        continue
    else:
        for i in range(count_passwords):
            for j in range(length):
                print(random.choice(random.choice(list1)), end="")
            print()
        break
