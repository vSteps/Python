a,b= map(int,input().split(" "))

if a==1:
    a=4
elif a==2:
    a=4.5
elif a==3:
    a=5
elif a==4:
    a=2
elif a==5:
    a=1.5
conta = a*b

print("Total: R$ {:.2f}".format(conta))

