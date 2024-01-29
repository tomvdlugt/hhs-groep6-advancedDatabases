from config import *
from helpers import *
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
#from sklearn.metrics import classification_report , confusion_matrix , accuracy_score , auc
#from sklearn.model_selection import train_test_split

#import cv2
#from google.colab.patches import cv2_imshow
from PIL import Image 
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Input, Dense,Conv2D , MaxPooling2D, Flatten,BatchNormalization,Dropout
from keras.preprocessing import image_dataset_from_directory
#import tensorflow_hub as hub 

from keras.applications import MobileNetV2
from keras.applications.vgg19 import VGG19
from keras_preprocessing.image import ImageDataGenerator
from keras.layers import GlobalAveragePooling2D

class plantDiseaseRecogniseModel:
    def __init__(self, train_path, valid_path, test_path):
        self.train_path = train_path
        self.valid_path = valid_path
        self.test_path = test_path
        self.model = self.build_model()
        self.train_data = self.load_data(train_path, augment = True)
        self.valid_data = self.load_data(valid_path, augment = False)
        self.test_data = self.load_data(test_path, augment = False)

    
    def build_model(self):
        # Define your custom CNN architecture
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(128, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            GlobalAveragePooling2D(),
            Dense(128, activation='relu'),  # Automatically infer input shape
            Dropout(0.7),
            Dense(3, activation='softmax')  # Adjust to your number of classes
        ])

        model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
        return model
    
    def load_data(self, path, augment = False):
        if augment:
            datagen = ImageDataGenerator(
                rescale=1.0 / 255.0,
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                fill_mode='nearest'
            )
        else:
            datagen = ImageDataGenerator(rescale = 1.0 / 255.0)

        return datagen.flow_from_directory(
            path,
            target_size=(244, 244),
            batch_size = 32,
            class_mode = 'sparse',
        )
    
    def train(self, epochs, batch_size):
        total_train_images = self.train_data.samples
        steps_per_epoch = np.ceil(total_train_images / batch_size).astype(int)
        validation_steps = np.ceil(self.valid_data.samples / batch_size).astype(int)

        print(f"Total training images: {total_train_images}")
        print(f"Batch size: {batch_size}")
        print(f"Steps per epoch: {steps_per_epoch}")

        history = self.model.fit(
            self.train_data,
            epochs = epochs,
            batch_size = batch_size,
            steps_per_epoch = steps_per_epoch,
            validation_data = self.valid_data,
            validation_steps = validation_steps
            
        )
        return history
    
    def evaluate(self):
        loss, accuracy = self.model.evaluate(self.test_data)
        print(f'Test loss: {loss}, Test accuracy: {accuracy}')
        return loss, accuracy

    def save(self, folderPath, filename):
        save_url = folderPath + filename + now() + ".h5"
        self.model.save(filepath=save_url)

    def plot_metrics(self, history):
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']
        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(len(acc))

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.title('Training and Validation Accuracy')
        plt.legend(loc='lower right')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.title('Training and Validation Loss')
        plt.legend(loc='upper right')

        plt.show()
