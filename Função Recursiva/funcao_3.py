def f(x,y):
    if (x>=y):
        return (x+y)/2
    else:
        return f(f(x+2,y-1),f(x+1,y-2))
n1 = int(input())
n2 = int(input())
retorno = f(n1,n2)
print(retorno)