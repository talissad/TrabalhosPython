# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)

#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!




# 1) Crie uma classe cadastro.
class Cadastro:
    def __init__(self):
        self.lista = []
        self.ler()

    def ler(self):
        try:
            arquivo = open('Aula23/cadastro.txt','r')
            for pessoa in arquivo:
                pessoa = pessoa.strip().split(';')
                dicionario_pessoa = {'codigo':pessoa[0], 'nome':pessoa[1], 'idade':pessoa[2], 'sexo':pessoa[3], 'email':pessoa[4], 'telefone':pessoa[5]}
                self.lista.append(dicionario_pessoa)
        finally:
            arquivo.close()

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
    def salvar(self, nome, atributo='a'):
        try:
            arquivo = open(f'Aula23/{nome}.txt',atributo)
            for pessoa in self.lista:
                texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}"
                arquivo.write(texto)
        finally:
            arquivo.close()

# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
    def cadastrar(self):
        nome = input('Digite o nome: ')
        idade = int(input('Digite o idade: '))
        sexo = input('Digite o sexo: ')
        email = input('Digite o email: ')
        telefone = input('Digite o telefone: ')
        
        codigo = int(self.lista[-1]['codigo']) + 1
        
        dicionario_pessoa = {'codigo':codigo, 'nome':nome, 'idade':idade, 'sexo':sexo, 'email':email, 'telefone':telefone}
        self.lista.append(dicionario_pessoa)
        
 # 4) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
    def consulta(self, codigo):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                print(f"Codigo: {pessoa['codigo']}\nNome: {pessoa['nome']}\nIdade: {pessoa['idade']}\nSexo: {pessoa['sexo']}\nEmail: {pessoa['email']}\nTelefone: {pessoa['telefone']}\n")
                break


# 5) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
    def atualizar(self, codigo):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                nome = input('Digite o nome: ')
                idade = int(input('Digite o idade: '))
                sexo = input('Digite o sexo: ')
                email = input('Digite o email: ')
                telefone = input('Digite o telefone: ')
                #Atualizar dados:
                pessoa['nome'] = nome
                pessoa['idade'] = idade
                pessoa['sexo'] = sexo
                pessoa['email'] = email
                pessoa['telefone'] = telefone
                


# numero_consulta = int(input('Digite o codigo da consulta: '))

p = Cadastro()

# p.cadastrar()
# p.salvar

p.consulta(20)
p.atualizar(20)
p.consulta(20)






















# class Cadastro:
#     def __init__(self):
        
#         self.codigo = None
#         self.nome = None
#         self.idade = None
#         self.sexo = None
#         self.email = None
#         self.telefone = None

# # Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.
#     def ler_cadastro(self):
#         arquivo = open('Aula23/cadastro.txt','r')
#         cadastro = []
#         for linha in arquivo:
#             pessoas = pessoas.strip().split(';')
#             dicionario_pessoas = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
#             cadastro.append(dicionario_pessoas)
#         arquivo.close()
#         return cadastro

#     def salvar(self):
#         arquivo = open(f'Aula23/cadastro.txt','a')
#         for pessoa in lista:
#             texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}\n"
#             arquivo.write(texto)
#         arquivo.close()

#     def cadastrar(self):
        
    



# #     def consulta(self):
# #         codigo = int(input('Digite um codigo: '))
# #         for linha in self.lista:
# #             if linha == codigo:
# #                 print(linha)
# #                 break






# # # def ler_cadastro():
# # #     arquivo = open('Aula23/cadastro.txt','r')
# # #     cadastro = []
# # #     for pessoas in arquivo:
# # #         pessoas = pessoas.strip().split(';')
# # #         dicionario_pessoas = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
# # #         cadastro.append(dicionario_pessoas)
# # #     arquivo.close()
# # #     return cadastro

# # # # 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# # # # 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo 
# # # # assim não pode se repetir.
# # # def salvar_dados(self, codigo):
# # #     novo_cadastro = open('Aula23/cadastro.txt','a')
# # #     for linhas in novo_cadastro:
# # #         novo = []
# # #         for informacoes in range(0, quantidade_cadastros):
# # #             codigo = int(input('Difite o código: '))
# # #             nome = input('Difite o nome: ')
# # #             idade = int(input('Difite a idade: '))
# # #             email = input('Difite o email: ')
# # #             telefone = input('Difite o telefone')
# # #             texto = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
# # #         novo.append(texto)
# # #         print(texto)

# # # def consulta(lista_consulta_funcao,numero):
# # #    for lista_consulta in lista_consulta_funcao:
# # #         if int(lista_consulta['codigo']) == numero:
# # #             print(f"{lista_consulta['codigo']}\n{lista_consulta['nome']}\n{lista_consulta['idade']}\n{lista_consulta['sexo']}\n{lista_consulta['email']}\n{lista_consulta['telefone']}")
# # #         elif numero == 's':
# # #             numero = False
# # #         else:
# # #             print('código não encontrado!')

# # # lista1 = ler_cadastro()
# # # lista_email(lista1)

# # # while True:
# # #    a=int(input('Digite um numero: '))
# # #    consulta(lista1,a)



# # # verificar = ler_cadastro()
# # # salvar_dados()

# # # quantidade_cadastros = int(input('Digite a quantidade de cadastros: '))



