from PlantDiseaseRecogniseModel import plantDiseaseRecogniseModel
from config import *

if __name__ == "__main__":
    #instantiate the class
    model = plantDiseaseRecogniseModel(train_path, valid_path, test_path)
    print(f"Test path: {test_path}")
    
    # Train the model
    history = model.train(epochs = epochs, batch_size = batch_size)

    model.evaluate()

    # saves file 
    model.save(folderPath=trained_models, filename='plantDiseaseRecognitionModel')
    
    # draws diagram of the training result
    model.plot_metrics(history)
    print("done")