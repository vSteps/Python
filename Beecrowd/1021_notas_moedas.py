v,c= map(int, input().split("."))
c = c+v*100

print("NOTAS:")
print(f'{c//10000} nota(s) de R$ 100.00')
c = c%10000
print(f'{c//5000} nota(s) de R$ 50.00')
c = c%5000
print(f'{c//2000} nota(s) de R$ 20.00')
c = c%2000
print(f'{c//1000} nota(s) de R$ 10.00')
c = c%1000
print(f'{c//500} nota(s) de R$ 5.00')
c = c%500
print(f'{c//200} nota(s) de R$ 2.00')
c = c%200
print("MOEDAS:")
print(f'{c//100} moeda(s) de R$ 1.00')
c = c%100
print(f'{c//50} moeda(s) de R$ 0.50')
c = c%50
print(f'{c//25} moeda(s) de R$ 0.25')
c = c%25
print(f'{c//10} moeda(s) de R$ 0.10')
c = c%10
print(f'{c//5} moeda(s) de R$ 0.05')
c = c%5
print(f'{c//1} moeda(s) de R$ 0.01')
c = c%1



