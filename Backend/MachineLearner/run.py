import os
import glob
import random
import numpy as np
from keras.preprocessing import image
from keras.models import load_model

# Load the pre-trained model
model = load_model('/Users/tom/Documents/Documents/Projects/HHS/Semester 5/portfolio 3/hhs-groep6-advancedDatabases/new_my_h5_model.h5')  # Replace with your model's filename

# Function to preprocess the image
def prepare_image(image_path):
    img = image.load_img(image_path, target_size=(256, 256))  # Resize the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalize the image
    return x

# Directory containing images
directory = '/Users/tom/Documents/Documents/Projects/HHS/Semester 5/portfolio 3/hhs-groep6-advancedDatabases/MachineLearningModel/input/new_plant_diseases_dataset/LiveTest'  # Replace with your directory path

# Get list of image paths
image_paths = glob.glob(os.path.join(directory, '*.*'))  # Adjust the pattern as needed

random.shuffle(image_paths)

# Class names
class_names = ["Potato___Early_blight", "Potato___healthy", "Potato___Late_blight"]  # Replace with your class names

# Loop through the images and make predictions
for image_path in image_paths:
    prepared_image = prepare_image(image_path)
    prediction = model.predict(prepared_image)
    predicted_class = np.argmax(prediction, axis=1)
    print(f"Image: {os.path.basename(image_path)} - Predicted class: {class_names[predicted_class[0]]}")
