nome = input('Digite o nome do funcionário: ')
cpf = input('Digite o CPF: ')
registro = input('Digite o Número do Registro: ')
cargo = input('Digite o cargo: ')
salario = float(input('Digite o salário: '))

print("\nSalário é igual a: ", salario)

if salario <= 1751.81:
    descontoInss = salario * 0.08
    print('Desconto INSS: ', descontoInss)
elif salario >= 1751.82 and salario <= 2919.72:
    descontoInss2 = salario * 0.095
    print('Desconto INSS: ', descontoInss2)
else:
    descontoInss3 = salario * 0.11
    print('Desconto INSS: ', descontoInss3)

if salario <= 1903.98:
    print ('Não tem desconto do IRRF')
elif salario >=1903.95 and salario <= 2826.65:
    descontoIrrf = salario * 0.075
    print('Desconto IRRF: ', descontoIrrf)
elif salario >=2826.66 and salario <= 3751.05:
    descontoIrrf2 = salario * 0.15
    print('Desconto IRRF: ', descontoIrrf2)
elif salario >=3751.06 and salario <= 4664.68:
    descontoIrrf3 = salario * 0.225
    print('Desconto IRRF: ', descontoIrrf3)
else:
    descontoIrrf4 = salario * 0.275
    print('Desconto IRRF: ', descontoIrrf4)