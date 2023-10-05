n = int(input())
i = list(map(int, input(). split()))
I1 = 0
I2 = 0
for a in range(n):
    if i[a] == 1 and I1 == 0:
        I1 = 1
    elif i[a] == 1 and I1 == 1:
        I1 = 0
    if i[a] == 2 and I1 == 0 and I2 == 0:
        I1 = 1
        I2 = 1
    elif i[a] == 2 and I1 == 0 and I2 == 1:
        I1 = 1
        I2 = 0
    elif i[a] == 2 and I1 == 1 and I2 == 0:
        I1 = 0
        I2 = 1
    elif i[a] == 2 and I1 == 1 and I2 == 1:
        I1 = 0
        I2 = 0
print(I1)
print(I2)