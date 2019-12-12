# Aula 21 - 12-12-2019


# Produto

# Crie uma classe produto.

# Esta classe deve ter como atributo: codigo produto(int), nome, marca, preço de custo(float),
# preço de venda(float) e quantidade em estoque(int).

# Cada produto deve ter um código unico e sequencial.
# Só pode vender produtos que tenha no estoque.

# Metodos: Atualizar dados do produto, adicionar e 
# remover produtos do estoque, __str__ e __eq__ (para pesquisar mais facilmente o
# código do produto)


class Produto:
    def __init__(self,codigo, nome, marca, preco_custo, preco_venda, estoque):
        self.codigo = codigo
        self.nome = nome
        self.marca = marca
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.estoque = estoque


    def atualizar (self):
        '''
        Este metodo serve para atualizar o cadastro do produto. 
        Os dados que podem ser atualizados são: 
        nome, marca, preço de custo(float),preço de venda(float)
        '''
        def atualizar(self, codigo):
        for produto in range:
            if int(produto['codigo']) == codigo:
                nome = input('Digite o nome: ')
                marca = int(input('Digite a marca: '))
                preco_custo = float(input('Digite o preco de custo: '))
                preco_venda = float(input('Digite o preco de venda: '))
                #Atualizar dados:
                produto['nome'] = nome
                produto['marca'] = marca
                produto['preco_custo'] = preco_custo
                produto['preco_venda'] = preco_venda
        
        
        pass

    def atualizar_estoque(self):
        '''
        Esta função é usada para atualizar a quantidade de produto no estoque.
        
        '''
                estoque = input('Digite a quantidade de estoque: ')
                produto['estoque'] = estoque
        pass

    

    def __eq__(self,valor):
        '''
        Este metodo deve comparar se o valor do código é igual ao valor.
        Se positivo ele retorna True caso contrário retorna False
        '''
        pass

    def __srt__(self):
        '''
        Este metodo deve retornar uma string com todos os dados.
        Use f-string para interpolar o texto com as variáveis
        '''
        pass