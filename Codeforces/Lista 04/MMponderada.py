a,b = map(int,input().split(" "))
c,d = map(int,input().split(" "))
p1,p2 = map(int,input().split(" "))

media1 = (a*p1+b*p2)//(p1+p2)
media2 = (c*p1+d*p2)//(p1+p2)
media_final = (media1*p1+media1*p2)//(p1+p2)
media_final2 = (media2*p1+media2*p2)//(p1+p2)

if media1>=media2 and media1>=media_final2:
    print(1)
else:
    print(2)

print(media_final)
print(media_final2)
print(media1)
print(media2)
