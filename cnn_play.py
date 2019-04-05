#!/usr/bin/env python3

from selenium import webdriver
from keras.models import load_model
from screen import Screen
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import keyboard
import time

#loading weights
model = load_model('dino_weigths_after_train3.h5')

#instance of Screen class
screen = Screen([755, 200, 1250, 320])  

#chrome webdriver instance
driver = webdriver.Chrome()
driver.get('http://www.google.com')
page = driver.find_element_by_class_name('offline')
#"Space" key
page.send_keys(u'\ue013')

#predicting next move
def predict():
  img = screen.grab_screen()
  img = img[20:100, 30:430]
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img = cv2.Canny(img, 100, 200)
  img = img.reshape(1, 80, 400, 1)
  y_pred = model.predict(img)
  prediction = y_pred.argmax(axis=-1)

  if prediction == 1:
    print('STAY')
    time.sleep(0.7)

  if prediction == 0:
    time.sleep(0.7)
    page.send_keys(u'\ue013')
    print('JUMP')

if __name__ == '__main__':
  while True:
    predict()




