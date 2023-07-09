a=int(input())
for i in range(100000):
    if i*i>a:
        print("Квадрат этого числа больше заданного:",i)
        break
