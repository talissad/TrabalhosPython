# Estrutura de repetição - FOR
'''
#Geralmente inicia em 0, último elemento não é incluido
#Inicio, fim
for i in range (1,10):
   print (f'{i} Padawans HBsis')

#Inicio, fim, incremento
for i in range (0,10, 2):
   print (f'{i}- par ')

lista = ['Mateus', 'Matheus', 'Marcela', 'Nicole', 'Tonho', 'Pablo']
# for range tem que saber o tamanho da lista
for i in range(0,6):
   print (lista[i])

#Adiciona elemento
lista.append ('Natan')

#for in apresenta todos os elementos
for sortudo in lista:
    print (sortudo) '''

numero = 10
for i in range (0,11):
    print(f'{i} x {numero} = {i*numero}')


