a = int(input())
b = []
for i in str(a):
    b.append(i)
# print(b)
for i in range(len(b) - 1):
    for j in range(len(b) - i - 1):
        if int(b[j]) < int(b[j + 1]):
            b[j], b[j + 1] = b[j + 1], b[j]
# print(b)
c = ""
for i in range(len(b)):
    c = c + str(b[i])
print(c)
