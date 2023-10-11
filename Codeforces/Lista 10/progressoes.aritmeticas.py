def eh_progressao_aritmetica(subsequencia):
    if len(subsequencia) <= 2:
        return True
 
    diff = subsequencia[1] - subsequencia[0]
    for i in range(2, len(subsequencia)):
        if subsequencia[i] - subsequencia[i - 1] != diff:
            return False
 
    return True
 
def numero_minimo_partes_progressoes_aritmeticas(sequencia):
    numero_partes = 1
    subsequencia_atual = [sequencia[0]]
 
    for i in range(1, len(sequencia)):
        subsequencia_atual.append(sequencia[i])
 
        if not eh_progressao_aritmetica(subsequencia_atual):
            numero_partes += 1
            subsequencia_atual = [sequencia[i]]
 
    return numero_partes
 
N = int(input())
sequencia = list(map(int, input().split()))
 
min_partes = numero_minimo_partes_progressoes_aritmeticas(sequencia)
 
print(min_partes)
