p,p1,p2 = input().split(" ")
P,P1,P2 = input().split(" ")

p = int(p)
p1 = int(p1)
p2 = float(p2)

P = int(P)
P1 = int(P1)
P2 = float(P2)

v1 = p2 * p1
v2 = P2 * P1
V = v1 + v2

print("VALOR A PAGAR: R$ {:.2f}".format(V))
