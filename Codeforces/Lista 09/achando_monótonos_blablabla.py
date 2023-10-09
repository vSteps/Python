n = input()
sla = list(input().split("b"))
qtd = 0
for i in sla:
    if i != "":
        if len(i)>1:
            qtd+=len(i)
print(qtd)
