#!/usr/bin/python3
import mysql.connector

class DatabaseConnection:
  def __init__(self, host='localhost', user='root', password='root', database='ALX_prodev'):
        """
        Initialize with database connection parameters.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None


  def __enter__(self):
    """
      connect to database to perform the queries
    """
    self.connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.database
    )

    return self.connection
  

  def __exit__(self, exc_type, exc_value, traceback):
    """
      close the connection
    """
    self.connection.close()


with DatabaseConnection() as d:
  cursor = d.cursor()
  cursor.execute('SELECT * FROM user_data')
  result = cursor.fetchall()
  for row in result:
    print(row)
  cursor.close()
