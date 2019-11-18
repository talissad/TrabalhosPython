lista_numeros = [1,2,3,5,6]
numero = 2


if'Teti'.count('t') > 0:
    print('Existe "T" em "Teti"')
if 'e' in 'Teti':
    print('Existe "E" em "Teti"')
if 'M' not in 'Teti':
    print('Não existe "M" em "Teti"')

if 4 in lista_numeros:
    print('Existe o 4 na lista')
else:
    print('Não existe')

if numero in lista_numeros:
    print('Existe')
else:
    print('Não existe')

lista_vazia = []

if len(lista_numeros) ==0:
    print('Vazia')
else:
    print('Não vazia')

lista_nomes = []
if lista_nomes:
    print('Tem nomes')
else:
    print('Não tem nomes')

nome = ''
if nome:
    print('Preenchido')
else:
    print('Vazio')

nome = ''
print(nome)
nome = 'Maykon'
print(nome[2])

#nome[2] = 'T'
print(nome)