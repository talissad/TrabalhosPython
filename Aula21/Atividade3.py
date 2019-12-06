# 1 - Crie um metodo que leia 5 valores inteiros e retorne uma lista.
# Esta função deve ter tratamento de excessão evitando erro ValueError.

# 2 - Com a lista retornada, faça a multiplicação por 5 e salve o resultado
# em outra lista.

# Imprima a lista resultante

lista_numero = []
resultado_multiplicacao = []
n = 1

try:
    for i in range(5):
        a = int(input(f'Digite o {n} número: '))
        lista_numero.append(a)
        n += 1

    for j in lista_numero:
        multiplicacao = j * 5
        resultado_multiplicacao.append(multiplicacao)

    #print(f'O resultado da multiplicação é: {resultado_multiplicacao}')
    print(f'5 * {lista_numero[0]} = {resultado_multiplicacao[0]}\n5 * {lista_numero[1]} = {resultado_multiplicacao[1]}\n'
            f'5 * {lista_numero[2]} = {resultado_multiplicacao[2]}\n5 * {lista_numero[3]} = {resultado_multiplicacao[3]}\n'
            f'5 * {lista_numero[4]} = {resultado_multiplicacao[4]}')



except ValueError:
    print('Digite somente números inteiros!')