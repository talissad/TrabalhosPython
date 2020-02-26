import sqlalchemy as db

class BaseDao:
    def __init__(self):
        conexao = db.create_engine("mysql+mysqlconnerctor://root:@127.0.0.1:3306/")
        criado_sessao = db.orm.sessionmaker()
        criado_sessao.configure(bind=conexao)
        self.sessao = criado_sessao()