#!/usr/bin/env python3

import cv2
import keyboard
import time
import csv
from screen import Screen


def get_data():
  #open csv file to save moves
  with open('moves1.csv', 'w') as f:
    x = 0 
    #object of the screen class
    screen = Screen([725, 130, 1260, 270]) 

    while True:
      img = screen.grab_screen()
      #save image and move
      if keyboard.is_pressed('space'):
        time.sleep(0.1)
        cv2.imwrite(f'img{x}.jpg', img)
        f.write('1\n')
        print('JUMP')
        f.flush()
        x += 1
      
      #save image and move
      if keyboard.is_pressed('k'):
        time.sleep(0.1)
        cv2.imwrite(f'img{x}.jpg', img)
        f.write('2\n')
        print('STAY')
        f.flush()
        x += 1

      if cv2.waitKey(27) and 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cv2.close()

if __name__ == '__main__':
  get_data()

