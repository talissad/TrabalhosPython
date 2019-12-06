continuar = 'n'

while continuar != 's':
    
    try:
        a = int(input('\nDigite um número: '))
        b = int(input('Digite outro número: '))

        print(f'\n{a} + {b} = {a+b}'
            f'\n{a} / {b} = {a/b}'
            f'\n{a} * {b} = {a*b}'
            f'\n{a} - {b} = {a+b}\n')

        continuar = input("Digite 'S' para finalizar ou 'N' para continuar: ")

    except ValueError:
        print('Digite um número inteiro! Digite novamente')

    except ZeroDivisionError:
        print('Digite um número diferente de zero! Digite novamente')
    