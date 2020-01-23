import MySQLdb
import sys
sys.path.append('C:/Users/900161/Documents/TrabalhosPython/Aula37')
from Model.squads import Squads

class SquadsDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans11', user='padawans11', passwd='at2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        #comando = f"SELECT * FROM squads"
        comando = f"SELECT * FROM squads AS s LEFT JOIN linguagemBackend AS l  s.linguagemBackend_id = l.id LEFT JOIN frameworkFrontend as f  ON s.frameworkFrontend_id = f.id LEFT JOIN sgbds as b ON s.sgbds_id = b.id"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        #comando = f"SELECT * FROM squads WHERE P.ID = {id}"
        comando = f"SELECT * FROM squads AS s LEFT JOIN linguagemBackend AS l  s.linguagemBackend_id = l.id LEFT JOIN frameworkFrontend as f  ON s.frameworkFrontend_id = f.id LEFT JOIN sgbds as b ON s.sgbds_id = b.id  WHERE s.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squads:Squads):
        comando = f""" INSERT INTO squads
        (
            Nome,
            Descricao,
            NumeroPessoas,
            linguagemBackend_id
            FrameworkFrontend_id
            Sgbds_id
        )
        VALUES
        (
            '{squads.nome}',
            '{squads.descricao}',
            {squads.numeroPessoas},
            '{squads.linguagemBackend.id}',
            '{squads.frameworkFrontend.id}'
            '{squads.sgbds.id}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squads:Squads):
        comando = f""" UPDATE squads
        SET
            Nome = '{squads.nome}',
            Descricao ='{squads.descricao}',
            NumeroPessoas = {squads.numeroPessoas},
            LinguagemBackend_id = '{squads.linguagemBackend.id}',
            FrameworkFrontend_id =' {squads.frameworkFrontend.id}'
            Sgbds_id = {squads.sgbds.id}
        WHERE ID = {squads.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM squads WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
    