import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37')
import MySQLdb
from Model.sgbds import Sgbds

class SgbdsDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans11', user='padawans11', passwd='at2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM sgbds"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM sgbds WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgbds:Sgbds):
        comando = f""" INSERT INTO sgbds
        (
            nome
        )
        VALUES
        (
            '{sgbds.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, sgbds:Sgbds):
        comando = f""" UPDATE sgbds
        SET
            nome= '{sgbds.nome}'
        WHERE ID = {sgbds.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM sgbds WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()