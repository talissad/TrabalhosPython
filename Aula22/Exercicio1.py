# Aula 21 - 09-12-2019
# Crie uma classe cliente:
# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo
# 2) como metodos: receber salario, comprar, pagar divida
# Quando recebe aumenta o dinheiro na carteira. 
# quando compra aumenta os bens e diminui o dinheiro na carteira
# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira e aumentar a divida.
# Para pagar a divida tem que ter dinheiro o suficiente na carteira
# 3) atributos de estado: dinheiro na carteira, divida, bens

class Cliente:
    def __init__(self, codigo, cpf, nome, idade, sexo):
        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

        self.divida = 0
        self.bens = []
        self.dinheiro_carteira = 0

    def receber_salario(self, receber):
        self.dinheiro_carteira = receber + self.dinheiro_carteira


    def compra(self, bem, valor):
            self.bens.append(bem)
            if valor <= self.dinheiro_carteira:
                self.dinheiro_carteira = self.dinheiro_carteira - valor
            else:
                self.divida = self.divida - (self.dinheiro_carteira - valor)
                self.dinheiro_carteira = 0     
    
    def divida(self, divida):
            if self.divida < self.dinheiro_carteira:
                self.divida = self.bens - self.dinheiro_carteira


pessoa = Cliente(10, 8181548, 'Amanda', 18,  'f')

pessoa.receber_salario(8000)
pessoa.compra = ('casa', 90000)

print(pessoa.dinheiro_carteira)
print(pessoa.bens)
print(pessoa.divida)
