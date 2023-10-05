p = float(input("Qual é o preço do seu produto? R$"))

cálculo = (p * 5/100)
desconto = p-cálculo


print("O produto, que antes custava R${}, na promoção com desconto de 5%, vai custar R${:.2f}".format(p, desconto))
