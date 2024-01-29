class Directories:
    @classmethod
    def MainPart1_Method(cls):
        import InitialiazeModels
        from Handler.FileHandler import FileHandler as FileHandler_Class;
        InitialiazeModels_Class = InitialiazeModels.InitialiazeModels;
        #FileHandler_Class = FileHandler;
        from Models import ImageProcessingDirectoriesModel

        systemModel = InitialiazeModels_Class.InitializeOperatingSystem();
        pythonDirectoriesModel = InitialiazeModels_Class.InitializePythonDirectoriesModel();
        machineLearningDirectoriesModel = InitialiazeModels_Class.InitializeMachineLearningDirectoriesModel(pythonDirectoriesModel.projectRoot);
        imageProcessingDirectoriesModel = InitialiazeModels_Class.InitializeImageProcessingDirectoriesModel(pythonDirectoriesModel.projectRoot);
        # directories given
        print("Desired models initialized, locations shown below");
        print("Main directory given: ");
        print(pythonDirectoriesModel.projectRoot);
        print("Machine learning directories given: ");
        for instance in machineLearningDirectoriesModel.allPaths:
            print(instance);

        print("Image processing directories given: ");
        for instance in imageProcessingDirectoriesModel.allPaths:
            print(instance);

        print("Checking folders integrity... ");
        FileHandler_Class.CheckDirectoryCollectionIntegrity(machineLearningDirectoriesModel.allPaths);
        FileHandler_Class.CheckDirectoryCollectionIntegrity(imageProcessingDirectoriesModel.allPaths);