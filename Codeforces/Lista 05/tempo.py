a,b,c = map(int,input().split())

if a==c or a==b or b==c:
    print("S")
elif a+c==b or a+b==c or c+b==a:
    print("S")
else:
    print("N")
