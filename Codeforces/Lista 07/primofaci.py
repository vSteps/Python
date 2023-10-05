n = int(input())
qtd=0
if n == 1:
    print("Nao")
    exit()
if n == 2:
    print("Sim")
    exit()
for i in range(2, n):
    if n % i == 0:
        qtd+=1
if qtd==0:
    print("Sim")
else:
    print("Nao")
