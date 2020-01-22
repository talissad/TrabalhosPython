import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37')
import MySQLdb
from Model.linguagem_backend import LinguagemBackend

class BackDao:
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM linguagemBackend"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM linguagemBackend WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, linguagemBackend:LinguagemBackend):
        comando = f""" INSERT INTO linguagemBackend
        (
            linguagem,
            fk_back
        )
        VALUES
        (
            '{linguagemBackend.linguagem}',
            {linguagemBackend.fk_back}
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, linguagemBackend:LinguagemBackend):
        comando = f""" UPDATE linguagemBackend
        SET
            linguagem = '{linguagemBackend.linguagem}',
            fk_back = '{linguagemBackend.fk_back}',
        WHERE ID = {linguagemBackend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM linguagemBackend WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()