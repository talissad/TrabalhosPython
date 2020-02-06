import sqlalchemy as db


class BaseDao:
    def __init__(self):
        conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/aulabd")
        criado_sessao = db.orm.sessionmaker()
        criado_sessao.configure(bind=conexao)
        self.sessao = criado_sessao()

        # (host='127.0.0.1', database='aulabd', user='root', passwd='')
