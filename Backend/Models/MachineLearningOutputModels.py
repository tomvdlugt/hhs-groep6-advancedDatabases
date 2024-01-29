class MLD_OutputClassesModel:
    def __init__(self, trainedFileName: str, modelClassNames, loadedLearnedModel = None):
        self.trainedFileName = trainedFileName;    
        self.modelClassNames = ["Early_blight","Late_blight","healthy"];    
        self.loadedLearnedModel = loadedLearnedModel;

class MLD_OutputImageModel:
    def __init__(self, imagePath: str, imageNumpyArray = None, predictions = None):
        self.imagePath = imagePath;    
        self.imageTargetSize = (224, 224); 
        if(imageNumpyArray != None):
            self.imageNumpyArray = imageNumpyArray;  
        if(predictions != None):
            self.predictions = predictions;
        
