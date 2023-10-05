s = int(input())

horas = s//3600
minutos = (s%3600)//60
segundos = s%60

print("{}:{}:{}".format(horas, minutos, segundos))

