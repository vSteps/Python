def controlar_estoque(estoque, pedidos):
    vendas = 0
    for pedido in pedidos:
        tamanho = pedido - 1 
        if estoque[tamanho] > 0:
            estoque[tamanho] -= 1
            vendas += 1
    return vendas
estoque = []
pedidos = []
n = int(input())
for i in range (n):
    N = int(input())
    estoque.append(N)
p = int(input())
for i in range (p):
    P = int(input())
    pedidos.append(P)
total = controlar_estoque(estoque, pedidos)
print(total)
