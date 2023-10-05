def media_ponderada(v1, p1, v2, p2):
    soma_pesos = p1 + p2
    produto1 = v1 * p1
    produto2 = v2 * p2
    soma_produtos = produto1 + produto2
    media_ponderada = soma_produtos / soma_pesos
    return media_ponderada
