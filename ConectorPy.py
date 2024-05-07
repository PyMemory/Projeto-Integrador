from mysql.connector import connect

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

connection = mysql_connection('pi-2024-omateocortez.c.aivencloud.com','avnadmin',
                            'AVNS_mSrmiLQWmgRL7sxRVJ2', 'defaultdb')
