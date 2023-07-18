a = int(input("Число а: "))
b = int(input("Число b: "))
c = int(input("Число c: "))

if (a > b) & (a > c):
    if b > c:
        print("a - самое большое число")
        print(a, b, c)
    else:
        print("a - самое большое число")
        print(a, c, b)
if (c > b) & (c > a):
    if b > a:
        print("c - самое большое число")
        print(c, b, a)
    else:
        print("c - самое большое число")
        print(c, a, b)
if (b > c) & (b > a):
    if c > a:
        print("a - самое большое число")
        print(b, c, a)
    else:
        print("a - самое большое число")
        print(b, a, c)
