N = int(input())
K = int(input())
pontuacoes = []
 
for _ in range(N):
    pontuacao = int(input())
    pontuacoes.append(pontuacao)
 
pontuacoes.sort(reverse=True)
 
classificados = K
 
while classificados < N and pontuacoes[classificados] == pontuacoes[K-1]:
    classificados += 1
 
print(classificados)
