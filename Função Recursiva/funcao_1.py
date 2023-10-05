def conta_divisores_rec(n,div):
    if (div==1):
        return 1
    qtd=0
    if (n%div==0):
        qtd=qtd+1
    qtd = qtd+conta_divisores_rec(n,div-1)
    return qtd


def conta_divisores(n):
    return conta_divisores(n,n)






    

