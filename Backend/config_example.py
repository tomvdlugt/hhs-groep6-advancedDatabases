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

conn = pyodbc.connect(connectionString)
print(conn)