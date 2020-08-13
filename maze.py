import pygame
from pygame.locals import *
import os
import sys
import time
import pyinputplus as pyip
import random
from array import *
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bluer = (0, 100, 255)
r=31
b= r
r = 500/r
class box():
    def __init__(self,x,y,l,w,color,display):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.color = color
        self.hitbox = (self.x, self.y, self.w, self.l)
        self.hitboxstatus = True
        self.boxstatus = True
        vistited = False
    def draw(self,win):
        if(self.hitboxstatus == True):
            if(b >33):
                pygame.draw.rect(display, self.color, (self.x, self.y,  self.w,  self.w),2)
            elif (b >45):
                pygame.draw.rect(display, self.color, (self.x, self.y,  self.w,  self.w),2)
            else:
                pygame.draw.rect(display, self.color, (self.x, self.y, self.w,  self.w),2)
    def isStart(self):
        self.hitboxstatus = False
        self.boxstatus = False
    def ispart(self):
        self.hitboxstatus = False
        self.boxstatus = False
pygame.init()
t = []
TDArray = [[]]
j=0
run = True
display_width = 560
display_height =560
display= pygame.display.set_mode((display_width, display_height))
def makeboxes():
    for i in range(1,b):
        for l in range(1,b):
            t.append(box(i*r,l*r,r,r,bluer,display))

    print(len(t))
makeboxes()
def Make2darray():
    num = 0
    for i in range(1,b):
        insert = []
        for l in range(1,b):
            print(num)
            insert.append(t[num])
            num+=1
        TDArray.insert(i,insert)
Make2darray()
def setStart(row):
    startingpos = random.randint(0,b-1)
    startingclass  = TDArray[row][startingpos]
    startingclass.isStart()
setStart(1)
pygame.display.set_caption("Maze")
while run:
    display.fill((black))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run  = False

    random.randint(0,b)
    for r in TDArray:
        for c in r:
            c.draw(display)


    pygame.display.update()




pygame.quit()
quit()
