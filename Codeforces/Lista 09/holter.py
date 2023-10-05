n = int(input())
batimentos = []
qtd = 0
for b in range(n):
    b = int(input())
    batimentos.append(b)
media = sum(batimentos)//n
for i in batimentos:
    if i < int(media*0.9) or i > int(media*1.1):
        qtd+=1
print(media)
print(qtd)
