x = int(input())
picos = 0
while x != 0:
    mag = list(map(int, input().split()))
    mag.append(mag[0])
    mag.append(mag[1])
    for i in range(1, len(mag)-1):
        if mag[i] < mag[i-1] and mag[i] < mag[i+1]:
            picos +=1
        elif  mag[i] > mag[i-1] and mag[i] > mag[i+1]:
            picos +=1
    print(picos)
    picos = 0
    x = int(input())
