d = int(input())
v = int(input())
 
horas = int(d//v)
m1 = d%v
m2 = m1/v
minutos = int((m2*60))
 
print("{:02d}:{:02d}".format(horas,minutos))