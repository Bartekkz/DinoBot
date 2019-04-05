#!/usr/bin/env python3

import numpy as np
import cv2
import pyscreenshot as ImageGrab

class Screen:
  '''
  Class that grabs part of the screen 
  according to given coordinates, it
  is able to display it too
  
  attributes:
    -coordinates -> coordinates of the screen You
    want to grab (x1, y1, x2, y2)
  '''
  def __init__(self, coordinates):
   self.x1 = coordinates[0]
   self.y1 = coordinates[1]
   self.x2 = coordinates[2]
   self.y2 = coordinates[3]

  def grab_screen(self):
    image = np.array(ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2)))
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #image = cv2.Canny(image, 100, 200)
    return image

  def show_screen(self):
    self.image = self.grab_screen()
    cv2.imshow('img', self.image)
    cv2.waitKey(0)
    if cv2.waitKey(27) and 0xFF == ord('q'):
      cv2.destroyAllWindows()
      cv2.close()

