nome = input()
salario = float(input())
vendas = float(input())
 
comissao = 15/100*vendas
 
salario_final = salario+comissao
 
print("{}\nR$ {:.2f}".format(nome,salario_final))