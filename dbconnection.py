import pyodbc


class DatabaseCon:

  def __init__(self):
      self.conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "Server=TIGER05562;"
        "Database=goods_clearance;"
        "Trusted_Connection=yes;")
      self.cursor = self.conn.cursor()
