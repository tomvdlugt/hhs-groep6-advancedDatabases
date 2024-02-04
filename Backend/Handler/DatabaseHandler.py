"""
Connects to a SQL database using pyodbc
Make sure ODBC 18 is installed
""" 
import pyodbc


class DatabaseConnector:
    def __init__(self):
        from AppSettings.ConnectionStrings import USERNAME, PASSWORD
        self.SERVER = 'groep6server.database.windows.net'
        self.DATABASE = 'PlantenZiektenHerkenner'
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.DRIVER= '{ODBC Driver 18 for SQL Server}'
        self.conn = None

    def connect_test(self, userNameGiven: str, passwordGiven: str, databaseGiven: str):
        try:
            self.conn = pyodbc.connect(f'DRIVER={self.DRIVER};SERVER={self.SERVER};'
                                        f'DATABASE={databaseGiven};UID={userNameGiven};PWD={passwordGiven}')
            print("Connected to the database")
            return True;
        except Exception as e:
            print(f'Error connecting to the database: {e}')
            return False;

    def connect(self):
        if not self.conn:
            try:
                self.conn = pyodbc.connect(f'DRIVER={self.DRIVER};SERVER={self.SERVER};'
                                           f'DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD}')
                print("Connected to the database")
                return True;
            except Exception as e:
                print(f'Error connecting to the database: {e}')
                return False;

    def connect(self):
        if not self.conn:
            try:
                self.conn = pyodbc.connect(f'DRIVER={self.DRIVER};SERVER={self.SERVER};'
                                           f'DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD}')
                print("Connected to the database")
                return True;
            except Exception as e:
                print(f'Error connecting to the database: {e}')
                return False;

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed")
    

    def executeReadQuery(self, query, params=None):
        # This query will read, not insert new values or create new tables
        # If you do that, then the cursor.fetchall will crash
        if not self.conn:
            print("Not connected to the db")
            return;
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query, params) if params else cursor.execute(query)
                for row in cursor.fetchall():
                    #todo 
                    #expand with proper log files  
                     print(row);
                self.conn.commit()
                print("Query executed successfully")
            except Exception as e:
                print(f"Error executing the query: {e}")
                self.conn.rollback()
                
    def executeQuery(self, query, params=None):
        if not self.conn:
            print("Not connected to the db")
            return False;
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query, params) if params else cursor.execute(query)
                self.conn.commit()
                print("Query executed successfully")
                return True;
            except Exception as e:
                print(f"Error executing the query: {e}")
                self.conn.rollback()
                return False;
        