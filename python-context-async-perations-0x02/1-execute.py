#!/usr/bin/python3
import mysql.connector


class ExecuteQuery:
  def __init__(
      self,
      query='SELECT * FROM users WHERE age > %s',
      params=(25,),
      host='localhost',
      user='root',
      password='root',
      database='alx_prodev',
  ):
    """
      create the constructor
    """
    self.query = query
    self.params = params
    self.connection = None
    self.cursor = None
    self.host = host
    self.user = user
    self.password = password
    self.database = database

  def __enter__(self):
    """
      create the context manager enterance
    """
    self.connection = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.database
    )
    self.cursor = self.connection.cursor()
    return self
  
  def execute(self):
    """
    execute the command and return the result
    """
    self.cursor.execute(self.query, self.params)
    result = self.cursor.fetchall()
    return result
  
  def __exit__(self, exc_type, exc_value, traceback):
    """
      close the context manager
    """
    self.cursor.close()
    self.connection.close()

with ExecuteQuery() as e:
  results = e.execute()
  for result in results:
    print(result)
