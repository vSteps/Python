p,n = map(int,input().split())
canos = list(map(int,input().split()))
qtd = 0
for i in range(1, n):
    if abs(canos[i-1]-canos[i])>p:
        qtd+=1
    
if qtd>0:
    print("GAME OVER")
else:
    print("YOU WIN")