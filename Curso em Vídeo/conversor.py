a = float(input("Quanto dinheiro você tem na carteira? R$"))

#Este programa leva em conta a cotação atual do dólar 19/04/2023

dolar = a/5.08

print("Com R${}, você pode comprar US${:.2f}".format(a, dolar))


