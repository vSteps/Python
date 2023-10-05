from multiprocessing import allow_connection_pickling


A,G,Ra,Rg = map(float,input().split(" "))

gasolina = G*0.7

if A==G:
    print("G")
    quit()
if A<gasolina:
    print("A")
else:
    print("G")
    
