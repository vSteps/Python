teste = 1
 
while True:
    areas = int(input())
    if areas == 0:
        break
 
    print("Teste", teste)
 
    x1 = -1000000000
    y1 = 1000000000
    x2 = 1000000000
    y2 = -1000000000
 
    while areas > 0:
        a, b, c, d = map(int, input().split())
        if a > x1:
            x1 = a
        if b < y1:
            y1 = b
        if c < x2:
            x2 = c
        if d > y2:
            y2 = d
        areas -= 1
 
    if x2 < x1 or y1 < y2:
        print("nenhum")
    else:
        print(x1, y1, x2, y2)
    print()
 
    teste += 1
