l,d = map(int,input().split(" "))
k,p = map(int,input().split(" "))
 
c1 = l//d
cp = c1*p
cg = k*l
ct = int(cg+cp)
 
print(ct)