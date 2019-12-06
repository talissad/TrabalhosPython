# Aula 20 - 05-12-2019

# DICA: use o metodo round(valor,2) para arredondar os numeros para fazer
# a conta. Assim evita que o python use valores muito quebrados para as 
# contas.
# Exemplo:
# >>> round(2.7555,2)
# 2.76

# DICA2: Há 3 operadores matemáticos para a divisão: / // e o %
# / - é a divisão total entre os dois números. Pode resultar em numeros 
# reais.
# Exemplo: 5 / 3 = 1.6666666666666667
# // - é a divisão inteira. Ela vai resultar em números inteiros
# Exemplo: 5 // 3 = 1
# % - é o resto da divisão inteira. É o que sobra.
# Exemplo: 5 % 3 = 2



# 1 - Caixa eletrônico 
# Com estas listas de  dicionários:

nota = [{'Nota(s)':100.00},{'Nota(s)':50.00},{'Nota(s)':20.00},
        {'Nota(s)':10.00},{'Nota(s)':5.00},{'Nota(s)':2.00},]
            
            
moeda = [{'Moeda(s)':1.00},{'Moeda(s)':0.50},{'Moeda(s)':0.25},
         {'Moeda(s)':0.10},{'Moeda(s)':0.05},{'Moeda(s)':0.01}]

# Monte um metodo que leia um valor e imprima (f-string) a quantidade de 
# cada nota(s) e moeda(s) necessária(s) para devolver o troco ao cliente.


saque = int(input('Digite um valor: '))

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

print(f'{cem} Nota(s) R$ 100,00.\n'
        f'{cinquenta} Notas(s) R$ 50,00.\n' 
        f'{vinte} Notas(s) R$ 20,00.\n'
        f'{dez} Notas(s) R$ 10,00.\n'
        f'{cinco} Notas(s) R$ 5,00.\n'
        f'{dois} Notas(s) R$ 2,00.\n')