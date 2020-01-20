class Endereco:
    id = 0
    logradouro = '' 
    numero = ''
    complemento = '' 
    bairro = ''
    cidade = ''
    cep = ''

    # def exportar_txt(self, lista_enderecos):
    #     with open('Aula33-4/endereco.txt','a') as arquivo:
    #         for p in lista_enderecos:
    #             arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}'