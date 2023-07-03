def da():
    a=int(input("Введите число"))
    if (a>=10):
        if (a<=20):
            print("Спасибо")
            return 0
        else:
            print("Число больше требуемого")
    else:
        print("Число меньше требуемого")
        return da()
da()
