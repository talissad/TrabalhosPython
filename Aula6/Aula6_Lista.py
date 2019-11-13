#inicia variavel do tipo lista
lista = []

#inicia variavel do tipo lista, com elementos
lista2 = ['Marcela', 'Nicole', '*Matheus']

#inicia variavel do tipo lista, com inteiros
lista3 = [1, 2, 3, 5]

#lista de tipos diferentes
lista4 = [1, 'Talissa', 3.5]

#Adiciona elementos em listas já criadas
lista.append(lista2)
lista.append(lista3)

#imprime
print (lista)
print (lista2)
print (lista3)

#Listas com dados do Input
lista.append(input("Digite seu nome: "))
lista_perguntas = [input("Digite sua idade: "), input("Digite seu endereço: ")]

print (lista)
print (lista_perguntas)

#Escolhe a posição para imprimir
posicao = int(input('Digite a posição: '))
print ( lista2[posicao-1] )
print ( lista2[3] )