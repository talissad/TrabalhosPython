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

# conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')

cursor=conexao.cursor()

# listar_todos(cursor)
buscar_por_id(cursor, 3)