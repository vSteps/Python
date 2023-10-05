n = int(input())
acima = 0
abaixo = 0
lista = list(map(int,input().split()))
media = sum(lista)/len(lista)
for e in lista:
    if e>=media:
        acima = acima+1
    else:
        abaixo = abaixo+1
print("{:.1f}".format(media))
print(abaixo)
print(acima)

