# Define the paths to your dataset
import os

# gets the root project path
base_path = os.getcwd()

# Sets paths to the folders
base_directory = f"{base_path}/input/new_plant_diseases_dataset"
train_path = base_directory + '/train'
valid_path = base_directory + '/valid'
test_path = base_directory + '/test/'
trained_models = base_path + '/trained_models/'

# Sets the amount of epochs ran by the training
epochs = 1

#
batch_size = 30