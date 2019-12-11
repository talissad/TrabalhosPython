# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)




# 4) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 5) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)

#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!



# 1) Crie uma classe cadastro.
class Cadastro:
    def __init__(self):
        
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.
    def ler_cadastro(self):
        arquivo = open('Aula23/cadastro.txt','r')
        cadastro = []
        for linha in arquivo:
            pessoas = pessoas.strip().split(';')
            dicionario_pessoas = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
            cadastro.append(dicionario_pessoas)
        arquivo.close()
        return cadastro

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
    def salvar(self):
        arquivo = open(f'Aula23/cadastro.txt','a')
        for pessoa in lista:
            texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}\n"
            arquivo.write(texto)
        arquivo.close()

# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
    def cadastrar(self):
        
    










# def ler_cadastro():
#     arquivo = open('Aula23/cadastro.txt','r')
#     cadastro = []
#     for pessoas in arquivo:
#         pessoas = pessoas.strip().split(';')
#         dicionario_pessoas = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
#         cadastro.append(dicionario_pessoas)
#     arquivo.close()
#     return cadastro

# # 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# # 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo 
# # assim não pode se repetir.
# def salvar_dados(self, codigo):
#     novo_cadastro = open('Aula23/cadastro.txt','a')
#     for linhas in novo_cadastro:
#         novo = []
#         for informacoes in range(0, quantidade_cadastros):
#             codigo = int(input('Difite o código: '))
#             nome = input('Difite o nome: ')
#             idade = int(input('Difite a idade: '))
#             email = input('Difite o email: ')
#             telefone = input('Difite o telefone')
#             texto = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
#         novo.append(texto)
#         print(texto)

# def consulta(lista_consulta_funcao,numero):
#    for lista_consulta in lista_consulta_funcao:
#         if int(lista_consulta['codigo']) == numero:
#             print(f"{lista_consulta['codigo']}\n{lista_consulta['nome']}\n{lista_consulta['idade']}\n{lista_consulta['sexo']}\n{lista_consulta['email']}\n{lista_consulta['telefone']}")
#         elif numero == 's':
#             numero = False
#         else:
#             print('código não encontrado!')

# lista1 = ler_cadastro()
# lista_email(lista1)

# while True:
#    a=int(input('Digite um numero: '))
#    consulta(lista1,a)



# verificar = ler_cadastro()
# salvar_dados()

# quantidade_cadastros = int(input('Digite a quantidade de cadastros: '))



