import MySQLdb
import sys
sys.path.append('C:/Users/900161/Documents/TrabalhosPython/Aula37')
from Model.squads import Squads

class SquadsDao:
    conexao = MySQLdb.connect(host='127.0.0.1', database='Squads', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM squads"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM squads WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squads):
        comando = f""" INSERT INTO squads
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackEnd
            FrameworkFrontEnd
        )
        VALUES
        (
            '{squads.nome}',
            '{squads.descricao}',
            {squads.numeroPessoas},
            '{squads.linguagemBackEnd}',
            '{squads.frameworkFrontEnd}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squads):
        comando = f""" UPDATE squads
        SET
            Nome = '{squads.nome}',
            Descricao ='{squads.descricao}',
            NumeroPessoas = {squads.numeroPessoas},
            LinguagemBackEnd = {squads.linguagemBackEnd}
            FrameworkFrontEnd = {squads.frameworkFrontEnd}

        WHERE ID = {squads.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM squads WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()
    