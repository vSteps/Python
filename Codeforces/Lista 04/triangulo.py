A,B,C,D = map(int,input().split(" "))


if A<(B+C) or B<(C+A) or C<(B+A) or A<(B+D) or A<(C+D) or B<(A+D) or B<(C+D) or C<(A+D) or C<(B+D) or D<(A+B) or D<(B+C) or D<(A+C):
    print("S")
else:
    print("N")
    
