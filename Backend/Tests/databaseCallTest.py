from databaseConnector import DatabaseConnector
from Models.checksModel import ChecksModel
from DAO.checkDao import ChecksDao

db = DatabaseConnector()
db.connect()
checks_dao = ChecksDao(db)


check = ChecksModel('1997-10-24', True)
check = ChecksModel('2023-10-24', False)

checks_dao.addCheck(check)
# print(check.momentOfCheck)
# checkDao = ChecksDao()
# checkDao.addCheck(check)


