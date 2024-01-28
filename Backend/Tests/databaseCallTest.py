from databaseConnector import DatabaseConnector
from Models.checksModel import ChecksModel
from DAO.checkDao import ChecksDao
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

db = DatabaseConnector()
db.connect()
checks_dao = ChecksDao(db)

# Load the pre-trained model
model = load_model('Backend/trainedModel/plantDiseaseRecognitionModel28012024_123422.h5')

# Define class names based on your model's training
class_names = ['Early_blight', 'healthy', 'Late_blight']

# Load and preprocess the image
img = image.load_img('Backend/Tests/test_image/PotatoEarlyBlight4.JPG', target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.

# Make a prediction
predictions = model.predict(img_array)

# Map the prediction to a class name
predicted_class_index = np.argmax(predictions, axis=1)[0]
predicted_class_name = class_names[predicted_class_index]

def healthy_action():
    check = ChecksModel(True, 1)
    checks_dao.addCheck(check)

def early_blight_action():
    check = ChecksModel(False, 2)
    checks_dao.addCheck(check)

def Late_blight_action():
    check = ChecksModel(False, 3)
    checks_dao.addCheck(check)

    

print("Predicted class index:", predicted_class_index)
print("Predicted class name:", predicted_class_name)

# Define actions for each class in a dictionary
actions = {
    'Early_blight': lambda: early_blight_action(),
    'healthy': lambda: healthy_action(),
    'Late_blight': lambda: Late_blight_action(),
}

# Perform action based on the predicted class
action = actions.get(predicted_class_name, lambda: print("Unrecognized Picture."))
action()

# checks_dao.addCheck(check)
# print(check.momentOfCheck)
# checkDao = ChecksDao()
# checkDao.addCheck(check)


