n = int(input())
 
votos=[]
carlos=0
for i in range(n):
    v = int(input())
    votos.append(v)
    if i ==0:
        carlos=v
escolhido = True
for v in votos:
    if v>carlos:
        escolhido=False
        break
if escolhido:
    print("S")
else:
    print("N")
    
