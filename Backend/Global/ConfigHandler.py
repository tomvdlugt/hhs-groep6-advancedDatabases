class ConfigHandler:
    @classmethod
    def GetOperatingSystem(cls):
        import platform;
        operatingSystem = platform.system();

    @classmethod
    def ParseDirectoryPath(cls, givenPath, operatingSystem):
        # return the givenPath with the correct directory divider
        operatingSystem = cls.GetOperatingSystem();
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

    @classmethod
    def CheckDirectoryIntegrity(cls):

        from Global.Config import projectRoot;
        from Global.Config import GlobalConfig;
        

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
        cls.CreateFolder(mainImagesPath, "Images");
        cls.CreateFolder(rawImagesPath, "Incoming");
        cls.CreateFolder(processedImagesPath, "Processed");
        cls.CreateFolder(trainedImagesPath, "Trained");
        # End creating folders in the desired directories.

        # Import newly available trained files

        # Import incoming images from query

    @classmethod
    def CheckDirectoryIntegrity(cls, givenDirectoryCollection):
        from Handler.FileHandler import FileHandler;
        for directoryGiven in givenDirectoryCollection:
            print(directoryGiven);