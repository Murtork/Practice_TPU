need_to_ride=float(input("Сколько надо проехать?"))
t_to_km=float(input("Сколько литров тратится на 100 км?"))
toplivo=float(input("Сколько литров в баке?"))
moj=toplivo/t_to_km*100
if need_to_ride>moj:
    print("Доехать не получится, надо заправиться")
if need_to_ride>moj:
    print("Доехать получится! Вперед!")
