from PlantDiseaseRecogniseModel import plantDiseaseRecogniseModel
from config import *

if __name__ == "__main__":
    #instantiate the class
    model = plantDiseaseRecogniseModel(train_path, valid_path, test_path)
    print(f"Test path: {test_path}")
    
    # Train the model
    history = model.train(epochs = 5, batch_size = 30)

    model.evaluate()

    # saves file 
    model.save('plantDiseaseRecognitionModel.h5')
    
    # draws diagram of the training result
    model.plot_metrics(history)