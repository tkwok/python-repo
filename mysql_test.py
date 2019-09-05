import mysql.connector
from mysql.connector import errorcode
from python_mysql_dbconfig import read_db_config

def iterate_row(cursor, size=10):
  while True:
    rows = cursor.fetchmany(size)
    if not rows:
      break
    for row in rows:
      yield row

def connect():
  db_config = read_db_config()

  try:
    db_connection = mysql.connector.connect(**db_config)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM books")
    for row in iterate_row(cursor, 10):
      print(row)
    # rows = cursor.fetchall()
    # print('Total row(s) selected:', cursor.rowcount)
    # for row in rows:
      # print(row)
    # row = cursor.fetchone()
    # while row is not None:
    #   print(row)
    #   row = cursor.fetchone()

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print("Error".format(err))
  else:
    db_connection.close()

if __name__ == '__main__':
  connect()
