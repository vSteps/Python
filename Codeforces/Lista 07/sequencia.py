n = int(input())
cont = []
qtd=1
for i in range(n):
    num = int(input())
    cont.append(num)
for x in range(n):
    try:
        if cont[x]!=cont[x+1]:
            qtd+=1
    except:
        break
print(qtd)
    
