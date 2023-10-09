message = input()
crib = input()
 
count = 0
 
for i in range(len(message) - len(crib) + 1):
    match = True
    for j in range(len(crib)):
        if message[i+j] == crib[j]:
            match = False
            break
    if match:
        count += 1
 
print(count)
