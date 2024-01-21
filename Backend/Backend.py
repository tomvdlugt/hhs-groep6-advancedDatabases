
# This is the main, before the program is going to run, it will check all the variables given.

# Check where the program is stored, the FileHandler is to be used to determin file positions aswell
# In short: It will make the folders on startup and assign images properly when given.
from Handler.FileHandler import FileHandler
FileHandler.CheckDirectoryIntegrity();

