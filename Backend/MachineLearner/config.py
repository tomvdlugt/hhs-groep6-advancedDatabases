# Define the paths to your dataset
import os
from Handler.FileHandler import FileHandler as FileHandler_Class; 

# gets the root project path
base_path = os.getcwd()

print(base_path)

# Sets paths to the folders
base_directory = FileHandler_Class.ParseDirectoryPath(f"{base_path}/MachineLearningModel/input/new_plant_diseases_dataset");
train_path = FileHandler_Class.ParseDirectoryPath(base_directory + '/train')
valid_path = FileHandler_Class.ParseDirectoryPath(base_directory + '/valid')
test_path = FileHandler_Class.ParseDirectoryPath(base_directory + '/test')
trained_models = FileHandler_Class.ParseDirectoryPath(base_path + '/trained_models')

# Sets the amount of epochs ran by the training
epochs = 5

#
batch_size = 40