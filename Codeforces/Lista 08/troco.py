
def maior_troco(preco_marcas, din):
    for i in range(len(preco_marcas)):
        if preco_marcas[i] > din:
            preco_marcas[i] = 0
        else:
            preco_marcas[i] = din % preco_marcas[i]
    return max(preco_marcas)
 
x = int(input())
for i in range(x):
    din, qnt_marc = map(int, input().split())
    marcas = list(map(float, input().split()))
    print(f"{maior_troco(marcas, din):.2f}")
