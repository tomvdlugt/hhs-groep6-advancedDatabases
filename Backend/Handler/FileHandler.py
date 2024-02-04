"""
Do not use AppSettings within the FileHandler
The AppSettings need the FileHandler to initialize propper paths
But
using those paths here will create circular imports, causing memory leaks.
""" 
class FileHandler:
    #from Global.config import GlobalConfig;
    #print(GlobalConfig.projectRoot);
    @classmethod
    def GetProjectRoot(cls):
        import os;
        return str(os.getcwd());

    @classmethod
    def CheckDirectoryCollectionIntegrity(cls, givenCollection):
        for directory in givenCollection:
            cls.CreateFolderWithName(directory);
    
    @classmethod
    def CheckDirectoryIntegrity(cls):
        

        from Global.config import projectRoot;
        from Global.config import GlobalConfig;
        

        import os;
        import platform;

        # This class is meant to publicly build the used paths for the code.
        # Think of it as global variables, but one that allows the project to be launched
        # from any chosen directory.
        # This should be essential to the functions of the program.

        projectRoot = str(os.getcwd());
        projectRoot = GlobalConfig.base_directory;
        
        operatingSystem = platform.system();
        print("operatingSystem: " + operatingSystem);
        print("project root given: " + projectRoot);
        
        mainImagesPath = cls.ParseDirectoryPath(projectRoot + "\\Images");
        rawImagesPath = cls.ParseDirectoryPath(mainImagesPath + "\\Incoming");
        processedImagesPath = cls.ParseDirectoryPath(mainImagesPath + "\\Processed");
        trainedImagesPath = cls.ParseDirectoryPath(mainImagesPath + "\\Trained");

        # can be improved with a double string array foreach loop
        # But I am disinclined to do that for now.
        # Start creating folders in the desired directories.
        cls.CreateFolderWithName(mainImagesPath, "Images");
        cls.CreateFolderWithName(rawImagesPath, "Incoming");
        cls.CreateFolderWithName(processedImagesPath, "Processed");
        cls.CreateFolderWithName(trainedImagesPath, "Trained");
        # End creating folders in the desired directories.

        # Import newly available trained files

        # Import incoming images from query

    @classmethod
    def ParseDirectoryPath(cls, givenPath):
        import os;
        import platform;
        projectRoot = str(os.getcwd());
        operatingSystem = platform.system();

        # return the givenPath with the correct directory divider
        match operatingSystem:
            case "Windows":
                return givenPath.replace("/", "\\");
            case "Mac":
                return givenPath.replace("\\", "/"); 
            case "Darwin":
                return givenPath.replace("\\", "/");
            case _:
                print("operatingSystem: unknown, hopping the default path is good.\n\tDetected operating system: " + operatingSystem);
                return givenPath;
        
    def CreateFolderWithName(path: str, folderName: str = 'NoneGiven'):
        import os;
        import platform;
        if(os.path.exists(path)):
            print(f"Folder {folderName} exists, stopping any further actions.");
        else:
             print(f"Folder {folderName} did not exist, creating new folder");
             os.mkdir(path);
             print("Folder created");

    @classmethod
    def MoveFileToFolder(cls, currentFolderPath: str, desiredFolderPath: str, fileName: str, newFileName: str):
        import os; 
        currentFolderPath = cls.ParseDirectoryPath(currentFolderPath + "/" + fileName);
        desiredFolderPath = cls.ParseDirectoryPath(desiredFolderPath + "/" + fileName);
        os.rename(currentFolderPath, desiredFolderPath)
        


    @classmethod
    def MoveIncommingToProcessed(cls, fileName):
        #TODO
        # Instead of receiving images from the root folder, get them from incoming
        import os; 
        import shutil;
        newName = cls.GenerateUid();
        from Models.ImageModels import CheckedImageModel
        from datetime import datetime
        newImageModel = CheckedImageModel(fileName, newName, fileName[fileName.find("."):], 0, "InReview", datetime.now())
        
        

        
        # the actual moving and renaming
        projectRoot = str(os.getcwd());
        currentFilePath = cls.ParseDirectoryPath(projectRoot + "\\Images\\Incoming\\" + fileName);
        fileName = newName + fileName[fileName.find("."):];
        desiredFilePath = cls.ParseDirectoryPath(projectRoot + "\\Images\\Processed\\" + fileName);
        # Rename and place the file in the desired path.
        os.rename(currentFilePath, desiredFilePath)
        
        cls.MoveFileToFolder()
        return newImageModel;

    """
    Use the values assigned within the AppSettings.
    """
    @classmethod
    def MoveIncommingToChecked(cls, fileName, incomingFolderPath, checkedFolderPath):
        newName = cls.GenerateUid();
        givenExtension = fileName[fileName.find("."):];
        from Models.ImageModels import CheckedImageModel
        from datetime import datetime
        newImageModel = CheckedImageModel(fileName, newName, givenExtension, 0, "InReview")
        
        newFileName = newName + givenExtension;
    
        cls.MoveFileToFolder(incomingFolderPath, checkedFolderPath, fileName, newFileName);
        
        return newImageModel;

    @classmethod
    def RemoveFile(cls, fileName: str):
        import os; 
        os.remove(fileName);
        
    @classmethod
    def GenerateUid(cls):
        import uuid;
        generatedUid = uuid.uuid4();
        print("GeneratedUUID: " + generatedUid);
        return str(generatedUid);
    
    @classmethod
    def MoveFile(cls):
        import os;
        import platform;
        import uuid;

        print(uuid.uuid4());

    @classmethod
    def GetAllFilesInDirectory(cls, filePath):
        import os;
        return os.listdir(filePath)
    
    @classmethod
    def CheckIfFileInDirectory(cls, filePath):
        import os;
        return os.listdir(filePath)

            

# can't create function map until class has been created
FileHandler.function_map = {
    "CheckDirectoryIntegrity": FileHandler.CheckDirectoryIntegrity
}

if __name__=='__main__':
    functionList = {'CheckDirectoryIntegrity':True}