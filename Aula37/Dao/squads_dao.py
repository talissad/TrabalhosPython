import MySQLdb
import sys
sys.path.append('C:/Users/900161/Documents/TrabalhosPython/Aula37')
from Model.squads import Squads

class SquadsDao:
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM squads"
        comando = f"SELECT * FROM squads AS s LEFT JOIN linguagemBackend AS l LEFT JOIN frameworkFrontend as f LEFT JOIN sgbds as b ON s.linguagemBackend.id = l.ID"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM squads WHERE P.ID = {id}"
        ##comando = f"SELECT * FROM squads AS s LEFT JOIN linguagemBackend AS l LEFT JOIN frameworkFrontend as f LEFT JOIN Sgbds as b ON
        ##### s.linguagemBackend.id = l.ID WHERE s.ID = {id}"

        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squads:Squads):
        comando = f""" INSERT INTO squads
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackend
            FrameworkFrontend

            LinguagemBackend.id
            FrameworkFrontend.id
            Sgbds.id
        )
        VALUES
        (
            '{squads.nome}',
            '{squads.descricao}',
            {squads.numeroPessoas},
            '{squads.linguagemBackend}',
            '{squads.frameworkFrontend}'

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
            LinguagemBackend = '{squads.linguagemBackend}',
            FrameworkFrontend =' {squads.frameworkFrontend}'

        WHERE ID = {squads.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM squads WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
    