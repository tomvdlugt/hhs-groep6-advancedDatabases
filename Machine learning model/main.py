import os;
import platform;

print(str(os.getcwd()));
print(platform.system());

import warnings
warnings.filterwarnings('ignore')

from config import *

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report , confusion_matrix , accuracy_score , auc
from sklearn.model_selection import train_test_split

import cv2
#from google.colab.patches import cv2_imshow
from PIL import Image 
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Input, Dense,Conv2D , MaxPooling2D, Flatten,BatchNormalization,Dropout
from keras.preprocessing import image_dataset_from_directory
import tensorflow_hub as hub 

from keras.applications import MobileNetV2
from keras.applications.vgg19 import VGG19
from keras_preprocessing.image import ImageDataGenerator
from keras.layers import GlobalAveragePooling2D

# Load and preprocess the data
datagen = ImageDataGenerator(
    rescale=1.0 / 255.0,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
)

train_scaled_data = datagen.flow_from_directory(
    train_path,
    target_size=(224, 224),
    batch_size=256,
    shuffle=True,
    class_mode='sparse',
)

valid_scaled_data = datagen.flow_from_directory(
    valid_path,
    target_size=(224, 224),
    batch_size=256,
    shuffle=True,
    class_mode='sparse',
)

# Define your custom CNN architecture
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.7),
    Dense(len(train_scaled_data.class_indices), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Summary of the model architecture
model.summary()

# Train the model
history = model.fit(train_scaled_data, batch_size=256, epochs=10, verbose=1, validation_data=valid_scaled_data)

# Evaluate the model on train and validation data
loss, acc = model.evaluate(train_scaled_data)
print('Loss on Train data:', loss)
print('Accuracy on train data:', acc)

loss, acc = model.evaluate(valid_scaled_data)
print('Loss on validation data:', loss)
print('Accuracy on validation data:', acc)

test_datagen = ImageDataGenerator(rescale = 1.0 / 255.0)



model.save('plantDiseaseRecognition.h5')

# Plot training and validation metrics
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = 10
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(range(epochs), acc, label="Training accuracy")
plt.plot(range(epochs), val_acc, label='Validation accuracy')
plt.legend(loc='lower right')
plt.title('Training and validation accuracy')

plt.subplot(1, 2, 2)
plt.plot(range(epochs), loss, label="Training loss")
plt.plot(range(epochs), val_loss, label="Validation loss")
plt.legend(loc="lower right")
plt.title("Training and Validation loss")
plt.show()