a,b,c,d = map(int,input().split())
hora_final = (c-a)
minuto_final = (d-b)
if hora_final==0 and minuto_final==0:
    hora_final=24
    minuto_final=0
if minuto_final<0:
    hora_final -= 1
    minuto_final+= 60
if hora_final<0:
    hora_final+= 24

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora_final, minuto_final))
