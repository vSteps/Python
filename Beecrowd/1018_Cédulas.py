C = int(input())

print(C)

#100
C100 = C//100
C = C%100

#50
C50 = C//50
C = C%50

#20
C20 = C//20
C = C%20

#10
C10 = C//10
C = C%10

#5
C5 = C//5
C = C%5

#2
C2 = C//2
C = C%2

#1
C1 = C//1
C = C%1

print("{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(C100, C50, C20, C10, C5, C2, C1))
