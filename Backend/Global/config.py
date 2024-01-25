from asyncio.windows_events import NULL
from typing import Self


class GlobalConfig:
	# Define the paths to your dataset
	import os
	from Global.ConfigHandler import ConfigHandler;
	from Handler.FileHandler import FileHandler;
	# Global variables
	projectRoot = str(os.getcwd());

	# Sets paths to the folders
	# Main
	train_directory = NULL;
	train_path = NULL;
	valid_path = NULL;
	test_path = NULL;
	trained_models = NULL;
	# Image processing
	mainImagesPath = NULL;
	rawImagesPath = NULL;
	processedImagesPath = NULL;
	trainedImagesPath = NULL;


	# gets the root project path
	projectRoot = str(os.getcwd());

	# Sets paths to the folders
	# Main
	train_directory = f"{projectRoot}/input/new_plant_diseases_dataset"
	train_path = train_directory + '/train'
	valid_path = train_directory + '/valid'
	test_path = train_directory + '/test/'
	trained_models = projectRoot + '/trained_models/'

	
	# Image processing
	mainImagesPath = projectRoot + "\\Images";
	rawImagesPath = mainImagesPath + "\\Incoming";
	processedImagesPath = mainImagesPath + "\\Processed";
	trainedImagesPath = mainImagesPath + "\\Trained";

	# Change paths to correct system paths
	projectRoot = ConfigHandler.ParseDirectoryPath(projectRoot);
	train_directory = ConfigHandler.ParseDirectoryPath(train_directory);
	train_path = ConfigHandler.ParseDirectoryPath(train_path);
	valid_path = ConfigHandler.ParseDirectoryPath(valid_path);
	test_path = ConfigHandler.ParseDirectoryPath(test_path);
	trained_models = ConfigHandler.ParseDirectoryPath(trained_models);
	
	# Image processing
	mainImagesPath = ConfigHandler.ParseDirectoryPath(projectRoot + "\\Images");
	rawImagesPath = ConfigHandler.ParseDirectoryPath(mainImagesPath + "\\Incoming");
	processedImagesPath = ConfigHandler.ParseDirectoryPath(mainImagesPath + "\\Processed");
	trainedImagesPath = ConfigHandler.ParseDirectoryPath(mainImagesPath + "\\Trained");
	
	# Create directory collection
	trainDirectoryCollection = {train_directory, train_path, valid_path, test_path, trained_models }
	processingDirectoryCollection = {mainImagesPath, rawImagesPath, processedImagesPath, trainedImagesPath }
	
	# Check and Create paths if not present
	

	# Sets the amount of epochs ran by the training
	epochs = 1

	#
	batch_size = 30
	
	def RunCollectionParseDirectory(self):
		from Global.ConfigHandler import ConfigHandler;
		projectRoot = ConfigHandler.ParseDirectoryPath(projectRoot);
		train_directory = ConfigHandler.ParseDirectoryPath(train_directory);
		train_path = ConfigHandler.ParseDirectoryPath(train_path);
		valid_path = ConfigHandler.ParseDirectoryPath(valid_path);
		test_path = ConfigHandler.ParseDirectoryPath(test_path);
		trained_models = ConfigHandler.ParseDirectoryPath(trained_models);
	