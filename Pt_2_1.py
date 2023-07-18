import random
def findout(answer):
    print("Попробуй угадать цвет который я загадал: ")
    ans = str(input())
    if ans == answer:
        print("Отлично!")
    else:
        print("Подсказка:")
        if answer == "Зеленый":
            print("Цвет начинается на букву З")
            findout(answer)
        if answer == "Желтый":
            print("Цвет начинается на букву Ж")
            findout(answer)
        if answer == "Красный":
            print("Цвет начинается на букву К")
            findout(answer)
        if answer == "Синий":
            print("Цвет начинается на букву С")
            findout(answer)
        if answer == "Розовый":
            print("Цвет начинается на букву Р")
            findout(answer)

a = random.randint(1, 5)
print(a)
if a == 1:
    answer = "Зеленый"
if a == 2:
    answer = "Желтый"
if a == 3:
    answer = "Красный"
if a == 4:
    answer = "Синий"
if a == 5:
    answer = "Розовый"
findout(answer)
