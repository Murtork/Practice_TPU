a=int(input())
a=str(a)
mas=[]
for i in a:
    mas.append(i)
mas.reverse()
print(mas.index(max(mas)))
