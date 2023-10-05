lista = sorted([int(input()),int(input()),int(input())])

if lista[0]+lista[1]<=lista[2]:
    print("Nenhum")

elif lista[0]!=lista[1] and lista[0]!=lista[2] and lista[1]!=lista[2]:
    print("escaleno")
elif lista[0]==lista[1] and lista[0]==lista[2] and lista[1]==lista[2]:
    print("equilatero")
elif lista[0]==lista[1] or lista[1]==lista[2] or lista[0]==lista[2]:
    print("isosceles")
