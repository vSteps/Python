a,b = map(int,input().split())
for i in range (a,b+1):
    if i%a==0:
        print(i, end=" ")