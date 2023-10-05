Lista = []
m = int(input())
b = int(input())
a = int(input())
Lista.append(b)
Lista.append(a)

idade_terceiro = m-(b+a)
Lista.append(idade_terceiro)

print(max(Lista))
