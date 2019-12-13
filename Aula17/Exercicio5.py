# 5.1 - Crie uma função que retorne False se a lista criada tiver alguma repetição ou tiver 
# menos que 10 númenros. retorne True se a lista tiver 10 números e nenhuma repetição.

# 5.2 - Crie uma lista com 100 números aleátorios. Estes números não pode ser repetidos.
# Na lista deve ter numeros de 1 a 999. Imprima na tela uma mensagem dizendo se a lista está 
# confrome a especificação ou fora de especificação.

from random import randint

a = int(input('Digite a quantidade de números: '))

lista = []
for i in range(0, a):
    lista.append(randint(0, 100))

b = len(lista)
if b < 10:
    print('Há menos que 10 números')
else:
    print('Há mais que 10 números') 

lista.sort()

# for x in lista:
#     if x == x:
#         print(f'O número {x} não é igual ao anterior! ')
#     else:
#         print(f'O número {x} é igual ao anterior! ')

