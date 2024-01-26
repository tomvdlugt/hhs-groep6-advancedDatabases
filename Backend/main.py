#import Models.SystemModel
from InitialzeHandlers.MainPart1_Directories import Directories;
from InitialzeHandlers.MainPart2_TrainTheModel import TrainTheModel;
Directories.MainPart1_Method();
#TrainTheModel.MainPart2_Method();

# Connect to the database
# can we put this in the MainPart3?
from databaseConnector import DatabaseConnector;
connection = DatabaseConnector(); #trigger the __init__(self)
connection.connect();





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