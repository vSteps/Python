def saltador_alegre(n, sequencia):
    diferencas = set()
 
    for i in range(1, n):
        diff = abs(sequencia[i] - sequencia[i - 1])
        if diff < 1 or diff >= n or diff in diferencas:
            return False
        diferencas.add(diff)
 
    return True
 
while True:
    try:
        linha = input()
        if linha == "":
            break
 
        n, *sequencia = map(int, linha.split())
 
        if saltador_alegre(n, sequencia):
            print('Alegre')
        else:
            print('Nao alegre')
    except EOFError:
        break
