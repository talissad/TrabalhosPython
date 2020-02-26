import sqlalchemy as db


class BaseDao:
    def __init__(self):
        # Cria a conexao com o banco de dados
        # (SGBD +conector ://usuario :senha @url :porta /nome da database
        conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/aulabd")
        criado_sessao = db.orm.sessionmaker()
        criado_sessao.configure(bind=conexao)
        self.sessao = criado_sessao()