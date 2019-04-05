#!/usr/bin/env python3

import cv2
import os
import numpy as np

class LoadData: 
  '''
  Class that loads in images and csv file
  of given paths, plus it preprocess images
  to make it easier for later usage with
  CNN
  
  attributes:
    -path -> path for data folder
    -csvile -> name of the csv file in data folder
    -n -> num of images in data folder
  '''
  def __init__(self, path, csvfile, n):
    self.path = path
    self.csvfile = csvfile
    self.X = []
    self.Y = []
    self.n = n

  def __len__(self):
    return {'X':self.X.shape, 'Y':len(self.Y)}
  
  def get_image_data(self):
    for i in range(self.n):
      img = cv2.imread(self.path + f'img{i}.jpg')
      #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
      img = img[60:150, 0:400]
      img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      img = cv2.Canny(img, 100, 200)
      img = img.reshape(80, 400, 1)
      self.X.append(img)
    self.X = np.array(self.X)

  def get_csv_data(self):
    with open(self.csvfile, 'r') as f:
      for line in f:
        self.Y.append(line.rstrip())
  
