import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula33-4')
import MySQLdb
from model.endereco import Endereco

class EnderecoDb:
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()
    
    def listar_todos(self):
        comando_sql_select = "SELECT * FROM endereco"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        lista_endereco_classe = self.converter_tabela_classe(resultado)
        return lista_endereco_classe

    def buscar_por_id(self, id):
        comando_sql_select = f"SELECT * FROM endereco WHERE ID= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        lista_endereco = []
        for e in lista_tuplas:
            e1 = Endereco()
            e1.id = e[0]
            e1.logradouro = e[1]
            e1.numero= e[2]
            e1.complemento = e[3]
            e1.bairro = e[4]
            e1.cidade = e[5]
            e1.cep = e[6]
            lista_endereco.append(e1)
        return lista_endereco
