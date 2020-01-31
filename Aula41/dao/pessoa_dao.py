import MySQLdb

from Aula41.Model.pessoa_model import PessoaModel

class PessoaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host = '127.0.0.1', database = 'aulabd', user = 'root', passwd = '')
        #self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    # 5 metodos do CRUD
    def list_all(self):
        self.cursor.execute("SELECT * FROM pessoa")
        pessoas = self.cursor.fetchall()
        lista_pessoa = []
        for p in pessoas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM pessoa Where id={id}")
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p.__dict__

    def insert(self, pessoa):
        return 'Cadastrando uma pessoa'

    def update(self, pessoa):
        return 'Alterando uma pessoa'

    def remove(self, id):
        self.cursor.execute(f"Delete * FROM pessoa Where id={id}")
        self.connection.commit()
        return f'Removido a pessoa de id: {id}'