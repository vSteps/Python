c = int(input())
a = int(input())
 
alunos=c-1
viagens= a//(alunos)
resto = a%alunos
if resto>0:
    viagens1=viagens+1
    print(viagens1)
else:
    print(viagens)
 
 
