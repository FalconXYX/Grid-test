import pygame
from pygame.locals import *
import os
import sys
import time

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
class box(object):
    def __init__(self,x,y,l,w,color):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.color = color
    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

pygame.init()
def refresh():
    display.fill((black))
    pygame.draw.rect(display, red, (1, 1, 10, 10))
    pygame.display.update()

run = True
thing = box(10,10,10,10,red)
display_width = 550
display_height =550
display= pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Maze")
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run  = False
    refresh()


pygame.quit()
quit()
