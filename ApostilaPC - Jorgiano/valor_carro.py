v = float(input())

sem_imposto = v/(1+18/100+13/100+1.4/100+7.6/100)


icms = sem_imposto*(18/100)
ipi = sem_imposto*(13/100)
pis = sem_imposto*(1.4/100)
cofins = sem_imposto*(7.6/100)

print("ICMS: {:.2f}\nIPI: {:.2f}\nPIS: {:.2f}\nCofins: {:.2f}\nValor sem impostos: {:.2f}".format(icms,ipi,pis,cofins,sem_imposto))



