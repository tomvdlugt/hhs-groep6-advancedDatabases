
# import sys
# import os
from Backend.databaseConnector import DatabaseConnector
from Backend.Models.checksModel import ChecksModel
from Backend.DAO.checkDao import ChecksDao
# from Models import checksModel
# from DAO import checkDao
# # Get the current script's directory
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # Add the directories containing your modules to sys.path
# sys.path.insert(0, os.path.join(current_dir, 'Backend', 'Models'))
# sys.path.insert(0, os.path.join(current_dir, 'Backend', 'DAO'))

# print(f"Path: {sys.path}")


# from checksModel import ChecksModel
# from checkDao import ChecksDao

db = DatabaseConnector()
db.connect()
checks_dao = ChecksDao(db)


check = ChecksModel('1997-10-24', True)
check = ChecksModel('2023-10-24', False)

checks_dao.addCheck(check)
# print(check.momentOfCheck)
# checkDao = ChecksDao()
# checkDao.addCheck(check)


