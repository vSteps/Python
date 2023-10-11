N = int(input())
 
fita = [int(x) for x in input().split()]
fita[N:] = [-1]
fita[:0] = [-1] 
 
for c in range(8):
    for i in range(1, N+1):
        if (fita[i] == -1):
            if (fita[i-1] == c or fita[i+1] == c):
                fita[i] = c + 1
 
for i in range(1, N+1):
    if (fita[i] == -1):
        fita[i] = 9
 
for i in range(1, N):
    print(fita[i], end=' ')
print(fita[N])


