fa,ba,ma = map(int,input().split())
fr,br,mr = map(int,input().split())

frango=fr-fa
bife=br-ba
massa=mr-ma
if fr>fa and br>ba and mr>ma:
    print(frango+bife+massa)
elif fr>fa and br>ba and mr<ma:
        print(frango+bife)
elif fr>fa and br<ba and mr<ma:
        print(frango)
elif fr>fa and br<ba and mr>ma:
        print(frango+massa)
elif fr<fa and br>ba and mr>ma:
        print(bife+massa)
elif fr<fa and br<ba and mr>ma:
        print(massa)
elif fr<fa and br>ba and mr<ma:
        print(bife)
else:
    print("0")

