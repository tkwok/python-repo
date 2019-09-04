import mysql.connector
from mysql.connector import errorcode
from python_mysql_dbconfig import read_db_config

def connect():
  db_config = read_db_config()

  try:
    db_connection = mysql.connector.connect(**db_config)

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    print("Database connected successfully")
    db_connection.close()

if __name__ == '__main__':
  connect()
