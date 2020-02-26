import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37')
import MySQLdb
from Model.framework_frontend import FrameworkFrontend


class FrontDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans11', user='padawans11', passwd='at2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM frameworkFrontend"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM frameworkFrontend WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, frameworkFrontend:FrameworkFrontend):
        comando = f""" INSERT INTO frameworkFrontend
        (
            nome
        )
        VALUES
        (
            '{frameworkFrontend.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, frameworkFrontend:FrameworkFrontend):
        comando = f""" UPDATE frameworkFrontend
        SET
            nome = '{frameworkFrontend.nome}'
            
        WHERE ID = {frameworkFrontend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM frameworkFrontend WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()