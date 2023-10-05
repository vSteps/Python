venda = float(input())

sem_imposto = venda/(1+0.18+0.13+0.014+0.076)
ICMS = 18/100*sem_imposto
IPI = 13/100*sem_imposto
COFINS = 7.6/100*sem_imposto
PIS = 1.4/100*sem_imposto

print("ICMS: {:.2f}\nIPI: {:.2f}\nPIS: {:.2f}\nCofins: {:.2f}\nValor sem impostos: {:.2f}\n".format(ICMS,IPI,PIS,COFINS,sem_imposto))


