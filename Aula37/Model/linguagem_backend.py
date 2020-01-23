class LinguagemBackend:
    def __init__(self):
        self.id = 0
        self.linguagem = ''

    def __str__(self):
        return f'{self.id};{self.linguagem}'