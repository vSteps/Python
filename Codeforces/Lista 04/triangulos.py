a,b,c = sorted(map(int,input().split(" ")))


if c**2<a**2+b**2:
        print("a")
elif c>=a+b:
        print("n")
elif c**2>a**2+b**2:
        print("o")
else:
    print("r")
