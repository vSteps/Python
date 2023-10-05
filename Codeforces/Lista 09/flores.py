while True:
    n = input()
    if n == "*":
        break
    palavras = n.lower.split()
    primeiras_letras = [palavra[0] for palavra in palavras] 
    for i in range(len(primeiras_letras)-1):
            if primeiras_letras[i] != primeiras_letras[i+1]:
                print("N")
            else:
                print("Y")
   