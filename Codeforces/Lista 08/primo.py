def primo(n):
    if n==1 or n ==0:
        return False
    for i in range(2,n-1):
        if n%i == 0:
            return False
    return True

n = int(input())
numero = n+1
while not primo(numero):
    numero+=1
print(numero)