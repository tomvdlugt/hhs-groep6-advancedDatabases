from databaseConnector import DatabaseConnector
from checksModel import ChecksModel

class ChecksDao:
    def __init__(self):
        self.db = DatabaseConnector
    
    def addCheck(self, checksModel:ChecksModel):
        query = f"INSERT INTO users (name, email) VALUES ({checksModel.momentOfCheck}, {checksModel.healthy})"
        self.db.executeQuery(query)