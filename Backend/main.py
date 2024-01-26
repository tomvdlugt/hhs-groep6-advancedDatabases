#import Models.SystemModel
from InitialzeHandlers.MainPart1_Directories import Directories;
from InitialzeHandlers.MainPart2_TrainTheModel import TrainTheModel;
Directories.MainPart1_Method();
TrainTheModel.MainPart2_Method();

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