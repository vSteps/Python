lista = []
a = int(input())
b = int(input())
c = int(input())
d = int(input())

time1 = a+b
time_1 = c+d
dif_time1 = abs(time1-time_1)
lista.append(dif_time1)

time2 = a+c
time_2 = b+d
dif_time2 = abs(time2-time_2)
lista.append(dif_time2)

time3 = a+d
time_3 = b+c
dif_time3 = abs(time3-time_3)
lista.append(dif_time3)

print(min(lista))