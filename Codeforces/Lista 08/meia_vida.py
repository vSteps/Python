s,m = map(int,input().split())
qtd=0
while m>=0.5:
    qtd+=s
    m = m/2
segundos = (qtd)%60
minutos = (qtd//60)%60
horas = (qtd//3600)%24
dias = (qtd//86400)
print("{:01d} dias {:02d}:{:02d}:{:02d}".format(dias,horas,minutos,segundos))