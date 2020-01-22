class LinguagemBackend:
    def __init__(self):
        self.id = 0
        self.linguagem = ''
        self.fk_back = 0

    def __str__(self):
        return f'{self.id};{self.linguagem};{self.fk_back}'