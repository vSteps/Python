n = int(input())


valor = 7
if n>=0 and n<=10:
    print("7")
elif n>=11 and n<=30:
    valor1=(valor+(n-10))*1
    print(valor1)
elif n>=31 and n<=100:
    valor2=(valor+20)+(n-30)*2
    print(valor2)
elif n>=101:
    valor3=(valor+20+140)+(n-100)*5
    print(valor3)
