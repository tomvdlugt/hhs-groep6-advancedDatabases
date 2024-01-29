#import Models.SystemModel
from InitialzeHandlers.MainPart1_Directories import Directories;
from InitialzeHandlers.MainPart2_TrainTheModel import TrainTheModel;
Directories.MainPart1_Method();
#TrainTheModel.MainPart2_Method
# load mainpart 3 = trained model




# Connect to the database
# can we put this in the MainPart3?
from databaseConnector import DatabaseConnector;
from DAO.checkDao import ChecksDao
connection_Class = DatabaseConnector(); #trigger the __init__(self)
connection_Class.connect();
checksDao_Class = ChecksDao(connection_Class)
# Retrieve Initialize models
import InitialiazeModels
InitialiazeModels_Class = InitialiazeModels.InitialiazeModels;
pythonDirectoriesModel = InitialiazeModels_Class.InitializePythonDirectoriesModel();
machineLearningDirectoriesModel = InitialiazeModels_Class.InitializeMachineLearningDirectoriesModel(pythonDirectoriesModel.projectRoot);

# Get trained model
from Models.MachineLearningOutputModels import MLD_OutputClassesModel, MLD_OutputImageModel;
from Handler.FileHandler import FileHandler as FileHandler_Class; ## required to parse out proper directory
# Load the pre-trained model
from tensorflow.keras.models import load_model
#from keras.models import load_model
trainedModel_Class = MLD_OutputClassesModel;
trainedModelFile = trainedModel_Class(FileHandler_Class.ParseDirectoryPath(pythonDirectoriesModel.projectRoot + "/trainedModel/plantDiseaseRecognitionModel28012024_123422.h5"), ['Early_blight', 'Late_blight', 'healthy']);
loadedModel = load_model(trainedModelFile.trainedFileName);
trainedModelFile.loadedLearnedModel = loadedModel;

# Load target model base
trainedModelImage_1 = MLD_OutputImageModel;
trainedModelImage_1 = trainedModel_Class(FileHandler_Class.ParseDirectoryPath(machineLearningDirectoriesModel.valid_path + "/Potato___Late_blight/1f560f09-0b70-40c9-b907-4cac9ba47b8d___RS_LB 3184.JPG"));
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














#connection.executeQuery("select * from [dbo].[checks]");
#connection.executeQuery("Create TABLE Images( imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255) , uuidName  varchar(255), extension varchar(10), disease  varchar(255), uploadDate  datetime, processedDate  datetime null);");
#connection.executeQuery("Create TABLE Images( imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255) , uuidName  varchar(255), extension varchar(10), disease  varchar(255), uploadDate  datetime, processedDate  datetime null);");
insertIntoImages = "INSERT INTO Images (originalName, uuidName, extension, disease, uploadDate, processedDate)";
insertIntoImages = insertIntoImages + "VALUES ('TestImage.jpg', 'banaanuid', 'jpg', 'Blight_Early', GetDate(), NULL);"
connection_Class.executeQuery(insertIntoImages);




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