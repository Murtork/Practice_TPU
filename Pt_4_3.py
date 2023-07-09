def isSimple(a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

low=int(input("Нижняя граница диапозона: "))
up=int(input("Верхняя граница диапазона: "))
for numb in range(low,up + 1):
    if isSimple(numb):
        print(numb)
