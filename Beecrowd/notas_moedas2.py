v,c= map(int, input().split("."))
c = c+v*100

n = [100, 50, 20, 10, 5, 2]
print("NOTAS:")
for nota in n:
    valor = c//(nota*100)
    print("{} nota(s) de R$ {}.00".format(valor,nota))
    c = c%(nota*100)

m = [100, 50, 25, 10, 5,1]

print("MOEDAS:")
for moeda in m:
    valor = c//moeda
    m = moeda//100
    m2 = moeda%100
    print("{} moeda(s) de R$ {}.{:.02}".format(valor, m, m2))
    c = c%moeda
    
