a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
print(d)
if d<0:
    print("Корней нет")
elif d==0:
    x1=(-b)/2*a
    print("Корень равен:",x1)
else:
    x1=(-b+d**(1/2))/(2*a)
    x2=(-b-d**(1/2))/(2*a)
    print("Корни равны:", x1,x2)
