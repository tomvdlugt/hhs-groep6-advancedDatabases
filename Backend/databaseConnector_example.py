"""
Connects to a SQL database using pyodbc
""" 
import pyodbc
SERVER = 'groep6server.database.windows.net'
DATABASE = 'PlantenZiektenHerkenner'
USERNAME = '<username>'
PASSWORD = '<password>'
DRIVER= '{ODBC Driver 18 for SQL Server}'

connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

def connect(self):
            if not self.conn:
                try:
                    self.conn = pyodbc.connect(f'DRIVER={self.DRIVER};SERVER={self.SERVER};'
                                            f'DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD}')
                    print("Connected to the database")
                except Exception as e:
                    print(f'Error connecting to the database: {e}')

def close(self):
    if self.conn:
        self.conn.close()
        print("Connection closed")
    
def executeQuery(self, query, params=None):
    if not self.conn:
        print("Not connected to the db")
        return;

    with self.conn.cursor() as cursor:
        try:
            cursor.execute(query, params) if params else cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully")
        except Exception as e:
            print(f"Error executing the query: {e}")
            self.conn.rollback()
        