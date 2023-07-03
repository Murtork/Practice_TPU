a=int(input())
a=str(a)
mas=[]
for i in a:
    mas.append(i)
print(mas)
print(mas.index(max(mas)))
mas.reverse()
print(mas.index(max(mas)))
