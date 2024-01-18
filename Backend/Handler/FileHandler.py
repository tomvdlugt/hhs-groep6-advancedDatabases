class FileHandler:
    from Config.config import rootDirectory_path
    import platform;
    operatingSystem = platform.system();
    
    @classmethod
    def CheckDirectoryIntegrity(cls):
        # This class is meant to publicly build the used paths for the code.
        # Think of it as global variables, but one that allows the project to be launched
        # from any chosen directory.
        # This should be essential to the functions of the program.
        print("operatingSystem: " + cls.operatingSystem);
        print("project root given: " + cls.rootDirectory_path);
        
        mainImagesPath = cls.ParseDirectoryPath(cls.rootDirectory_path + "\\Images");
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
        # return the givenPath with the correct directory divider
        match cls.operatingSystem:
            case "Windows":
                return givenPath.replace("/", "\\");
            case "Mac":
                return givenPath.replace("\\", "/"); 
            case "Darwin":
                return givenPath.replace("\\", "/");
            case _:
                print("operatingSystem: unknown, hopping the default path is good.\n\tDetected operating system: " + operatingSystem);
                return givenPath;
        
    def CreateFolder(path, folderName):
        import os;
        if(os.path.exists(path)):
            print(f"Folder {folderName} exists, stopping any further actions.");
        else:
             print(f"Folder {folderName} did not exist, creating new folder");
             os.mkdir(path);
             print("Folder created");
    
    @classmethod
    def PlaceIncoming(cls):
        import uuid;
        print(uuid.uuid4());

    @classmethod
    def MoveIncommingToProcessed(cls, fileName):
        #TODO
        # Instead of receiving images from the root folder, get them from incoming
        import os; 
        currentFilePath = cls.ParseDirectoryPath(cls.rootDirectory_path + "\\Images\\Incoming\\" + fileName);
        fileName = cls.GenerateUid() + fileName[fileName.find("."):];
        desiredFilePath = cls.ParseDirectoryPath(cls.rootDirectory_path + "\\Images\\Processed\\" + fileName);

        # Rename and place the file in the desired path.
        os.rename(currentFilePath, desiredFilePath)

    @classmethod
    def GenerateUid(cls):
        import uuid;

        generatedUid = uuid.uuid4();
        print(generatedUid);
        return str(generatedUid);

            

# can't create function map until class has been created
FileHandler.function_map = {
    "CheckDirectoryIntegrity": FileHandler.CheckDirectoryIntegrity
}

if __name__=='__main__':
    functionList = {'CheckDirectoryIntegrity':True}