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

    def cliente(self):
        a = self.dado_bruto.strip().split(';')
        self.codigo = int(a[0])
        self.nome = (a[1])
        self.idade = int(a[2])
        self.sexo = (a[3])
        self.email = (a[4])
        self.telefone = (a[5])
  
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.


    def salvar(self):
        arquivo = open ('Aula23/cadastro2', 'a')
        dicionario_pessoas = (f'Codigo: {c.codigo}, Nome: {c.nome}, Idade: {c.idade}, Sexo: {c.sexo}, Email: {c.email}, Telefone: {c.telefone}')
        arquivo.close()

    def atualizar(self, codigo, nome, idade, sexo, email, telefone):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone


c = Cliente(dadobruto)     
c.cliente()
c.atualizar(2, 'Talissa', 22, 'f', 'attas@fmd', '89732527385')

print(f'Codigo: {c.codigo}, Nome: {c.nome}, Idade: {c.idade}, Sexo: {c.sexo}, Email: {c.email}, Telefone: {c.telefone}')
