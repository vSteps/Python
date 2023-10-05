def dia_da_semana(h, d):
    dias_semana = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    indice_hoje = dias_semana.index(h.capitalize())
    indice_evento = (indice_hoje + d) % 7
    return dias_semana[indice_evento]