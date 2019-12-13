#Learn more or give us feedback
# Faça um programa que lê um numero inteiro do teclado e mostre a soma do numero com os valores da
# seguinte tupla: 
# (61, 138, 13, 86, 7, 160, 150, 90, 182, 158, 167, 171, 79, 162, 197, 63, 164, 22, 194, 17, 168)
# use o f-string para apresentar o numero.

numero = int(input('Digite um número: '))
numeros_somar = (61, 138, 13, 86, 7, 160, 150, 90, 182, 158, 167, 171, 79, 162, 197, 63, 164, 22, 194, 17, 168)

for i in numeros_somar:
    print(f'{numero} + {i} = {i + numero}')
