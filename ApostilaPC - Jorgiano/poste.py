d = int(input())
dp = int(input())

dm = d*1000
p = int(dm/dp) 
m = dm%dp
t = p+2

print(" {} poste(s)\n {} metro(s)".format(t, m))

