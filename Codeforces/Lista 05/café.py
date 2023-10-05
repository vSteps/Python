a1 = int(input())
a2 = int(input())
a3 = int(input())

andar1 = a1*0 + a2*2 + a3*4
andar2 = a1*2 + a2*0 + a3*2
andar3 = a1*4 + a2*2 + a3*0

if a2>=a3 and a2>=a1:
    print(andar2)
elif a3>=a1 and a3>=(a1+a2):
    print(andar3)
elif a1>=a3 and a1>=(a2+a3):
    print(andar1)
else:
    print(andar2)
