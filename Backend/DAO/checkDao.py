from databaseConnector import DatabaseConnector
from Models.checksModel import ChecksModel

class ChecksDao:
    def __init__(self, db_connector):
        self.db = db_connector
    
    def addCheck(self, checksModel:ChecksModel):
        query = "INSERT INTO dbo.checks (moment_of_check, healthy) VALUES (?, ?)"
        params = (checksModel.momentOfCheck, checksModel.healthy)
        self.db.executeQuery(query, params)