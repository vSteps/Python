A,B,C = input().split(" ") 

A = int(A)
B = int(B)
C = int(C)

MaiorAB = (A + B+abs(A-B))//2
MaiorAC = (A + C+abs(A-C))//2
MaiorBC = (B + C+abs(B-C))//2

if MaiorAB==A:
  print("{} eh o maior".format(MaiorAC))
else:
  print("{} eh o maior".format(MaiorBC))
