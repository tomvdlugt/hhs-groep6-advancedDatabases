from re import S


class ImageProcessingDirectoriesModel:
    def __init__(self, mainImagesPath, rawImagesPath, processedImagesPath, trainedImagesPath):
        self.mainImagesPath = mainImagesPath;
        self.rawImagesPath = rawImagesPath;
        self.processedImagesPath = processedImagesPath;
        self.trainedImagesPath = trainedImagesPath;
        self.allPaths = {mainImagesPath,
                          rawImagesPath, 
                          processedImagesPath, 
                          trainedImagesPath};