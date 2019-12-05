lista = [['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]]

# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com biblioteca.

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.

lista_produtos = {}

for i in lista:
    for j in i:
        dicionario_produtos = {'codigo':lista[0], 'produto':lista[1], 'valor':lista[2], 'quantidade':lista[3]}
        dicionario_produtos.append(lista_produtos)
    # arquivo.close()
    # return lista


k = i
print(k)