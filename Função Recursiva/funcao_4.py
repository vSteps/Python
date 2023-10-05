def algarismos(n):
        if (n==0):
            return 0
        else:
            return 1 + algarismos(n//10)
n = int(input())
print(algarismos(n))