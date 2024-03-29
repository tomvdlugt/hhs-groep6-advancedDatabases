from fileinput import filename
from msilib.schema import File
from os import replace


class FileHandler:
    @classmethod
    def CheckDirectoryIntegrity(cls):
        import os;
        import platform;

        # This class is meant to publicly build the used paths for the code.
        # Think of it as global variables, but one that allows the project to be launched
        # from any chosen directory.
        # This should be essential to the functions of the program.

        projectRoot = str(os.getcwd());
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
        cls.CreateFolder(mainImagesPath, "Images");
        cls.CreateFolder(rawImagesPath, "Incoming");
        cls.CreateFolder(processedImagesPath, "Processed");
        cls.CreateFolder(trainedImagesPath, "Trained");
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
            case _:
                print("operatingSystem: unknown, hopping the default path is good.\n\tDetected operating system: " + operatingSystem);
                return givenPath;
        
    def CreateFolder(path, folderName):
        import os;
        import platform;
        if(os.path.exists(path)):
            print(f"Folder {folderName} exists, stopping any further actions.");
        else:
             print(f"Folder {folderName} did not exist, creating new folder");
             os.mkdir(path);
             print("Folder created");
    
    @classmethod
    def PlaceIncoming(cls):
        import os;
        import platform;
        import uuid;

        print(uuid.uuid4());

    @classmethod
    def MoveIncommingToProcessed(cls, fileName):
        #TODO
        # Instead of receiving images from the root folder, get them from incoming
        import os; 
        import shutil;
        projectRoot = str(os.getcwd());
        currentFilePath = cls.ParseDirectoryPath(projectRoot + "\\Images\\Incoming\\" + fileName);
        fileName = cls.GenerateUid() + fileName[fileName.find("."):];
        desiredFilePath = cls.ParseDirectoryPath(projectRoot + "\\Images\\Processed\\" + fileName);

        # Rename and place the file in the desired path.
        os.rename(currentFilePath, desiredFilePath)

    @classmethod
    def GenerateUid(cls):
        import os;
        import platform;
        import uuid;

        generatedUid = uuid.uuid4();
        print(generatedUid);
        return str(generatedUid);
    
    @classmethod
    def MoveFile(cls):
        import os;
        import platform;
        import uuid;

        print(uuid.uuid4());

            

# can't create function map until class has been created
FileHandler.function_map = {
    "CheckDirectoryIntegrity": FileHandler.CheckDirectoryIntegrity
}

if __name__=='__main__':
    functionList = {'CheckDirectoryIntegrity':True}