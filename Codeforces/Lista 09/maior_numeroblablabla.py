def contador_algarismos(numero):    
    while numero >= 10:
        soma = 0
        while numero > 0:
            soma += numero % 10
            numero //= 10
        numero = soma
    return numero

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if contador_algarismos(n) > contador_algarismos(m):
        print(1)
    elif contador_algarismos(m) > contador_algarismos(n):
        print(2)
    else:
        print(0)