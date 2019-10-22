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
    # for row in iterate_row(cursor, 10):
    #   print(type(row))
    wrapStringInHTML("python-output", "https://www.google.com", iterate_row(cursor, 10))

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print("Error".format(err))
  else:
    db_connection.close()

def wrapStringInHTML(program, url, body):
  import datetime
  from webbrowser import open_new_tab

  now = datetime.datetime.today().strftime("%Y/%m/%d-%H%:M:%S")
  filename = program + '.html'
  f = open(filename,'w')

  for row in body:
    content = "<li id='listitem clearfix'><div class='listitem_data'>{}</div><div class='listitem_task'>{}</div></li>".format(row[0], row[1])
    print(content)

  wrapper = """<html>
  <head>
  <title>%s output - %s</title>
  <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body><p>URL: <a href=\"%s\">%s</a></p>
  <ul id="sortable_list">
    <li id="listitem clearfix header">
      <div class="listitem_data">Title</div>
      <div class="listitem_task">Pages</div>
    </li>
  %s
  </ul>
  </body>
  </html>"""

  whole = wrapper % (program, now, url, url, content)
  f.write(whole)
  f.close()

  filename = 'file:///Users/tk/Documents/Github/python-repo/' + filename
  open_new_tab(filename)

if __name__ == '__main__':
  connect()
