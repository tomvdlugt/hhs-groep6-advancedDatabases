
import sys
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the directories containing your modules to sys.path
sys.path.insert(0, os.path.join(current_dir, 'Backend', 'Models'))
sys.path.insert(0, os.path.join(current_dir, 'Backend', 'DAO'))

print(f"Path: {sys.path}")


# from checksModel import ChecksModel
# from checkDao import ChecksDao

# check = ChecksModel("24-10-1997", True)
# print(check.momentOfCheck)
# checkDao = ChecksDao()
# checkDao.addCheck(check)


