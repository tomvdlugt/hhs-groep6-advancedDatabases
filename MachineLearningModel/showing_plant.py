

from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np

img_path = '/Users/tom/Documents/Documents/Projects/HHS/Semester 5/portfolio 3/hhs-groep6-advancedDatabases/MachineLearningModel/input/new_plant_diseases_dataset/train/Potato___Early_blight/0a8a68ee-f587-4dea-beec-79d02e7d3fa4___RS_Early.B 8461.JPG'
img1 = image.load_img(img_path)
plt.imshow(img1);
#preprocess image
img1 = image.load_img(img_path, target_size=(256, 256))
img = image.img_to_array(img1)
img = img/255
img = np.expand_dims(img, axis=0)