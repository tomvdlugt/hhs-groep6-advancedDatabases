import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

import keras as keras
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D,Activation,AveragePooling2D,BatchNormalization
train_dir = "D:\\Projects_D\\S5_Groep6\\PlantenHerkenning\\Backend\\MachineLearningModel\\input\\new_plant_diseases_dataset\\train"
test_dir = "D:\\Projects_D\\S5_Groep6\\PlantenHerkenning\\Backend\\MachineLearningModel\\input\\new_plant_diseases_dataset\\test"
valid_dir = "D:\\Projects_D\\S5_Groep6\\PlantenHerkenning\\Backend\\MachineLearningModel\\input\\new_plant_diseases_dataset\\valid"

def get_files(directory):
    if not os.path.exists(directory):
        return 0
    count = 0
    for current_path, dirs, files, in os.walk(directory):
        for dr in dirs:
            count += len(glob.glob(os.path.join(current_path, dr+"\\*")))
    return count

train_samples = get_files(train_dir)
num_class_train = len(glob.glob(train_dir+"\\*"))

test_samples = get_files(test_dir)
num_classes_test = len(glob.glob(test_dir+"\\*"))

valid_samples = get_files(valid_dir)
num_classes_valid = len(glob.glob(valid_dir+"\\*"))

# print(num_class_train, "classes")
# print(train_samples, "train images")

# print(num_classes_test, "Classes")
# print(test_samples,"Test images")

# print(num_classes_valid, "Classes")
# print(valid_samples,"Valid images")

train_datagen=ImageDataGenerator(rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

valid_datagen = ImageDataGenerator(rescale = 1./255)

img_width, img_height = 256, 256

input_shape=(img_width, img_height, 3)

batch_size = 256

train_generator = train_datagen.flow_from_directory(train_dir, target_size=(img_width, img_height), batch_size=batch_size)
valid_generator = valid_datagen.flow_from_directory(valid_dir, target_size=(img_width, img_height), batch_size=batch_size)
# test_generator = test_datagen.flow_from_directory(test_dir, shuffle = True, target_size = (img_width, img_height), batch_size = batch_size)

train_generator.class_indices
valid_generator.class_indices


def printData(generator):
    print("-----------------------------------------")
    print("Samples:",generator.samples)
    print("No of classes:",generator.num_classes)
    print("Batch size:", generator.batch_size)
    print("Data format:", generator.dtype)
    print("Color mode:",generator.color_mode)
    print("Image shape:", generator.image_shape)
    print("Allowed class modes:", generator.allowed_class_modes)
    print("Class Mode:", generator.class_mode)
    

printData(train_generator)
printData(valid_generator)

model = Sequential()

model.add(Conv2D(32, (5,5), input_shape = input_shape, activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3)))

model.add(Conv2D(32, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(512, activation = 'relu'))

model.add(Dropout(0.25))

model.add(Dense(128, activation='relu'))

model.add(Dense(num_class_train, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()
