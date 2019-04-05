#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers import (Dense, MaxPooling2D, Conv2D, Dropout, Flatten,
                          BatchNormalization, Lambda)
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import to_categorical
import os
from loadata import LoadData

#instance of the LoadData class
loader = LoadData('./image_data/', 'moves1.csv', 2122)

#load data with loader instance
def load_data():
  loader.get_image_data()
  loader.get_csv_data()
  return loader.X, loader.Y

#Fix labels for using keras.utils later
def fixed_labels():
  y = []
  for i in Y:
    if i == '1':
      y.append(0)
    if i == '2':
      y.append(1)
  return y

#Loading data
X, Y = load_data()
print(loader.__len__())

#normalize and preprocess data
Y = fixed_labels()
Y = to_categorical(Y, 2)
X = X/255

#split data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=123)

input_shape = X_train[0].shape

#Create keras model
def create_model():
  model = Sequential()
  model.add(Lambda(lambda x: x, input_shape=input_shape))
  model.add(Conv2D(32, (3,3), activation='relu'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D((2,2)))
  model.add(Flatten())
  model.add(Dense(256, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(2, activation='sigmoid'))
  return model

model = create_model()

#Model constants
optimizer = Adam(lr=2e-4)
num_epochs = 20 
batch_size=150

#compiling model
model.compile(loss='binary_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])

#Fitting model
history = model.fit(X_train, 
                    y_train, 
                    batch_size=batch_size, 
                    epochs=num_epochs, 
                    validation_data=(X_test, y_test))

#Saving weights of the model
model.save('dino_weigths_after_train4.h5')

#save accuracy and losses of training and validation sets
acc = history.history['acc']
loss = history.history['loss']
val_acc = history.history['val_acc']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

#plotting accuracies
fig = plt.figure(figsize=(20, 12))
plt.plot(epochs, acc, 'b', label='Training Accuracy')
plt.plot(epochs, val_acc, 'bo', label='Validation Accuracy')
plt.show()
