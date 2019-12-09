# #1 o que uma pessoa tem? Quais as caracteristica?
# nome
# idade
# telefone
# sexo 

# #2 o que a pessoa faz?
# respira
# dorme
# corre
# bebe
# come
# multiplica

# #3 como a pessoa está agora?
# divida
# cansada
# viva
# fome
# sede

class Pessoa: 
    def __init__(self, nome1, idade1, telefone1, sexo1):
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1

        self.divida = None
        self.cansada = 'não'
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'

    def respira(self, respira):
        if self.viva == True:
            if respira == True:
                self.viva = True
            else:
                self.viva = False


    def corre(self, distancia):
        if self.viva:
            if distancia <100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'
            elif distancia >= 200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'

    def dorme(self):
        if self.viva:
            self.cansada = 'não'
            self.bebe()
            self.come()

    def come(self):
        if self.viva:
            self.fome = 'não'

    def bebe(self):
        if self.viva:
            self.sede = 'não'

    def multiplica(self):
        pass
        
p = Pessoa('Antonio', 18, '479999988', 'm')
# print(dir(p))
p.corre(300)
p.dorme()
p.come()


print(f'Nome é {p.nome} \nEstá vivo? {p.viva} \nEstá com fome? {p.fome} \nEstá com sede? {p.sede} \nEstá cansada? {p.cansada}')