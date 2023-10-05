from tkinter import S
from typing import SupportsRound


C = int(input())
D = int(input())
T = int(input())

d = (D/C)
m = T*C

if T==0:
    print(f"{d:.1f}")

if T!=0:
    v=D-m
    if m>D:
        print(0.0)
        quit()
    s = v/C
    print(round(s,1))

    
