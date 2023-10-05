A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C) 

D = B + A
P = A + B + C
aT = ((A+B)*C)/2


if A<(B+C) and B<(C+A) and C<(B+A):
    print("Perimetro = {:.1f}".format(P))
else:
    print("Area = {:.1f}".format(aT))
