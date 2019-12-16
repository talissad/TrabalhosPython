# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))

# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:

# 1.1) Qual é o tamanho da lista1?
print(len(lista1)) 
print(len(lista2)) 
print(len(lista3))

# 1.2) Qual é o maior valor da lista2?
print(max(lista1))
print(max(lista2))
print(max(lista3))

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print(f'\nO máximo é {max(lista1)} e o mínimo é {min(lista1)}. A soma deles é {max(lista1)+min(lista1)}')
print(f'O máximo é {max(lista2)} e o mínimo é {min(lista2)}. A soma deles é {max(lista2)+min(lista2)}')
print(f'O máximo é {max(lista3)} e o mínimo é {min(lista3)}. A soma deles é {max(lista3)+min(lista3)}\n')

# 1.4) Qual é a média aritmética da lista1?
print(f'A média é de {(sum(lista1)) / (len(lista1))} ')

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(f'\nA soma dos elementos da lista 1 é: {sum(lista1)}')
print(f'A soma dos elementos da lista 2 é: {sum(lista2)}')
print(f'A soma dos elementos da lista 3 é: {sum(lista3)}')
print(f'A soma das listas é: {sum(lista1) + sum(lista2) + sum(lista3)}\n')

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
n = 1
for i in lista1:
    print(f'O número {n} é: {i}')
    n += 1

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
try:
    print(f'\nLISTA 1 - Posição 5 = {lista1[4]} - Posição 9 = {lista1[8]} - Posição 10 = {lista1[9]} - Posição 25 = {lista1[24]}')
except IndexError:
    print('\nA lista 1 não possui o mínimo de 25 itens')

try:
    print(f'LISTA 2 - Posição 5 = {lista2[4]} - Posição 9 = {lista2[8]} - Posição 10 = {lista2[9]} - Posição 25 = {lista2[24]}')
except IndexError:
    print('A lista 2 não possui o mínimo de 25 itens')

try:
    print(f'LISTA 3 - Posição 5 = {lista3[4]} - Posição 9 = {lista3[8]} - Posição 10 = {lista3[9]} - Posição 25 = {lista3[24]}\n')
except IndexError:
    print('A lista 3 não possui o mínimo de 25 itens\n')

# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
if len(lista1) > len(lista2) and len(lista1) > len(lista3):
    print(f'A maior lista é a primeira. Ela possui {len(lista1)} itens')
elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
    print(f'A maior lista é a segunda. Ela possui {len(lista2)} itens')
elif len(lista3) > len(lista1) and len(lista3) > len(lista2):
    print(f'A maior lista é a terceira. Ela possui {len(lista3)} itens')
elif len(lista1) == len(lista2) and len(lista1) != len(lista3):
    print(f'A lista 1 e a lista 2 possui a mesma quantidade de elementos, elas possuem {len(lista1)} itens')
elif len(lista2) == len(lista3) and len(lista2) != len(lista1):
    print(f'A lista 2 e a lista 3 possui a mesma quantidade de elementos, elas possuem {len(lista1)} itens')
else:
    print(f'As listas possuem a mesma quantidade. Elas tem {len(lista1)} itens\n')

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
soma_listas = sum(lista1) + sum(lista2) + sum(lista3)
if min(lista1) > min(lista2) and min(lista1) > min(lista3):
    print(f'O menor número é da lista 1. O resultado da conta é: {soma_listas - min(lista1)}')
if min(lista2) > min(lista3) and min(lista2) > min(lista1):
    print(f'O menor número é da lista 2. O resultado da conta é: {soma_listas - min(lista2)}')
else:
    print(f'O menor número é da lista 3. O resultado da conta é: {soma_listas - min(lista3)}')

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
try:
    soma = max(lista1) + max(lista2) + max(lista3) + min(lista1) + min(lista2) + min(lista3)
except IndexError:
    print('A lista não possui o mínimo de 25 itens')
finally:
    print(f'\nA soma de todos os menores com os maiores é: {soma}')
