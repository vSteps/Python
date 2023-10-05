S = float(input())

R1 = S * (15/100)
R2 = S * (12/100)
R3 = S * (10/100)
R4 = S * (7/100)
R5 = S * (4/100)

N1 = R1 + S
N2 = R2 + S
N3 = R3 + S
N4 = R4 + S
N5 = R5 + S

P1 = 15
P2 = 12
P3 = 10 
P4 = 7
P5 = 4

if S<=400.00:
  print("Novo salario: {:.2f}".format(N1))
  print("Reajuste ganho: {:.2f}".format(R1))
  print("Em percentual: {} %".format(P1))

elif S<=800.00:
  print("Novo salario: {:.2f}".format(N2))
  print("Reajuste ganho: {:.2f}".format(R2))
  print("Em percentual: {} %".format(P2))
elif S<=1200.00:
  print("Novo salario: {:.2f}".format(N3))
  print("Reajuste ganho: {:.2f}".format(R3))
  print("Em percentual: {} %".format(P3))
elif S<=2000.00:
  print("Novo salario: {:.2f}".format(N4))
  print("Reajuste ganho: {:.2f}".format(R4))
  print("Em percentual: {} %".format(P4))
else:
  print("Novo salario: {:.2f}".format(N5))
  print("Reajuste ganho: {:.2f}".format(R5))
  print("Em percentual: {} %".format(P5))
  
