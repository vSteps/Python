n = int(input())
saldo = 100
maior = saldo
for i in range(n):
    c = int(input())
    valor = c + saldo
    saldo = valor
    if saldo > maior:
        maior = saldo
print(maior)

