# Aula 21 - 16-12-2019
# Metodos da lista

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_inpura_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import lista_simples_impura
from geradorlista import embaralhar
from geradorlista import embaralhar_int_str_hard
from geradorlista import binario
import copy
from binhex import *

'''# Exercícios baseados do livro Pense em Python.

# 1) Escreva uma função chamada nested_sum que receba a lista de listas de números
# inteiros (lista1), retorne uma lista única e print a soma de todos os elementos.
# Por exemplo:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> lista = nested_sum(t)
# 21
# >>> lista
# [1, 2, 3, 4, 5, 6]

lista1 = [lista_simples_int() ,lista_simples_int(), lista_simples_int()]

def nested_sum(lista):
    lista_completa = []
    lista_completa.extend(lista1[0])
    lista_completa.extend(lista1[1])
    lista_completa.extend(lista1[2])
    print(sum(lista_completa))
    return lista_completa

# def nested_sum(lista):
#     lista_completa = []
#     for i in lista:
#         for j in i:
#             lista_completa.append(j)
#     print(sum(lista_completa))
#     return lista_completa

lista = nested_sum(lista1)
print(lista)

# __________________________________________________________________________
# 2) Com as seguintes listas, transforme em uma string para poder gravar (futuramente) em um arquivo!

lista_cadastro = ['codigo', 'cpf', 'nome_completo', 'data_de_nascimento',
                  'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero', 'complemento']

lista_cadastrados = ['1', '11111111111', 'João Carlos', '12/12/90',
                  'SC', 'Camboriú', '8833', 'Tabuleiro', 'Cerejeiras', '45', 'ap 101']

lista_cadastrados1 = ['2', '22222222222', 'Paulo Roberto', '23/01/89',
                  'SC', 'Blumenau', '99999', 'Velha', '7 de setembro', '55', '']

lista_qualquer = []
lista_qualquer.extend(lista_cadastro)
lista_qualquer.extend(lista_cadastrados)
lista_qualquer.extend(lista_cadastrados1)

string_lista = ';'.join(lista_qualquer)

print(string_lista)

# __________________________________________________________________________
# 3) Com as seguintes lista, transforme em uma string para poder gravar (futuramente) em um arquivo!

lista_cadastros = [['1', 'Arnaldo', '23', 'm', 'alexcabeludo2@hotmail.com', '014908648117'], 
                    ['2', 'Haroldo', '44', 'f', 'baratarebelde@gmail.com', '050923172729'],
                    ['3', 'Pilar', '50', 'm', 'wanderson10sp@gmail.com', '018937341049'], 
                    ['4', 'Suzete Salvador', '45', 'f', 'eladiomp2@yahoo.com.br', '056928409823'], 
                    ['5', 'Riane', '37', 'f', 'orkutzimpower@terra.com.br', '018916004377'], 
                    ['6', 'Waldir', '34', 'f', 'nandah.s2@bol.com.br', '058903756441'], 
                    ['7', 'Lilian', '22', 'f', 'arydoido@gmail.com', '031958621596'], 
                    ['8', 'Matilde', '20', 'm', 'eu_kaka_@hotmail.com', '012941959390'], 
                    ['9', 'Samanta', '19', 'm', 'carro.tuning@yahoo.com.br', '028964480437'], 
                    ['10', 'Margarida', '30', 'm', 'paraaconta.08@hotmail.com', '047903547580'], 
                    ['11', 'Evelyn', '31', 'm', 'joaosilvaticudo@gmail.com', '053958638386'], 
                    ['12', 'Alessio', '29', 'm', 'w.nill02@gmail.com', '033961294774'], 
                    ['13', 'Yolanda', '25', 'm', 'patty_karen2005@hotmail.com', '027903312626'], 
                    ['14', 'Germana', '33', 'f', 'jarlinhatopdelinhagv@hotmail.com', '053964603415'], 
                    ['15', 'Helio', '33', 'f', 'juh.slim@gmail.com', '046997316461'], 
                    ['16', 'Liége', '21', 'f', 'gledsonlds@hotmail.com', '056992948431'], 
                    ['17', 'Yan', '42', 'm', 'lucapratto@yahoo.com.br', '016963562866'], 
                    ['18', 'Silvain', '50', 'f', 'hie.s2@hotmail.com', '021963399433'], 
                    ['19', 'Brian', '33', 'f', 'juliagabrielle06@hotmail.com', '027962676732'], 
                    ['20', 'Deoclides', '40', 'f', 'patriciamascena@gmail.com', '012961047979'], 
                    ['21', 'Ja0queline', '32', 'm', 'aninha183@hotmail.com', '014958997782'], 
                    ['22', 'Ro0samaria', '45', 'f', 'j_leosao@hotmail.com', '026944672627'], 
                    ['23', 'Ca0rla', '42', 'm', 'jhasdfjo@hotmail.com', '046976625208'], 
                    ['24', 'Ai0da Santos', '30', 'f', 'nayara.cristinap@hotmail.com', '034920819199'], 
                    ['25', 'Th0omas', '19', 'm', 'jfdslinda@bol.com.br', '030974027667'], 
                    ['26', 'Naiara', '23', 'm', 'darknees_666@ig.com.br', '018976696717'], 
                    ['27', 'Karyne', '17', 'm', 'garotosonhador_1@hotmail.com', '054984689319'], 
                    ['28', 'Alenis Dias', '43', 'f', 'vi_vi_cristinaf@hotmail.com', '034980886309'], 
                    ['29', 'Grace', '38', 'm', 'amandakell@uol.com.br', '041932906720'], 
                    ['30', 'Zacarias', '31', 'm', 'loca.som@hotmail.com', '041926007066']]

lista_cadastro_junto = []
for i in lista_cadastros:
    lista_cadastro_junto.append(';'.join(i))

string_lista_cadastro = ';'.join(lista_cadastro_junto)

print(string_lista_cadastro)

# __________________________________________________________________________
# 4) Crie uma função que solicite 5 nomes e retorne uma lista com todos eles

lista_nomes = [] 
def adicionar_pessoa(chamada):
    for i in range(1,6):
        a = input(f'Digite o {i} nome: ')
        a.split()
        lista_nomes.append(a)
    return lista_nomes

lista = adicionar_pessoa(lista_nomes)
print(lista_nomes)

# __________________________________________________________________________
# 5) Com a lista "Nomes", feita no exercicio 4 (anterior) faça uma cópia para 'Nomes2' e adicione 
# o nome "Pedro Paulada" no "Nomes" e "Paulo Cacetada" no "Nomes2"
lista_nomes2 = copy.deepcopy(lista_nomes)
try:
    lista_nomes.append('Pedro Paulada')
    lista_nomes2.append('Paulo Cacetada')
except:
    print(lista_nomes)
    print(lista_nomes2)

print(lista_nomes)
print(lista_nomes2)
# __________________________________________________________________________
# 6) Com a lista 'lista_aninhada' faça uma cópia e nomeie como 'lista_aninhada_2'. Na lista_aninhada
# adicione ao lado do número 9 o número 10. Na lista_aninhada_2 adicione ao lado do número 8 a frase 
# "Aqui não pode ter o número 10!"

lista_aninhada = [1,2,3,[4,5,[7,[9],8],6]]

lista_aninhada2 = copy.deepcopy(lista_aninhada) 

lista_aninhada[3][2][1].insert(1, 10)
lista_aninhada2[3].insert(3, 'Aqui não pode ter o número 10!')

print(lista_aninhada)
print(lista_aninhada2)
'''

# 7) Continuando o exercicio, adicione a lista Nomes (exercicio 4) na lista_aninhada entre os números
# 2 e o 3. Na lista_aninhada_2 adicione a "Pedro Pedroca" entre os números 4 e 5. 
# Adicione na lista_aninhada, entre os números 1 e 2, a frase 'um, dois' e na lista_aninhada_2, 
# entre os números 1 e 2 a frase 'Adiciono qualquer coisa em qualquer lugar nesta lista!'


# 8) Com a lista1, ordene os números de maior para menor!
lista1 = lista_simples_int(100)
lista1.sort(reverse= True)
#print(lista1)

# 9) Com a lista2, ordene os números de menor para maior!
lista2 = lista_simples_int(100)
lista2.sort()
#print(lista2)

# 10) Usando o metodo, adicione a lista1 e lista2 (já ordenadas) na lista0.
lista0 = []

for i in lista1:
    lista0.append(i)

for i in lista2:
    lista0.append(i)

#adicionar = lista1, lista2

# 11) Ordene a lista0 e diga qual é o maior valor, menor valor e em quais das listas (lista1 ou lista2)
# estes pertencem.
lista0.sort()
print(max(lista0))
print(min(lista0))

if max(lista0) in lista1 and max(lista0) not in lista2:
    print('O número máximo pertence a primeira lista')

elif max(lista0) in lista2 and max(lista0) not in lista1:
    print('O número máximo pertence a segunda lista')

elif max(lista0) in lista2 and max(lista0) in lista1:
    print('O número máximo está nas duas listas')

elif min(lista0) in lista1 and min(lista0)  not in lista2:
    print('O número minímo pertence a primeira lista')

elif min(lista0) in lista2 and min(lista0) not in lista1:
    print('O número minímo pertence a segunda lista')

elif min(lista0) in lista2 and min(lista0) in lista1:
    print('O número minímo está nas duas listas')

else:
    print('Possui erro no codigo')      

# 12) Com a lista_aninhada e lista_aninhada2, do exercicio 7, remova todas as alterações que nelas foram
# colocadas. Salve os dados removidos em uma lista e imprima na tela cada item em uma linha
# usando o f-string (use o .pop() )



# 13) Remova, usando o .remove(), os seguintes itens destas listas:

lista_cadastro = ['codigo', 'cpf', 'nome_completo', 'data_de_nascimento',
                  'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero', 'complemento']

lista_cadastrados = ['1', '11111111111', 'João Carlos', '12/12/90',
                  'SC', 'Camboriú', '8833', 'Tabuleiro', 'Cerejeiras', '45', 'ap 101']

lista_cadastrados1 = ['2', '22222222222', 'Paulo Roberto', '23/01/89',
                  'SC', 'Blumenau', '99999', 'Velha', '7 de setembro', '55', '']

# 13.1) cpf da lista_cadastro
# 13.4) rua 
# 13.9) cidade
# 13.10) data_de_nascimento
lista_cadastro.remove('cpf')
lista_cadastro.remove('rua')
lista_cadastro.remove('cidade')
lista_cadastro.remove('data_de_nascimento')

# 13.2) camboriú da lista_cadastrados
# 13.5) 8833 
# 13.7) João Carlos
# 13.8) 11111111111
lista_cadastrados.remove('Camboriú')
lista_cadastrados.remove('8833')
lista_cadastrados.remove('João Carlos')
lista_cadastrados.remove('11111111111')

# 13.3) Paulo Roberto da lista_cadastrados1
# 13.6) Velha
lista_cadastrados1.remove('Paulo Roberto')
lista_cadastrados1.remove('Velha')

print(lista_cadastro)
print(lista_cadastrados)
print(lista_cadastrados1)

# 14) Com a lista_fusao mostre com f-strig e o metodo .index() a posição dos seguintes elementos:
# 14.1) cidade
# 14.2) João Carlos
# 14.3) Camboriú
# 14.4) 12/12/90
# 14.5) 99999
# 14.6) nome_completo
# 14.7) 22222222222
# 14.8) Tabuleiro
# 14.9) numero

lista_fusao = ['codigo', 'cpf', 'nome_completo', 'data_de_nascimento',
                  'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero', 'complemento',
                  '1', '11111111111', 'João Carlos', '12/12/90',
                  'SC', 'Camboriú', '8833', 'Tabuleiro', 'Cerejeiras', '45', 'ap 101',
                  '2', '22222222222', 'Paulo Roberto', '23/01/89',
                  'SC', 'Blumenau', '99999', 'Velha', '7 de setembro', '55', '']

a = (lista_fusao.index('cidade'))
b = (lista_fusao.index('João Carlos'))
c = (lista_fusao.index('Camboriú'))
d = (lista_fusao.index('12/12/90'))
e = (lista_fusao.index('99999'))
f = (lista_fusao.index('nome_completo'))
g = (lista_fusao.index('22222222222'))
h = (lista_fusao.index('Tabuleiro'))
i = (lista_fusao.index('numero'))

print(f'posição - Cidade: {a}\nposição - João Carlos: {b}\nposição - Camboriú: {c}\nposição - 12/12/90: {d}\n'
        f'posição - 99999: {e}\nposição - nome_completo: {f}\nposição - 22222222222: {g}\nposição - Tabuleiro: {h}\n'
        f'posição - numero: {i}\n')


# 15) Usando o metodo .index(), Crie uma função que localize a posição dos seguintes nomes: 
# Germana, Deoclides, Zacarias, Karyne, Helio, Silvain, Aida Santos
# Esta função deve receber como parametro a lista_cadastros e o nome. Deve retornar uma lista contendo
# o endereço do nome na lista_cadastros. 
# Exemplo:

# >>> lista = localize(lista_cadastros,'Alenis Dias')
# >>> lista_cadastros[ lista[0] ][ lista[1] ]
# 'Alenis Dias'

# Dica: Use o tratamento de ecessões para evitar erro ao procurar um indice que não existe!

lista_cadastros = [['1', 'Arnaldo', '23', 'm', 'alexcabeludo2@hotmail.com', '014908648117'], ['2', 'Haroldo', '44', 'f', 'baratarebelde@gmail.com', '050923172729'], ['3', 'Pilar', '50', 'm', 'wanderson10sp@gmail.com', '018937341049'], ['4', 'Suzete Salvador', '45', 'f', 'eladiomp2@yahoo.com.br', '056928409823'], ['5', 'Riane', '37', 'f', 'orkutzimpower@terra.com.br', '018916004377'], ['6', 'Waldir', '34', 'f', 'nandah.s2@bol.com.br', '058903756441'], ['7', 'Lilian', '22', 'f', 'arydoido@gmail.com', '031958621596'], ['8', 'Matilde', '20', 'm', 'eu_kaka_@hotmail.com', '012941959390'], ['9', 'Samanta', '19', 'm', 'carro.tuning@yahoo.com.br', '028964480437'], ['10', 'Margarida', '30', 'm', 'paraaconta.08@hotmail.com', '047903547580'], ['11', 'Evelyn', '31', 'm', 'joaosilvaticudo@gmail.com', '053958638386'], ['12', 'Alessio', '29', 'm', 'w.nill02@gmail.com', '033961294774'], ['13', 'Yolanda', '25', 'm', 'patty_karen2005@hotmail.com', '027903312626'], ['14', 'Germana', '33', 'f', 'jarlinhatopdelinhagv@hotmail.com', '053964603415'], ['15', 'Helio', '33', 'f', 'juh.slim@gmail.com', '046997316461'], ['16', 'Liége', '21', 'f', 'gledsonlds@hotmail.com', '056992948431'], ['17', 'Yan', '42', 'm', 'lucapratto@yahoo.com.br', '016963562866'], ['18', 'Silvain', '50', 'f', 'hie.s2@hotmail.com', '021963399433'], ['19', 'Brian', '33', 'f', 'juliagabrielle06@hotmail.com', '027962676732'], ['20', 'Deoclides', '40', 'f', 'patriciamascena@gmail.com', '012961047979'], ['21', 'Jaqueline', '32', 'm', 'aninha183@hotmail.com', '014958997782'], ['22', 'Rosamaria', '45', 'f', 'j_leosao@hotmail.com', '026944672627'], ['23', 'Carla', '42', 'm', 'jhasdfjo@hotmail.com', '046976625208'], ['24', 'Aida Santos', '30', 'f', 'nayara.cristinap@hotmail.com', '034920819199'], ['25', 'Thomas', '19', 'm', 'jfdslinda@bol.com.br', '030974027667'], ['26', 'Naiara', '23', 'm', 'darknees_666@ig.com.br', '018976696717'], ['27', 'Karyne', '17', 'm', 'garotosonhador_1@hotmail.com', '054984689319'], ['28', 'Alenis Dias', '43', 'f', 'vi_vi_cristinaf@hotmail.com', '034980886309'], ['29', 'Grace', '38', 'm', 'amandakell@uol.com.br', '041932906720'], ['30', 'Zacarias', '31', 'm', 'loca.som@hotmail.com', '041926007066']]
a = lista_cadastros.index('Germana')
b = lista_cadastros.index('Deoclides')
c = lista_cadastros.index('Zacarias')
d = lista_cadastros.index('Karyne')
e = lista_cadastros.index('Helio')
f = lista_cadastros.index('Silvain')
g = lista_cadastros.index('Aida Santos')

print(a,b,c,d,e,f,g)

# 16) Conte na lista1 a quantidade dos seguintes valores (use o f-string):
# 16.1) 4529
# 16.2) 29
# 16.3) 1107
# 16.4) 7927
# 16.5) 6967
# 16.6) 5964
# 16.7) 8893
# 16.8) 3972
# 16.9) 10
# 16.10) 8548
# 16.11) 8214
# 16.12) 169
# 16.13) 6214
# 16.14) 15
# 16.15) 4937
# 16.16) 9909
# 16.17) 3412
# 16.18) 6306
# 16.19) 306

lista1 = lista_simples_int(10000)
print(f'4529:{lista1.count(4529)}\n29:{lista1.count(29)}\n1107:{lista1.count(1107)}\n7927:{lista1.count(7927)}\n6967:{lista1.count(6967)}\n'
        f'5964:{lista1.count(5964)}\n8893:{lista1.count(8893)}\n3972:{lista1.count(3972)}\n10:{lista1.count(10)}\n8548:{lista1.count(8548)}\n'
        f'8214:{lista1.count(8214)}\n169:{lista1.count(169)}\n6214:{lista1.count(6214)}\n15:{lista1.count(15)}\n4937:{lista1.count(4937)}\n'
        f'9909:{lista1.count(9909)}\n3412:{lista1.count(3412)}\n6306:{lista1.count(6306)}\n306:{lista1.count(306)}\n')

###################### .reverse() ######################

# 17) Um numero binário, localizado em uma lista 'listabin', necessita ser convertido em número decimal.
# Faça uma função que converta o número binário e retorne o número em decimal. Imprima na tela
# o número binário e o resultado. (use o .reverte())

listabin = binario()
print(listabin)

convertendo = 0
dec = 1

listabin.reverse(hex)



# 18) com as seguintes listas, imprima elas e .reverte() suas posições. Some as posições e retorne a lista com
# as somas.
# Exemplo:
# >>> lista1        = [42,3, 1, 4]
# >>> lista_reversa = [4, 1, 3, 42]
# >>> lista_soma    = [46,4, 4, 46]

# 18.1) lista1
lista1 = lista_simples_int(8)
print(lista1)
print(lista1.reverse(), '\n')
# 18.2) lista2
lista2 = lista_simples_int(8)
print(lista2)
print(lista2.reverse(), '\n')

# 18.3) lista3
lista3 = lista_simples_int(8)
print(lista3)
print(lista3.reverse(), '\n')

# 18.4) lista4
lista4 = lista_simples_int(8)
print(lista4)
print(lista4.reverse(), '\n')

# 18.5) lista5
lista5 = lista_simples_int(8)
print(lista5)
print(lista5.reverse(), '\n')

# 18.6) lista6
lista6 = lista_simples_int(8)
print(lista6)
print(lista6.reverse(), '\n')

# 18.7) lista7
lista7 = lista_simples_int(8)
print(lista7)
print(lista7.reverse(), '\n')

# 18.8) lista8
lista8 = lista_simples_int(8)
print(lista8)
print(lista8.reverse(), '\n')

# 18.9) lista9
lista9 = lista_simples_int(8)
print(lista9)
print(lista9.reverse(), '\n')

# 18.10) lista10
lista10 = lista_simples_int(8)
print(lista10)
print(lista10.reverse(), '\n')

# 18.11) lista11
lista11 = lista_simples_int(8)
print(lista11)
print(lista11.reverse(), '\n')

# 18.12) lista12
lista12 = lista_simples_int(8)
print(lista12)
print(lista12.reverse(), '\n')

# 18.13) lista13
lista13 = lista_simples_int(8)
print(lista13)
print(lista13.reverse(), '\n')

# 18.14) lista14
lista14 = lista_simples_int(8)
print(lista14)
print(lista14.reverse(), '\n')

# 18.15) lista15
lista15 = lista_simples_int(8)
print(lista15)
print(lista15.reverse(), '\n')

# 18.16) lista16
lista16 = lista_simples_int(8)
print(lista16)
print(lista16.reverse(), '\n')

# 18.17) lista17
lista17 = lista_simples_int(8)
print(lista17)
print(lista17.reverse(), '\n')

# 18.18) lista18
lista18 = lista_simples_int(8)
print(lista18)
print(lista18.reverse(), '\n')

# 18.19) lista19
lista19 = lista_simples_int(8)
print(lista19)
print(lista19.reverse(), '\n')



# 19) Com um comando .clear()  apague as seguintes informações:
# 19.1) apague toda a lista
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]
lista_aninhada.clear()

# 19.2)  apague somente: [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]
lista_aninhada.clear()

# 19.3) [4, 5, [7, [9], 8], 6]
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]
lista_aninhada.clear()

# 19.4)  [7, [9], 8]
lista_aninhada = [1, 2, 3, [4, 5, [1, 2, 3, [4, 5, [7, [9], 8], 6]], 6]]
lista_aninhada.clear()

# 19.5) 5,6
lista_aninhada = [[1,2],[3,4],[5,6],[7,8],[9,10]]
lista_aninhada.clear()

# 19.6) 9,10
lista_aninhada = [[1,2],[3,4],[5,6],[7,8],[9,10]]
lista_aninhada.clear()
'''