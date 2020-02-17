import os

class AmigosDao:
    def __init__(self):
        self.lista_pessoas = []
        arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "r")
        for pessoas in arquivo:
            pessoas = pessoas.strip()
            self.lista_pessoas.append(pessoas)

    def list_all(self):
        return self.lista_pessoas

    def get_by_id(self, id):
        for i in self.lista_pessoas:
            if int(i[0]) == int(id):
                return i

    def insert(self):
        texto = input("Digite uma frase para acrescentar ao arquivo:\n")
        arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "a")
        arquivo.write(texto + '\n')
        arquivo.close()
        return f"objeto(s) inserido(s) com sucesso!"

    def remove(self, id):
        lista_atualizada = []
        for i in self.lista_pessoas:
            if int(i[0]) == int(id):
                os.remove(i)
                    arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "w", lista_atualizada)
        return f"objeto deletado com sucesso!"
