def lista_troca_menor_primeiro(lista):
    if lista[0]==min(lista):
        return 0
    else:
        menor = list.index(min(lista))
        primeiro = lista[0]

        primeiro, menor = menor, primeiro
        return 1
        
    