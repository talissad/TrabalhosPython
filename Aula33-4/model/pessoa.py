class Pessoa:
    id = 0
    nome = ''
    sobrenome = ''
    idade = 0
    endereco_id = 0 

    def exportar_txt(self, lista_pessoas):
        with open('Aula33/Aula33-4/pessoas4.txt','a') as arquivo: #----- Cria um arquivo e atribui a uma variável 'arquivo'
            for p in lista_pessoas: #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
                arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco.id}'