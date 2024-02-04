# Models import
import Models.PythonDirectoriesModel;
import Models.MachineLearningDirectoriesModel;
import Models.ImageProcessingDirectoriesModel;

# Python Import
#import Handler.FileHandler as FileHandler_Class
from Handler.FileHandler import FileHandler as FileHandler_Class

## Note: This is a initializer, don't use it inbetween otherwise there will be dependency issues
## It will collect all the paths and set them into proper models, allowing easier changes to be made
class InitialiazeModels:
    @classmethod
    def InitializePythonDirectoriesModel(cls):
        import os;
        rootGiven = FileHandler_Class.ParseDirectoryPath(os.getcwd());
        return Models.PythonDirectoriesModel.PythonDirectoriesModel(rootGiven);

    @classmethod
    def InitializeMachineLearningDirectoriesModel(cls, projectRoot):
        train_directory = FileHandler_Class.ParseDirectoryPath(f"{projectRoot}/MachineLearningModel/input/new_plant_diseases_dataset");
        train_path = FileHandler_Class.ParseDirectoryPath(train_directory + "/train");
        valid_path = FileHandler_Class.ParseDirectoryPath(train_directory + "/valid");
        test_path = FileHandler_Class.ParseDirectoryPath(train_directory + "/test");
        trained_models = FileHandler_Class.ParseDirectoryPath(train_directory + "/trained_models");
        return Models.MachineLearningDirectoriesModel.MachineLearningDirectoriesModel(train_directory, train_path, valid_path, test_path, trained_models);

    @classmethod
    def InitializeImageProcessingDirectoriesModel(cls, projectRoot):
        mainImagesPath = FileHandler_Class.ParseDirectoryPath(projectRoot + "\\Images");
        rawImagesPath = FileHandler_Class.ParseDirectoryPath(mainImagesPath + "\\Incoming");
        processedImagesPath = FileHandler_Class.ParseDirectoryPath(mainImagesPath + "\\Processed");
        trainedImagesPath = FileHandler_Class.ParseDirectoryPath(mainImagesPath + "\\Trained");
        return Models.ImageProcessingDirectoriesModel.ImageProcessingDirectoriesModel(mainImagesPath, rawImagesPath, processedImagesPath, trainedImagesPath);