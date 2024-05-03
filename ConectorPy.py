from mysql.connector import connect

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

connection = mysql_connection('host','root', 'passwd', 'database')

query = '''
'''

cursor = connection.cursor()
cursor.execute(query)