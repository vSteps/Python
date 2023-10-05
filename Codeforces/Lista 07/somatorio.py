n = int(input())
soma = 0
for i in range(1, n+1):
    soma = soma+1/i
print("{:.4f}".format(soma))