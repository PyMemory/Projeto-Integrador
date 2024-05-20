import mysql.connector

def mysql_connection(host, user, passwd, port, database=None):
    connection = mysql.connector.connect(
        host = host,
        user = user,
        passwd = passwd,
	      port = port,
        database = database
    )
    return connection

connection = mysql_connection('pi-2024-omateocortez.c.aivencloud.com','avnadmin',
                            'AVNS_mSrmiLQWmgRL7sxRVJ2', '22705', 'defaultdb')
