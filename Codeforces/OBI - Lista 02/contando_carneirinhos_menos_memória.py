t = int(input())
for i in range(t):
    n = int(input())
    carneiros = list(map(int,input().split()))
    s = set(carneiros)
    print(len(s)) 
       
