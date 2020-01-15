import MySQLdb

def listar_todos():
    #conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    comando_sql_select = "SELECT * FROM pessoa"
    cursor.execute(comando_sql_select)

    resultado = cursor.fetchall()
    return resultado
