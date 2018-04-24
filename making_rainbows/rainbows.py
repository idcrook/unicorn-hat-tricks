#!/usr/bin/env python
#-*- coding: utf-8 -*-

import math
import time
import colorsys as col
import unicornhat as uh

uh.brightness(0.35)

def set_pixel_hsv(x,y,h,s,v):
  r, g, b = [int(c*255) for c in col.hsv_to_rgb(h,s,v)]
  uh.set_pixel(x,y,r,g,b)


def fade_pixel_hsv(x,y,h,s,v,t):
    end = int(v*100)
    delay = float(t)/end
    for v in range(end):
        set_pixel_hsv(x,y,h,s,v/100.0)
        uh.show()
        time.sleep(delay)

def draw_hue_sat_on_matrix():
    for y in range(8):
        for x in range(8):
            set_pixel_hsv(x,y,(1.0/8)*x,(1.0/8)*y,1.0)

    uh.show()

def fade_hue_sat_on_matrix():
    for y in range(8):
        for x in range(8):
            fade_pixel_hsv(x,y,(1.0/8)*x,(1.0/8)*y,1.0, 0.01)


if __name__ == '__main__':
    while 1:
        draw_hue_sat_on_matrix()
        time.sleep(2)
        fade_hue_sat_on_matrix()
