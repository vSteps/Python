def dia(dia, mes, ano):
    meses = {
        1: 'janeiro', 2: 'fevereiro', 3: 'marco', 4: 'abril', 5: 'maio', 6: 'junho',
        7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'
    }
    if dia<1 or dia>31 or mes<1 or mes>12 or ano < -10000 or ano > 10000:
        return "Data Invalida"
    if mes==2 and dia>28:
        return "Data Invalida"
    if dia==31 and mes==4 or mes==6 or mes==9 or mes==11:
        return "Data Invalida"
    dia_extenso= f"{dia:02d} de {meses[mes]} de {ano}"

