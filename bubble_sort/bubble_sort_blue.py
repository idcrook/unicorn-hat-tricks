"""
Program: Bubble Sort
Author: Tim Mulford
Date: 28/11/2017
Bubblesort LEDS on Unicorn HAT HD by brightness

23-Apr-2018: updated for Unicorn HAT (non-HD)
"""

from random import *
from unicornhat import *

def randomise_red():
    pixels = []

    for i in range(64):
        pixel = [randint(0,255),0,0]
        pixels.append(pixel)
    return pixels

def randomise_green():
    pixels = []

    for i in range(64):
        pixel = [0,randint(0,255),0]
        pixels.append(pixel)
    return pixels

def randomise_blue():
    pixels = []

    for i in range(64):
        pixel = [0,0,randint(0,255)]
        pixels.append(pixel)
    return pixels

def display(pixels):
    for i in range(64):
        set_pixel(i//8,i%8,pixels[i][0],pixels[i][1],pixels[i][2])

    show()

# colour use 0 for R, 1 for G, 2 for B
def bubblesort(pixels,colour):
    for i in range(63):
        swapped = False
        for j in range(0,63-(i)):
            if pixels[j][colour] > pixels[j+1][colour]:
                temp = pixels[j][colour]
                pixels[j][colour] = pixels[j+1][colour]
                pixels[j+1][colour] = temp
                swapped = True
            display(pixels)
        if swapped == False:
            break

pixels=randomise_blue()

bubblesort(pixels,2)
