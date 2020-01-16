import MySQLdb
import sys
sys.path.append('C:/Users/900161/Documents/TrabalhosPython/Aula33-4')
from model.pessoa import Pessoa

class PessoaDb:
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor() #----- Salva o cursor da conexão em uma variável
    
    def listar_todos(self):
        comando_sql_select = "SELECT * FROM pessoa" #----- Criação do comando SQL e passado para o cursor
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall() #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        lista_pessoas_classe = self.converter_tabela_classe(resultado)
        return lista_pessoas_classe

    def buscar_por_id(self, id):
        comando_sql_select = f"SELECT * FROM pessoa WHERE ID= {id}"
        self.cursor.execute(comando_sql_select) #----- Criação do comando SQL e passado para o cursor
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        lista_pessoas = [] #cria uma lista para armazenar os dicionarios
        for p in lista_tuplas:
            p1 = Pessoa() #----- Criação do objeto da classe pessoa
            p1.id = p[0] #--- pega cada posição da tupla e atribui a uma chave do dicionário
            p1.nome = p[1]
            p1.sobrenome= p[2]
            p1.idade = p[3]
            p1.endereco_id = p[4]
            lista_pessoas.append(p1)
        return lista_pessoas