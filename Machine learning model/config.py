# Define the paths to your dataset
import os

base_path = os.getcwd()

base_directory = f"{base_path}/input/new_plant_diseases_dataset"
print(f'base {base_directory}')
train_path = base_directory + '/train'
valid_path = base_directory + '/valid'
test_path = base_directory + '/test/'