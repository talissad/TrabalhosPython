#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)


numero = int(input('Digite um número: '))

for i in range (0,11):
    print(f'{numero} x {i} = {numero*i}')