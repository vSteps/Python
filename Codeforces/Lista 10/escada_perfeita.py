def escada_perfeita():
    n = int(input())
    sequencia = list(map(int, input().split()))
    soma = sum(sequencia)
 
    soma -= (n * n + n) // 2
 
    if soma >= 0 and soma % n == 0:
        movimentos = 0
        altura = soma // n + 1
 
        for i in range(n):
            if sequencia[i] > altura:
                movimentos += (sequencia[i] - altura)
            altura += 1
 
        print(movimentos)
    else:
        print(-1)
 
escada_perfeita()
