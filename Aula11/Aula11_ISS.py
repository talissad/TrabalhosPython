from metodo import iss

salario = float(input("Digite seu salário: "))
imposto = int(input("Digite a porcentagem de impostos "))

print('\nEm impostos você gasta aproximadamente: ', iss(salario, imposto))