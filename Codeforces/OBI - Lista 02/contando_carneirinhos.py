t = int(input())
for i in range(t):
    n = int(input())
    carneiros = list(map(int,input().split()))
    s = []
    for c in carneiros:
        if not c in s:
            s.append(c)
    print(len(s))
 
       
    
