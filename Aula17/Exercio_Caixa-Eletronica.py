# Faça um programa para um caixa eletronico que leia um determinado valor e retorne a 
# quantidade de dinheiro a ser entregue.
# O caixa eletronico trabalha com os seguintes valores:
#     Moedas: 0.01, 0.05, 0.10, 0.25, 0.50, 1.00
#     Notas: 2.00, 5.00, 10.00, 20.00, 50.00, 100.00
# Os valores devem estar dentro de dicionarios que deverão estar dentro de uma única lista.
# A impressão do dinheiro deve ser com .format()

saque = float(input('Digite um valor: '))

cem = int(saque/100)
saque = saque % 100

cinquenta = int(saque/50)
saque = saque % 50

vinte = int(saque/20)
saque = saque % 20

dez = int(saque/10)
saque = saque % 10

cinco = int(saque/5)
saque = saque % 5

dois = int(saque/2)
saque = saque % 2

um = int(saque/1)
saque = saque % 1

cinquenta_centavos = int(saque/0.5)
saque = saque % 0.5

vintecinco_centavos = int(saque/0.25)
saque = saque % 0.25

dez_centavos = int(saque/0.10)
saque = saque % 0.10

cinco_centavos = int(saque/0.05)
saque = saque % 0.05

um_centavo = int(saque/0.01)
saque = saque % 0.01

print(f'{cem} Nota(s) R$ 100,00.\n'
        f'{cinquenta} Notas(s) R$ 50,00.\n' 
        f'{vinte} Notas(s) R$ 20,00.\n'
        f'{dez} Notas(s) R$ 10,00.\n'
        f'{cinco} Notas(s) R$ 5,00.\n'
        f'{dois} Notas(s) R$ 2,00.\n'
        f'{um} centavo(s) R$ 1,00.\n'
        f'{cinquenta_centavos} centavo(s) R$ 0,50.\n'
        f'{dez_centavos} centavo(s) R$ 0,10.\n'
        f'{cinco_centavos} centavo(s) R$ 0,05.\n'
        f'{um_centavo} centavo(s) R$ 0,01.\n')