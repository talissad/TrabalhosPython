# 1) Crie uma classe cliente que possui como atributos: Nome, idade, telefone.
# A variável nome e telefone deve ser um string. A variável idade deve ser valor nteiro.
# O cliente deve ter R$ 100.00 de dinheiro como saldo no cartão.
# 2) Crie metodos para: adicionar saldo no cartão, descontar saldo do cartão e verificar saldo do cartão.



# 3) para descontar o saldo do cartão, deve-se entra com a quantidade de ml e o valor por ml da bebida.
# O metodo deve imprimir na tela a quantidade de bebida e o valor descontado. Caso o saldo do cliente não
# seja o suficiente, deve-se imprimir o valor descontado e o volume liberado de bebida.

# Bebidas:
# Refrigerante R$ 0.01 /ml 
# Cerveja ipa  R$ 0.05 /ml 
# Cerveja ale  R$ 0.063 /ml 

class Cliente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

        self.saldo_inicial = 10

    def adicionar_saldo(self, valor):
        self.saldo_inicial += valor

    def descontar_saldo(self, ml, preco):
        #self.saldo_inicial -= desconto
        custo = ml * preco
        if custo > self.saldo_inicial:
            liberado = self.saldo_inicial / preco
            print(f"Valor descontado: {self.saldo_inicial}. Foram liberados {liberado:.2f} ml.")
            self.saldo_inicial = 0
        else:
            self.saldo_inicial -= custo
            print(f"Valor descontado: {custo}. Foram liberados {ml} ml.")


    def verificar_saldo(self):
        pass

pessoa = Cliente('Talissa', 22, '82347236')

print(pessoa.saldo_inicial
pessoa.adicionar_saldo(10)
print(pessoa.saldo_inicial)
pessoa.descontar_saldo(100, 0.063)
print(pessoa.saldo_inicial)
pessoa.descontar_saldo(1000, 0.05)
print(pessoa.saldo_inicial)