a = 10
b = 10
b = 10.0

print(id(a))
print(id(b))

print(a is b)
__________________________
lista = '1; 2, 3, agua, vento'

__________________________
Split = transforma em lista. 
    EX(.split';')
Join = agrupa as informações da lista. 
    EX(';'.join(lista))
Copy = copia a lista. 
    EX (lista_copia = lista.copy()) 
    import copy
    lista_copia_2 = copy.deepcopy(lista) #copia tudo
Count = conta os elementos da lista
    lista_contar = [10,5,20,2,3,10,5,9,5]
    lista_contar.count(10) #conta quantos 10 há na lista
IN = verifica se há em determina variavel ou lista
    print(1 in lista)

Interavel = adicionar informações em uma lista
    lista.extends(range(12,90)) # adicionar de 12 até 89
    lista.insert(2, 'Posição 2')

Index = busca informações na lista
    lista.index('Posição 2', 0, 1) # Tem que colocar um número a mais, se ele não achar 1 vai retornar erro.

Sort = ordena a lista
    lista = [8,8,6,9,781,8,84,5715,7215]
    lista.sort() #maior para o menor
    lista.sort(reverse = True) #menor para o maior
    lista.reverse() #menor para o maior

Pop = remove elementos
    lista = [8,8,6,9,781,8,84,4,5715,4,7215]
    elem = lista.pop(3) #3 é a posição do elemento a ser eliminado
    lista.remove(4) # deleta o primeiro elemento, no caso é o número 4 (remove o item)

clear = limpa a lista
    lista.clear()

##### Metodo sort ####
__________________________
