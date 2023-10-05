d,m,a = map(int,input().split(" "))

lista_31 = ["01", "03", "05", "07", "08", "10", "12"]
lista_30 = ["04", "06", "11"]
lista_28 = ["02"]

if d=="31":
    if m==lista_28 or m==lista_30:
        print("invalida")
elif d=="30":
    if m==lista_28 or m==lista_31:
        print("invalida")
elif d=="28":
    if m==lista_31 or m==lista_30:
        print("invalida")
        