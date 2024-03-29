# This is the main, before the program is going to run, it will check all the variables given.

# Check where the program is stored, the FileHandler is to be used to determin file positions aswell
# In short: It will make the folders on startup and assign images properly when given.
from PythonTests.FileHandler import FileHandler
FileHandler.CheckDirectoryIntegrity();

FileHandler.MoveIncommingToProcessed("771f7d94-19c8-4715-8e4c-c00217254eec.JPG");


# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset (you can replace this with your own dataset)
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess the data
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the neural network model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')

import os
import glob
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
import keras as keras
msg = "hello me"
print(msg)
print(msg)

print(keras.__version__)
print(msg)
print(tf.__version__)



print(msg)