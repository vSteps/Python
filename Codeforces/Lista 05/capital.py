a,b,c,d = map(int,input().split())

if a*d==b*c or a*c==d*b or a*b==c*d:
    print("S")
else:
    print("N")