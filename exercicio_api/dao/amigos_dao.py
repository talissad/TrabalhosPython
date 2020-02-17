class AmigosDao:
    def ler_arquivo(self):
        self.lista_pessoas = []
        arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "r")
        for pessoas in arquivo:
            pessoas = pessoas.strip()
            self.lista_pessoas.append(pessoas)
        return self.lista_pessoas

    def list_all(self):
        for i in self.lista_pessoas:
            print(i+'\n')

    def get_by_id(self,  id):
        if id in self.lista_pessoas:

            print(id)

    def insert(self):
        arquivo = open("C:/Users/900161/Documents/TrabalhosPython/exercicio_api/pessoas.txt", "a")
        while retorno == 's':
            retorno = input('Gostaria de adicionar alguém a lista? (S/N) ')
            if retorno == 's':
                arquivo.write('\n'+input('Digite o nome da pessoa a ser adicionada: '))
            arquivo.close()
        return f"objeto(s) inserido(s) com sucesso!"

    def delete(self, id):
        del(id)
        return f"objeto deletado com sucesso!"
