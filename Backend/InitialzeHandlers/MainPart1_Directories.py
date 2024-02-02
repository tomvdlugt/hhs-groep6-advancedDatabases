from AppSettings.AppSettings import ROOTPATH, DATAFOLDER, IMAGESFOLDER, INCOMINGFOLDER, CHECKEDFOLDER, PROCESSEDFOLDER

allPaths = {DATAFOLDER, IMAGESFOLDER, INCOMINGFOLDER, CHECKEDFOLDER, PROCESSEDFOLDER}





class Directories:
    @classmethod
    def MainPart1_Method(cls):
        from Handler.FileHandler import FileHandler as FileHandler_Class;
        print("Main directory given: " + ROOTPATH);
        print("Checking DataFolder Structure...")
        FileHandler_Class.CheckDirectoryCollectionIntegrity(allPaths);
        print("DataFolder Checking complete.")
