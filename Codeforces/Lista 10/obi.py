qtd = 0
n,p = map(int,input().split())
for i in range(n):
    x,y = map(int,input().split())
    if (x+y)>=p:
        qtd+=1
print(qtd)