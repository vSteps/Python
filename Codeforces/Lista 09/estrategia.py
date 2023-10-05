'''def chunks(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]


J,R = map(int,input().split())
p = list(map(int,input().split()))

j1 = 1
j2 = 2
j3 = 3

rodadas = list(chunks(p, J))
if J==3:
    Lista1 = rodadas[0]
    Lista2 = rodadas[1]
    Lista3 = rodadas[2]
    jogador1 = Lista1[0]+Lista2[0]+Lista3[0]
    jogador2 = Lista1[1]+Lista2[1]+Lista3[1]
    jogador3 = Lista1[2]+Lista2[2]+Lista3[2]
    if jogador1>jogador2 and jogador1>jogador3:
        print (j1)
    elif jogador2>jogador1 and jogador2>jogador3:
        print (j2)
    elif jogador3>jogador2 and jogador3>jogador1:
        print (j3)
    else:
        print(j3)
elif J==2:
    Lista1 = rodadas[0]
    Lista2 = rodadas[1]
    jogador1 = Lista1[0]+Lista2[0]
    jogador2 = Lista1[1]+Lista2[1]
    if jogador1>jogador2:
        print (j1)
    elif jogador2>jogador1:
        print (j2)
    else:
        print(j2)
else:
    print(j1)'''

































J, R = map(int, input().split())
p = list(map(int, input().split()))

max_pontuacao = 0
vencedor = 0

for i in range(J):
    pontuacao = sum(p[i::J])
    if pontuacao >= max_pontuacao:
        max_pontuacao = pontuacao
        vencedor = i + 1

print(vencedor)