class MachineLearningDirectoriesModel:
    def __init__(self, train_directory, train_Path, valid_path, test_path, trained_models):
        self.train_directory = train_directory;
        self.train_Path = train_Path;
        self.valid_path = train_Path;
        self.test_path = test_path;
        self.trained_models = trained_models;
        self.allPaths = {train_directory, 
                         train_Path,
                         valid_path,
                         test_path,
                         trained_models}