class Pessoa:
    id = 0
    nome = ''
    sobrenome = ''
    idade = 0
    endereco_id = 0

    def __str__(self):
        return f'{self.id}; {self.nome}; {self.sobrenome}; {self.idade}; {self.endereco_id}'