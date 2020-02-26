import MySQLdb

from Aula41.Model.endereco_model import EnderecoModel

class EnderecoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host = '127.0.0.1', database = 'aulabd', user = 'root', passwd = '')
        #self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    # 5 metodos do CRUD
    def list_all(self):
        self.cursor.execute("SELECT * FROM endereco")
        enderecos = self.cursor.fetchall()
        lista_endereco = []
        for p in enderecos:
            endereco = EnderecoModel(p[1], p[2], p[3], p[4], p[5], p[6], p[0])
            lista_endereco.append(endereco.__dict__)
        return lista_endereco

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM endereco Where id={id}")
        endereco = self.cursor.fetchone()
        p = EnderecoModel(endereco[1], endereco[2], endereco[3], endereco[4], endereco[5], endereco[6],   endereco[0])
        return p.__dict__

    def insert(self, endereco: EnderecoModel):
        self.cursor.execute("""
            INSERT INTO endereco 
            (logradouro, numero, complemento, bairro, cidade, cep) 
            VALUES('{}','{}',{})""".format(endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.cep))
        self.connection.commit()
        id = self.cursor.lastrowid
        endereco.id = id
        return endereco.__dict__

    def update(self, endereco: EnderecoModel):
        self.cursor.execute("""
              UPDATE endereco 
                  SET 
                      logradouro = '{}',
                      numero = '{}',
                      complemento = '{}',
                      bairro = '{}',
                      cidade= '{}',
                      cep= '{}'                      
                  WHERE ID = {}
           """.format(endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.cep, endereco.id))
        self.connection.commit()
        return endereco.__dict__

    def remove(self, id):
        self.cursor.execute("DELETE FROM endereco WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido a endereco de id : {}'.format(id)