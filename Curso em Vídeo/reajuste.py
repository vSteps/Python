s = float(input("Qual é o salário do funcionário? R$"))

cálculo = (s * 15/100)
aumento = s+cálculo


print("Um funcionário que antes ganhava R${}, com 15% de aumento, passa a receber R${:.2f}".format(s, aumento))
