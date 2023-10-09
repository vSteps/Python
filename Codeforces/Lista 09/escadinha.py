N = int(input())
sequencia = list(map(int, input().split()))
 
if N <= 2:
    print(1)
else:
    contador = 1
    diferenca = sequencia[1] - sequencia[0]
    escadinhas = 1
 
    for i in range(2, N):
        if sequencia[i] - sequencia[i-1] == diferenca:
            contador += 1
        else:
            diferenca = sequencia[i] - sequencia[i-1]
            contador = 2
            escadinhas += 1
 
    print(escadinhas)
