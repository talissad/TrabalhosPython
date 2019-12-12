# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

# dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

class Cliente:
    def __init__(self, dadobruto):
        self.dado_bruto = dadobruto

        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

    def tratamento(self):
        a = self.dado_bruto.strip().split(';')
        self.codigo = int(a[0])
        self.nome = (a[1])
        self.idade = int(a[2])
        self.sexo = (a[3])
        self.email = (a[4])
        self.telefone = (a[5])
  

pessoa = Cliente(dadobruto)
pessoa.tratamento()     
print(f'Codigo: {pessoa.codigo}, Nome: {pessoa.nome}, Idade: {pessoa.idade}, Sexo: {pessoa.sexo}, Email: {pessoa.email}, Telefone: {pessoa.telefone}')

# OUTRA FORMA DE PRINT
#     def __str__(self):

#      texto = f'''

# Codigo: {self.codigo }
# Nome: {self.nome}
# Idade: {self.idade}
# Sexo: {self.sexo}
# Email:{self.email}
# Telefone: {self.telefone}'''
#         return texto

#FORMA DE VERIFICAR CODIGO DO CLIENTE
# def __eq__(self, valor):
#     return self.codigo == valor

# while True:
#     var = int(input('Digite o codigo do cliente: '))
#     print(a[0] == var)


