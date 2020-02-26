import MySQLdb

from Aula50.model.AulaModel import Aula

class AulaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host = '127.0.0.1', database = 'aulabd', user = 'root', passwd = '')
        self.cursor = self.connection.cursor()          #pedir + informações

    # 5 metodos do CRUD
    def list_all(self):
        self.cursor.execute("SELECT * FROM saladeaula")
        informacoes = self.cursor.fetchall()
        lista_informacoes = []
        for a in informacoes:
            aulas = Aula(a[1], a[2], a[3], a[4], a[0])
            lista_informacoes.append(aulas.__dict__)
        return lista_informacoes

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM saladeaula Where id={id}")
        aulas = self.cursor.fetchone()
        a = Aula(aulas[1], aulas[2], aulas[3], aulas[4], aulas[0])
        return a.__dict__

    def insert(self, aula:Aula):
        self.cursor.execute("""
            INSERT INTO saladeaula 
            (professor, quantidade, sala, disciplina) 
            VALUES('{}',{},'{}','{}')""".format(aula.professor, aula.quantidade, aula.sala, aula.disciplina))
        self.connection.commit()
        id = self.cursor.lastrowid
        aula.id = id
        return aula.__dict__

    def update(self, aula:Aula):
        self.cursor.execute("""
            UPDATE saladeaula 
                SET 
                    professor = '{}',
                    quantidade = {},
                    sala = '{}',
                    disciplina = '{}'                    
                WHERE ID = {} """.format(aula.professor, aula.quantidade, aula.sala, aula.disciplina, aula.id))
        self.connection.commit()
        return aula.__dict__

    def remove(self, id):
        self.cursor.execute("DELETE FROM saladeaula WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido a turma de id : {}'.format(id)