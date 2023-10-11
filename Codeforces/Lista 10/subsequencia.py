def is_subsequencia(sa, sb):
    i, j = 0, 0
    while i < len(sa) and j < len(sb):
        if sa[i] == sb[j]:
            j += 1
        i += 1
 
    return j == len(sb)
 
 
A, B = map(int, input().split())
SA = list(map(int, input().split()))
SB = list(map(int, input().split()))
 
 
if is_subsequencia(SA, SB):
    print('S')
else:
    print('N')
