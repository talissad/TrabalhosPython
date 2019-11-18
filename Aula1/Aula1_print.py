nomeCompleto = 'Talissa' ' ' 'Dahlke\n'

print((nomeCompleto).count('a'))        #conta quantos A tem na variavel
print((nomeCompleto).lower())           #coloca tudo minisculo
print((nomeCompleto).upper())           #coloca tudo maiusculo
print((nomeCompleto).split(' '))        #remove o caracter entre aspas e transforma em lista
print((nomeCompleto).strip().split('a'))#junta as funções, não imprimi o \n como a outra iria fazer
print((nomeCompleto).strip())           #remove todos os espaços antes e depois da variavel, remove também o \n
print((nomeCompleto).capitalize())      #Coloca a primeira letra Maiuscula

pessoa = ["", "Carinhoso", "Atencioso", "Querido"]
print((' nem ').join(pessoa))
print('a'.join('b'))

frase = ("Teti torrado")
print("a".join(frase))


print(pessoa[1], pessoa[2])         #imprime somente as variaveis que foram solicitadas
print(pessoa[:1])                   #imprime todos até o primeiro
print(pessoa[1:])                   #imprime todos depois do primeiro
print(pessoa[1:3])                  #imprime todos entre a sequencia
print(frase[5:])                    #imprime o caracter em diante da frase
print(frase[5:10])                  #imprime a sequencia entre os números
print(pessoa.count('Carinhoso'))    #Verifica se existe a palavra na sequencia
print(pessoa.count(' carinhoso'.strip().capitalize()))  


#print((pessoa).join(' nem'))        #Adiciona a palavra ao longo da variavel
#no join o que delimita são as , como não há , na string ele não inclui