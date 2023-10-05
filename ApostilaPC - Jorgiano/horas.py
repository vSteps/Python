minutos1 = int(input())
minutos2 = int(input())

h = (minutos2-minutos1)//60
m = (minutos2-minutos1)%60

print("{}:{}".format(h,m))

