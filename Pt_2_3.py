a=int(input("Введите число: "))
sum = 0
temp = a
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if a == sum:
    print("Число является числом Армстронга")
else:
    print("Число НЕ является числом армстронга")
