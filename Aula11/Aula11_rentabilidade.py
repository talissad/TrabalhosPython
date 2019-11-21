from metodo import rentabilidade

valor = float(input('Digite seu salário: '))
taxa = int(input('Digite a porcentagem a ser calculada: '))

print('\nCom um valor de {} e uma taxa de {}%'.format(valor, taxa))
print(f'No 12º mês você terá em juros um valor de: R${rentabilidade(valor, taxa)-valor:.2f} \nTotalizando R$ {rentabilidade(valor, taxa):.2f}\n')
