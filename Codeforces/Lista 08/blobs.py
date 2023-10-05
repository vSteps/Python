n = int(input())
qtd=0
for i in range(n):
    t = float(input())
    while t>1:
        qtd+=1
        t = t/2
    print("{} dias".format(qtd))
    qtd=0        
