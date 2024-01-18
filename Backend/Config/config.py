# Define the paths to your dataset
import os

# gets the root project path
rootDirectory_path = os.getcwd()

# Sets paths to the folders
dataset_directory = f"{rootDirectory_path}/input/new_plant_diseases_dataset"
train_path = dataset_directory + '/train'
valid_path = dataset_directory + '/valid'
test_path = dataset_directory + '/test/'
trained_models = rootDirectory_path + '/trained_models/'

# Sets the amount of epochs ran by the training
epochs = 1

#
batch_size = 30