class FrameworkFrontend:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.fk_front = 0

    def __str__(self):
        return f'{self.id};{self.nome};{self.fk_front}'