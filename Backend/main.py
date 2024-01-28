#import Models.SystemModel
from InitialzeHandlers.MainPart1_Directories import Directories;
from InitialzeHandlers.MainPart2_TrainTheModel import TrainTheModel;
Directories.MainPart1_Method();
#TrainTheModel.MainPart2_Method


# Connect to the database
# can we put this in the MainPart3?
from databaseConnector import DatabaseConnector;
connection = DatabaseConnector(); #trigger the __init__(self)
connection.connect();
#connection.executeQuery("select * from [dbo].[checks]");
#connection.executeQuery("Create TABLE Images( imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255) , uuidName  varchar(255), extension varchar(10), disease  varchar(255), uploadDate  datetime, processedDate  datetime null);");
#connection.executeQuery("Create TABLE Images( imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255) , uuidName  varchar(255), extension varchar(10), disease  varchar(255), uploadDate  datetime, processedDate  datetime null);");
insertIntoImages = "INSERT INTO Images (originalName, uuidName, extension, disease, uploadDate, processedDate)";
insertIntoImages = insertIntoImages + "VALUES ('TestImage.jpg', 'banaanuid', 'jpg', 'Blight_Early', GetDate(), NULL);"
connection.executeQuery(insertIntoImages);

# Janked this scheduler from tutorialspoint
# https://www.tutorialspoint.com/python/python_thread_scheduling.htm
import sched
from datetime import datetime
import time

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