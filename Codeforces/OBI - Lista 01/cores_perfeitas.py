R, G, B = sorted(map(int, input().split(" ")))
 
if 2 * G == R + B:
    print("S")
else:
    print("N")
    
