import random
win = defeat = 0
health=3
while True:
    print()
    user = input("Орел - 0 или Решка - 1 \n")
    print()
    if user not in ("01"):
        print("Конец игры")
        break
    pc=random.choice("01")
    if pc==user:
        win+=1
    else:
        defeat+=1
        health-=1
    print(f'Побед: {win}\nПоражений: {defeat}\nБаланс: {balance}')
    if balance <=0:
        print("Кончились жизни")
        break
