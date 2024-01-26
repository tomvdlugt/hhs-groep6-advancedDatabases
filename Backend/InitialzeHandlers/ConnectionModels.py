class ConnectionDatabaseModel:
    def __init__(self, SERVER, DATABASE, DRIVER, conn):
        self.SERVER = SERVER;
        self.DATABASE = DATABASE;
        self.DRIVER = DRIVER;
        self.conn = conn;

class ConnectionUserModel:
    def __init__(self, USERNAME, PASSWORD):
        self.USERNAME = USERNAME;
        self.PASSWORD = PASSWORD;