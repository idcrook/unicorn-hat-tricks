#!/usr/bin/env python

# https://www.raspberrypi.org/forums/viewtopic.php?t=98666#p865731
# code posted by evilunix, Sun Dec 20, 2015 6:43 pm
# updated indentation to PEP-8


import unicornhat as UH
import time
import random
import colorsys as col

UH.brightness(0.41)

SPEED = 0.1

# convert hex to rgb tuple
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


class Player:

    def __init__(self, hue):
	self.hue = hue

    direction_x = 0 # 1 = up, 2 = down
    y = 0 # position of topmost pixel

    def spawn(self):
	self.y = random.randint(0,5)

    def think(self, ball):

	# change colour
	if self.hue < 360:
	    self.hue = self.hue + 1
	else:
	    self.hue = 0

        rand = random.randint(0,19)
        if(rand == 13):
            derp = 1
        else:
            derp = 0

        if ball.y > self.y + 1 and self.y < 5:
            # ball is below player center - move down
            if derp == 0:
                self.y = self.y + 1


        if ball.y < self.y + 1 and self.y > 0:
            # ball is above player center - move up
            if derp == 0:
                self.y = self.y - 1


class Ball:

    direction_x = 0 # 1 = up, 2 = down
    direction_y = 0 # 1 = left, 2 = right

    x = 0
    y = 0

    colour = hex_to_rgb('ffffff')

    def spawn(self):

	print 'spawning ball...'

        # ball starting directions
        self.direction_x = random.randint(1,2)
	self.direction_y = random.randint(1,2)

	# ball starting position
	self.x = random.randint(3,4)
	self.y = random.randint(3,4)


player1 = Player(0)
player2 = Player(90)
ball = Ball()


def update():
    global ball, player1, player2

    player1.think(ball)
    player2.think(ball)

    # check if ball hit upper or lower wall
    if ball.y == 0:
        #change direction
        ball.direction_y = 2 # down
    if ball.y == 7:
        # change direction
        ball.direction_y = 1 # up

    if ball.direction_y == 2: # down
        # move 1 cell down
        ball.y = ball.y + 1
    elif ball.direction_y == 1: #up
        # move 1 cell up
        ball.y = ball.y - 1


    if ball.direction_x == 1: # moving left

	ball.x = ball.x - 1

        if ball.x == 0:
            # check for collision
	    if ball.y >=  player1.y and ball.y <= player1.y + 3:
		print 'SAVE!'
		#change direction
		ball.direction_x = 2
		ball.x = ball.x + 1
	    else:
           	# GOAL!
		print 'GOAL!'
		goal()
		ball.spawn()

    if ball.direction_x == 2: # moving right

	ball.x = ball.x + 1

        if ball.x == 7:
            # check for collision
	    if ball.y >= player2.y and ball.y <= player2.y + 3:
		print 'SAVE!'
		# change direction
		ball.direction_x = 1
		ball.x = ball.x - 2
	    else:
		# GOAL!
		goal()
		print 'GOAL!'
            	ball.spawn()

def goal():
    global ball

    draw()
    time.sleep(SPEED)

    set_pixel(ball.x, ball.y, hex_to_rgb('000000'))
    UH.show()
    time.sleep(SPEED)

    set_pixel(ball.x, ball.y, ball.colour)
    UH.show()
    time.sleep(SPEED)

    set_pixel(ball.x, ball.y, hex_to_rgb('000000'))
    UH.show()
    time.sleep(SPEED)


    set_pixel(ball.x, ball.y, ball.colour)
    UH.show()
    time.sleep(SPEED)



def set_pixel(x, y, colour):
    UH.set_pixel(x, y, colour[0], colour[1], colour[2])

def fill_hex(colour):
    rgb = hex_to_rgb(colour)
    for x in range(0, 8):
	for y in range(0, 8):
	    set_pixel(x, y, rgb)
	    UH.show()

def set_pixel_hue(x, y, h):

    hfloat = h / 255.0

    rgb = col.hsv_to_rgb(hfloat, 0.5, 1.0)
    r = int(rgb[0] * 255)
    g = int(rgb[1] * 255)
    b = int(rgb[2] * 255)
    UH.set_pixel(x, y, r, g, b)


def draw():
    global ball, player1, player2, BG_COLOUR
    UH.off()

    #fill_hex(BG_COLOUR)

    # draw ball
    set_pixel(ball.x, ball.y, ball.colour)

    # draw player1
    set_pixel_hue(0, player1.y, player1.hue)
    set_pixel_hue(0, player1.y + 1, player1.hue)
    set_pixel_hue(0, player1.y + 2, player1.hue)

    # draw player2
    set_pixel_hue(7, player2.y, player2.hue)
    set_pixel_hue(7, player2.y + 1, player2.hue)
    set_pixel_hue(7, player2.y + 2, player2.hue)


    UH.show()


player1.spawn()
player2.spawn()
ball.spawn()
draw()

while True:
    time.sleep(SPEED)
    update()
    draw()
