def da():
    a = int(input("Введите число от 10 до 20: "))
    if a >= 10:
        if a <= 20:
            print("Спасибо")
            return 0
        else:
            print("Число больше требуемого")
            return da()
    else:
        print("Число меньше требуемого")
        return da()


da()
