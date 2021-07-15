import pygame
from pygame.locals import *
import os
import sys
import time
import pyinputplus as pyip
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
thing = (0, 100, 255)
r = int(pyip.inputNum("Enter a number between 2 and 55: ", greaterThan=1, lessThan=56))
b= r
r = 500/r
class box():
    def __init__(self,x,y,l,w,color,display):
        box.x = x
        box.y = y
        box.l = l
        box.w = w
        box.color = color

    def draw(win,self):
        if(b >33):
            pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.l),2)
        elif (b >45):
            pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.l),1)



pygame.init()



t = []
j=0
run = True
display_width = 550
display_height =550
display= pygame.display.set_mode((display_width, display_height))
display.fill((black))
for i in range(1,b):
    for l in range(1,b):
        t.append(box(i*r,l*r,r,r,thing,display))
        box.draw(display,box)


print(t)


pygame.display.set_caption("Maze")

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run  = False

    box.draw(display,box)

    pygame.display.update()


pygame.quit()
quit()
