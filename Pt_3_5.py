unt = int(100) 
sim_num=[]
for number in range(1, unt + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            sim_num.append(number)
print("Простые числа")
print(sim_num)

print("Не простые числа")
not_sim_num=[x for x in range(unt) if x not in sim_num]
print(not_sim_num)
