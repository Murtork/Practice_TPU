alfavit_h =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_l =  'adcdefghijklmnopqrstuvwxyzadcdefghijklmnopqrstuvwxyz'
smeshenie = int(13)
message = input("Сообщение для шифровки: ")
itog = ''
for i in message:
    if i.isupper():
        mesto = alfavit_h.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_h:
            itog += alfavit_h[new_mesto]
        else:
            itog += i
    else:
        mesto = alfavit_l.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_l:
            itog += alfavit_l[new_mesto]
        else:
            itog += i
print(itog)