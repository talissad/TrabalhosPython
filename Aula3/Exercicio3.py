#nome = input('Digite o nome do funcionário: ')
#cpf = input('Digite o CPF: ')
#registro = input('Digite o Número do Registro: ')
#cargo = input('Digite o cargo: ')

from Aula3_impostos import calculo_inss
from Aula3_impostos import calculo_irrf

salario = float(input('Digite o salário: '))

inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)

salario_liquido = salario - inss - irrf

print(f'\nINSS: {inss}')
print(f'IRRF: {irrf}')
print(f'Seu salario líquido é: {salario_liquido}\n')