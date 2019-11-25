# 01/03/2025
from metodo import tesouroDireto

compras = float(input('Quantas cotas você quer comprar? '))
taxa = float(input('Digite a Taxa Selic: '))
periodo = int(input('Digite o periodo: '))
valorMinimo = 104.1 
cotas = compras // valorMinimo
valorInvestimento = cotas * valorMinimo

taxa = 0.02 + taxa


print('Você terá R$', tesouroDireto(valorInvestimento, taxa, periodo))

print('\n')
