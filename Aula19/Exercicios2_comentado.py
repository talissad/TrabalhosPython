# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)


cab = ['nome', 'telefone', 'email','idade']

pess = [['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
        ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
        ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
        ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17']]


# cab[0] = nome

# cab[0]   pess[0][0] 
# cab[1]   pess[1][0] 
# cab[2]   pess[2][0]  
# cab[3]   pess[3][0]

# cab[0]   pess[0][1] 
# cab[1]   pess[1][1] 
# cab[2]   pess[2][1]  
# cab[3]   pess[3][1]

def lista_maior_18(pess, cab):


        lista = []
        for i in range(7):
                dicionario = {}
                for j in range(4):
                        dicionario [ cab[j] ] =  pess[j][i]
                # dicionario [ 'nome' ] =  'alex'
                
                lista.append(dicionario)

        # lista = 
        # [{'nome': 'Alex', 'telefone': '4799991', 'email': 'a@a.com', 'idade': '18'},
        #  {'nome': 'Paulo', 'telefone': '4799992', 'email': 'b@b.com', 'idade': '25'},
        #   {'nome': 'Pedro', 'telefone': '4799993', 'email': 'c@c.com', 'idade': '40'}, 
        #   {'nome': 'Mateus', 'telefone': '4799994', 'email': 'd@d.com', 'idade': '16'}, 
        #   {'nome': 'Carlos', 'telefone': '4799995', 'email': 'e@e.com', 'idade': '15'}, 
        #   {'nome': 'João', 'telefone': '4799996', 'email': 'f@f.com', 'idade': '19'}, 
        #   {'nome': 'Joaquim', 'telefone': '4799997', 'email': 'g@g.com', 'idade': '17'}]

        lista_maiores = []
        for pessoa in lista:
                # pessoa = {'nome': 'Alex', 'telefone': '4799991', 'email': 'a@a.com', 'idade': '18'}
                if int(pessoa['idade']) >= 18:
                        lista_maiores.append(pessoa)
        return lista_maiores

lista1 = lista_maior_18(pess, cab)
#print(lista1)

for i in lista1:
        print(i)


# print(lista_maiores)

# lista = []
# for pessoa in pess:
#         # pessoa = ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim']
#         dicionario = {'nome':pessoa[0], 'telefone':pessoa[1], 'email': pessoa[2], 'idade': pessoa[3]}
#         lista.append(dicionario)