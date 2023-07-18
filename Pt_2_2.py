a = [0] * 5
a[0] = "Зимородок"
a[1] = "Хороший доктор"
a[2] = "Ведьмак"
a[3] = "Уэнсдей"

b = [0] * 5
b[0] = "Зимородок"
b[1] = "Хороший доктор"
b[2] = "Ведьмак"
b[3] = "Уэнсдей"

for i in range(5):
    print(a[i])
print()

nomer = int(input("Введите номер вашей передачи: "))
nomer = nomer - 1
nazv = str(input("Название передачи: "))

for i in range(4):
    if i >= nomer:
        a[i + 1] = b[i]
a[nomer] = nazv
print()
for i in range(5):
    print(a[i])
