from Aula9_metodo import soma
from Aula9_metodo import subt
from Aula9_metodo import multi
from Aula9_metodo import divInteira
from Aula9_metodo import divFracionada
from Aula9_metodo import resto
from Aula9_metodo import raiz

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('\nA soma é: ',soma(n1,n2))
print('A subtraçãoé: ',subt(n1,n2))
print('A multiplicação é: ',multi(n1,n2))
print('A divisão inteira é: ',divInteira(n1,n2))
print('A divisão fracionada é: ',divFracionada(n1,n2))
print('A resto é: ',resto(n1,n2))
print('A raiz dos número é: ',raiz(n1,n2))
