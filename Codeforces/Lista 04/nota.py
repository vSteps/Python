b = int(input())
t = int(input())

area_ret = 160*70
area_trap = (b+t)*70/2
area_trap2 = (160-t+160-b)*70/2

if area_trap>area_ret/2:
    print("1")
elif area_trap2>area_ret/2:
    print("2")
elif area_trap==area_ret/2 and area_trap2==area_ret/2:
    print("0")





