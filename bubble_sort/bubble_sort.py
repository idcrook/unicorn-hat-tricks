"""
Program: Bubble Sort
Author: Tim Mulford
Date: 28/11/2017
Bubblesort LEDS on Unicorn HAT HD by brightness

https://www.raspberrypi.org/forums/viewtopic.php?t=98666#p1241746

23-Apr-2018: @idcrook updated for  Unicorn HAT (not HD)
"""
import time
from random import *
from unicornhat import *


class Bubblesort():

    def __init__(self, colour = "grey"):

        self.pixels = []

        for i in range(64):
            if colour.lower() == "red":
                pixel = [randint(0,255),0,0]
            elif colour.lower() == "green":
                pixel = [0,randint(0,255),0]
            elif colour.lower() == "blue":
                pixel = [0,0,randint(0,255)]
            elif colour.lower() == "rgb":
                pixel = [randint(0,255),randint(0,255),randint(0,255)]
            elif colour.lower() == "purple":
                purple = randint(0,255)
                pixel = (purple,0,purple)
            elif colour.lower() == "yellow":
                yellow = randint(0,255)
                pixel = (yellow,yellow,0)
            elif colour.lower() == "grey":
                grey = randint(0,255)
                pixel = [grey,grey,grey]
            self.pixels.append(pixel)
        self.display()
        self.bubblesort()

    def display(self):
        for i in range(64):
            set_pixel(i//8,i%8,self.pixels[i][0],self.pixels[i][1],self.pixels[i][2])
        show()

    def bubblesort(self):
        for i in range(63):
            swapped = False
            for j in range(0,63-(i)):
                if self.pixels[j][0]+self.pixels[j][1]+self.pixels[j][2] > self.pixels[j+1][0]+self.pixels[j+1][1]+self.pixels[j+1][2]:
                    temp = self.pixels[j]
                    self.pixels[j] = self.pixels[j+1]
                    self.pixels[j+1] = temp
                    swapped = True
                self.display()
            if swapped == False:
                break
        time.sleep(2)

brightness(b=0.33)

unicorn = Bubblesort()
