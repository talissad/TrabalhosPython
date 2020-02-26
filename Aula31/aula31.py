# pip3 install flask_mysql

import MySQLdb

def listar_todos(c):
    cursor.execute('SELECT * FROM pessoa')
    pessoas = cursor.fetchall()
    for p in pessoas:
        print(p)

def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM pessoa where id = {id}')
    pessoa = c.fetchone()
    print(pessoa)

def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM pessoa where sobrenome like '{sobrenome}%'")
    for p in c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO pessoa (NOME, SOBRENOME, IDADE, ENDERECO_ID )VALUES('{nome}', '{sobrenome}',{idade},{endereco_id})")
    cn.commit()

#alterar pessoa
try:
    def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
        cr.execute(f"UPDATE pessoa SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID={id} ")
        cn.commit()
except (MySQLdb.Error, MySQLdb.Warning) as e:
    if (e.args[0]==1542):
        print(f'Erro no Foreign Key jovem, Id errado')

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM pessoa WHERE ID={id}')
    cn.commit()

#salvar endereço
def salvar_endereco(cn, cr, logradouro, numero, complemento, bairro, cidade, cep):
    cr.execute(f"INSERT INTO endereco (logradouro, numero, complemento, bairro, cidade, cep)VALUES('{logradouro}', '{numero}','{complemento}', '{bairro}', '{cidade}', '{cep}')")
    cn.commit()

#alterar endereço
def alterar_endereco(cn, cr, id, logradouro, numero, complemento, bairro, cidade, cep):
    cr.execute(f"UPDATE endereco SET logradouro='{logradouro}', numero='{numero}', complemento='{complemento}', bairro='{bairro}', cidade='{cidade}' , cep='{cep}' WHERE ID={id}")
    cn.commit()

#deletar endereço por ID
def deletar_endereco(cn, cr, id):
    cr.execute(f'DELETE FROM endereco WHERE ID={id}')
    cn.commit()


# conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')

cursor=conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor, 'Dahlke')
# salvar(conexao, cursor, 'Voltolini', 'KingOfFlask', 16)
# alterar(conexao, cursor, 8, 'Gugu Voltolini', 'KingOfBasquete', 17, 5)
# deletar(conexao, cursor, 7)
salvar_endereco(conexao, cursor, 'Rua das Folhas', '111', 'Ap 305', 'Centro', 'Gaspar', '98851865')
# alterar_endereco(conexao, cursor, 5, 'Rua sem saida', '201', 'casa', 'Centro', 'Gaspar', '98851865')
# deletar_endereco(conexao, cursor, 6)


# like % -> busca determinado caracter  