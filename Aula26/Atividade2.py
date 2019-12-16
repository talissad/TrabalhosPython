# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista1 = embaralhar(2,10)

a = lista1[0]
b = lista1[1]
c = lista1[2]
d = lista1[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.

lista2 = embaralhar(2,10,2)
print(lista2)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
print(f'\nA is B? {lista2[0] is lista2[1]}')
print(f'A == B? {lista2[0] == lista2[1]}\n')

# print(f'\nA is B? {a is b}')
# print(f'A == B? {a == b}\n')
# print(f'B is C? {b is c}')
# print(f'B == C? {b == c}\n')
# print(f'C is D? {c is d}')
# print(f'C == D? {c == d}\n')

# 2) Qual é o maior valor destas duas listas
if max(lista2[0]) > max(lista2[1]):
    print(f'O máximo da lista A é: {max(lista2[0])}')

else:
    print(f'O máximo da lista B é: {max(lista2[1])}\n')

# print(f'O máximo da lista A é {max(a)}') 
# print(f'O máximo da lista B é {max(b)}') 
# print(f'O máximo da lista C é {max(c)}') 
# print(f'O máximo da lista D é {max(d)}\n') 

# 3) Qual é o maior valor de cada lista
print(f'O máximo da lista A é: {max(lista2[0])}')
print(f'O máximo da lista B é: {max(lista2[1])}\n')

# 4) Há o número 10 dentro da lista[0]?
print(f'Há {lista2[0].count(10)} número(s) 10 na lista A')

# 5) Há o número 20 dentro da lista[1]?
print(f'Há {lista2[1].count(20)} número(s) 20 na lista B\n')

# 6) Quantos números da lista[0] tem dentro da lista[1]?
contador = 0

for i in lista2[0]:
    if i in lista2[1]:
        contador += 1   

print(f'Existe {contador} repetidos nas listas')

# 7) Mostre os números da lista[0] que estão dentro da lista[1]
numeros = []
for i in lista2[0]:
    if i in lista2[1]:
        numeros.append(i)
print(f'Os números que existem na lista 1 e que se repetem na lista 2 são: {numeros}\n')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
soma_listaA = sum(lista2[0])
for i in lista2[1]:
    print(f'Resultado: soma da lista {soma_listaA} * {i} = {soma_listaA*i}\n')

# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
div1 = max(lista2[0]) // min(lista2[0])
div2 = max(lista2[1]) // min(lista2[1])

print(f'O resultado da divisão de {max(lista2[0])} com {min(lista2[0])} é {div1}')
print(f'O resultado da divisão de {max(lista2[1])} com {min(lista2[1])} é {div2}')

if div1 in lista2[0]:
    print(f'Existe {div1} na lista A')
elif div1 in lista2[1]:
    print(f'Existe {div1} na lista B')
elif div2 in lista2[0]:
    print(f'Existe {div2} na lista A')
elif div2 in lista2[1]:
    print(f'Existe {div2} na lista B')
else:
    print('Não existe o resultado das divisões nas listas')


# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
a = int(max(lista2[0]))
b = int(min(lista2[1]))

print(f'\nO maior número ({a}) da lista A existe em B? {a in lista2[1]}')
print(f'O menor número ({b}) da lista B existe em A? {b in lista2[0]}\n')