numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print (f'Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}')

if numero1 > numero2:
    print('O maior número digitado é o primeiro: ', numero1)

elif numero1 == numero2:
    print('Os números são iguais: ', numero1)

else:
    print('O maior número digitado é o segundo: ', numero2)