n = int(input())
acima = 0
abaixo = 0
lista = list(map(int,input().split()))
media = sum(lista)/len(lista)
Lbaixo = []
Lcima = []
for e in lista:
    if e>=media:
        acima = acima+1
        Lcima.append(e)
    else:
        abaixo = abaixo+1
        Lbaixo.append(e)
print("{:.1f}".format(media))
print(abaixo, *Lbaixo)
print(acima, *Lcima)

