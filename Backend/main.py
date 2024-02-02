#import Models.SystemModel
from InitialzeHandlers.MainPart1_Directories import Directories;
from InitialzeHandlers.MainPart2_TrainTheModel import TrainTheModel;
from InitialzeHandlers.MainPart4_ProcessGivenImages import ProcessImages;
Directories.MainPart1_Method();
ProcessImages.MainPart4_Method_CheckIncoming();
#TrainTheModel.MainPart2_Method
from Handler.FileHandler import FileHandler as FileHandler_Class; ## required to parse out proper directory
# load mainpart 3 = trained model
# load image model
from Models.ImageModels import NewImageModel, ALLOWEDEXTENSIONS, ALLOWEDBACKENDEXTENSIONS
incomingFileDirectory = FileHandler_Class.ParseDirectoryPath("D:/Projects_D/S5_Groep6/PlantenHerkenning/Backend/Images/Incoming/");

#testImages
incomingFileName = "PotatoEarlyBlight1.JPG";
incomingFileName_2 = "PotatoEarlyBlight2.JPG";
#incomingFileNameImproper = "PotatoEarlyBlight1.exe";

givenImageArray = [incomingFileName, incomingFileName_2]

for arrayFileInstance in givenImageArray:
    fileAccepted = False;
    for givenExtension in ALLOWEDEXTENSIONS:
       if(arrayFileInstance[arrayFileInstance.find("."):].lower().replace(".","") == givenExtension):
          fileAccepted = True;
          break;

    if not fileAccepted:
       print("Possible malicious filetype detected, breaking off run to protect the system.");
       FileHandler_Class.RemoveFile(incomingFileDirectory+arrayFileInstance)
       raise Exception(f"Given file for the model is not allowed, removed the file prematurely. Filename that was given: {arrayFileInstance}");
# Checking files complete, proceed to connect to the Database 
from databaseConnector import DatabaseConnector;
from DAO.checkDao import ChecksDao
connection_Class = DatabaseConnector(); 
connection_Class.connect();
checksDao_Class = ChecksDao(connection_Class)
print("")
print("Before processing the files");
print("");
connection_Class.executeReadQuery("select * from dbo.UploadedImages");
print("");
# Process the new files    
#createDevelopTable = "Create TABLE UploadedImages (";
#createDevelopTable = createDevelopTable + "imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255), uuidName  varchar(255), extension varchar(10), ";
#createDevelopTable = createDevelopTable + "healthy int, plant_disease  varchar(255), uploadDate  datetime,  processedDate  datetime null);";
#connection_Class.executeQuery(createDevelopTable);


#stap 3
for arrayFileInstance in givenImageArray:
    from Models.ImageModels import NewImageModel
    newImageModel = FileHandler_Class.MoveIncommingToProcessed(arrayFileInstance);
    insertIntoImages = f"INSERT INTO UploadedImages (originalName, uuidName, extension, healthy, plant_disease, uploadDate)";
    insertIntoImages = f"{insertIntoImages}VALUES('{newImageModel.originalName}','{newImageModel.uuidName}',";
    insertIntoImages = f"{insertIntoImages}'{newImageModel.extension}','{newImageModel.healthy}',";
    insertIntoImages = f"{insertIntoImages}'{newImageModel.plant_disease}',GetDate())";
    connection_Class.executeQuery(insertIntoImages);
    

print("")
print("Before processing the files");
print("");
connection_Class.executeReadQuery("select * from dbo.UploadedImages");
print("");

# Connect to the database
# can we put this in the MainPart3?




#connection.executeQuery("select * from [dbo].[checks]");
#connection.executeQuery("Create TABLE Images( imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255) , uuidName  varchar(255), extension varchar(10), disease  varchar(255), uploadDate  datetime, processedDate  datetime null);");
#connection.executeQuery("Create TABLE Images( imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255) , uuidName  varchar(255), extension varchar(10), disease  varchar(255), uploadDate  datetime, processedDate  datetime null);");
insertIntoImages = "INSERT INTO Images (originalName, uuidName, extension, disease, uploadDate, processedDate)";
insertIntoImages = insertIntoImages + "VALUES ('TestImage.jpg', 'banaanuid', 'jpg', 'Blight_Early', GetDate(), NULL);"
connection_Class.executeQuery(insertIntoImages);





# Retrieve Initialize models
from InitialiazeModels import InitialiazeModels as InitialiazeModels_Class
pythonDirectoriesModel = InitialiazeModels_Class.InitializePythonDirectoriesModel();
machineLearningDirectoriesModel = InitialiazeModels_Class.InitializeMachineLearningDirectoriesModel(pythonDirectoriesModel.projectRoot);

# Get trained model
from Models.MachineLearningOutputModels import MLD_OutputClassesModel, MLD_OutputImageModel;

# Load the pre-trained model
from tensorflow.keras.models import load_model
#from keras.models import load_model
trainedModel_Class = MLD_OutputClassesModel;
trainedModelFile = trainedModel_Class(FileHandler_Class.ParseDirectoryPath(pythonDirectoriesModel.projectRoot + "\\trainedModel\\trained_modelsplantDiseaseRecognitionModel30012024_200549.h5"), ['Early_blight', 'Late_blight', 'healthy']);
loadedModel = load_model(trainedModelFile.trainedFileName);
trainedModelFile.loadedLearnedModel = loadedModel;

# Load target model base
trainedModelImage_1 = MLD_OutputImageModel;
trainedModelImage_1 = trainedModel_Class(FileHandler_Class.ParseDirectoryPath(machineLearningDirectoriesModel.valid_path + "/Potato___Late_blight/0b2bdc8e-90fd-4bb4-bedb-485502fe8a96___RS_LB 4906.JPG"));
# Process target model
import numpy
from keras.preprocessing import image
trainedModelImage_1 = trainedModel_Class(trainedModelImage_1.trainedFileName, image.load_img(trainedModelImage_1.trainedFileName, target_size=trainedModelImage_1.imageTargetSize))
tMI_1_predictions = image.img_to_array(trainedModelImage_1.imageNumpyArray);
tMI_1_predictions = np.expand_dims(trainedModelImage_1.imageNumpyArray);
tMI_1_predictions /= 255.

tMI_1_predictions = trainedModelFile.pr

trainedModelImage_1 = trainedModel_Class(trainedModelImage_1.trainedFileName,trainedModelImage_1.imageNumpyArray)


# Load

from keras.preprocessing import image
import numpy as np



# Janked this scheduler from tutorialspoint
# https://www.tutorialspoint.com/python/python_thread_scheduling.htm
import sched
from datetime import datetime
import time

#jobs testing
def addition(a,b):
   print("Performing Addition : ", datetime.now())
   print("Time : ", time.monotonic())
   print("Result : ", a+b)

s = sched.scheduler()

print("Start Time : ", datetime.now())

event1 = s.enter(10, 1, addition, argument = (5,6))
print("Event Created : ", event1)
s.run()
print("End Time : ", datetime.now())

# newmodel testing
from datetime import datetime
from Models.ImageModels import NewImageModel
newImageIncoming = NewImageModel("abc", "ghi","jkl", 1)
newImageIncoming2 = NewImageModel("abc", "ghi","jkl", 1, datetime.now())

#print(newImageIncoming.giventime)
print(newImageIncoming2.giventime)

import os
import glob
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
import keras as keras
msg = "hello me"
print(msg)
print(msg)

print(keras.__version__)
print(msg)
print(tf.__version__)



print(msg)