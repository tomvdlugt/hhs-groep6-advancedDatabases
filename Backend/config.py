"""
Connects to a SQL database using pyodbc
Make sure ODBC 18 is installed
""" 
import pyodbc


class DatabaseConnector:
    def __init__(self):
        self.SERVER = 'groep6server.database.windows.net'
        self.DATABASE = 'PlantenZiektenHerkenner'
        self.USERNAME = 'tom_cielo@groep6server'
        self.PASSWORD = 'Scoerabi294979!'
        self.DRIVER= '{ODBC Driver 18 for SQL Server}'
        self.conn = None

    def connect(self):
        if not self.conn:
            try:
                self.connect = pyodbc.connect(f'DRIVER={self.DRIVER};SERVER={self.SERVER};'
                                           f'DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD}')
            except Exception as e:
                print(f'Error: {e}')

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed")
