import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()


class AulaModel(BaseAlchemy):
    __tablename__ = "saladeaula"
    id = db.Column(db.Integer, primary_key=True)
    professor = db.Column(db.String(length=45))
    quantidade = db.Column(db.Integer)
    sala = db.Column(db.String(length=45))
    disciplina = db.Column(db.String(length=45))

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.id, self.professor, self.quantidade, self.sala, self.disciplina)
