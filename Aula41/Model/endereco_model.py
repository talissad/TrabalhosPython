
class EnderecoModel:
    def __init__(self, logradouro, numero, complemento, cidade, cep, id=None):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.cep = cep
