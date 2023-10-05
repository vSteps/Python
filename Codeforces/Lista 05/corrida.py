n,d,v = map(int,input().split())
n1,d1,v1 = map(int,input().split())

V = v*0.277778
V1 = v1*0.277778

vencedor= d/V
vencedor1 = d1/V1

if vencedor1<vencedor:
    print(n1)
elif vencedor<vencedor1:
    print(n)
