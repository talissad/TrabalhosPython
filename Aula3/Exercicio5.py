salario = float(input('Digite seu salário: '))

gastos = salario * 0.5
investimentosLongoPrazo = salario * 0.2
investimentosCurtoPrazo = salario * 0.1
livre = salario * 0.2

print('Seus gastos devem ser na média de {}\nOs investimentos a longo prazo devem ser de: {}\nOs investimentos de curto prazo devem ser de: {}\nE você pode gastar {} livremente'.format(gastos, investimentosLongoPrazo, investimentosCurtoPrazo, livre))