import pygame
from pygame.locals import *
import os
import sys
import time
import pyinputplus as pyip
import random
import numpy
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
        self.vistited = False
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
        self.vistited = True
    def ispart(self):
        self.hitboxstatus = False
        self.boxstatus = False
        self.vistited = True
    def isvisited(self):
        self.vistited = True
pygame.init()
t = []

j=0
run = True
display_width = 560
display_height =560
display= pygame.display.set_mode((display_width, display_height))
def makeboxes():
    for i in range(1,b):
        for l in range(1,b):
            t.append(box(i*r,l*r,r,r,bluer,display))


makeboxes()
def Make2darray():
    num = 0
    global TDArray
    for i in range(1,b):
        insert = []
        for l in range(1,b):
            insert.append(t[num])
            num+=1
        if(i == 1):
            TDArray =  numpy.array([insert])
        else:
            TDArray = numpy.append(TDArray, [insert],axis = 0)
Make2darray()

def setStart(row):
    startingpos = random.randint(0,b-2)
    startingclass  = TDArray[row, startingpos]
    startingclass.isStart()
    runmakemaze(startingclass)
def getneighbouring(input):
    cellx = numpy.where(TDArray == input)
    cellx = cellx[0]
    celly = numpy.where(TDArray == input)
    celly = celly[1]
    neigboors = []
    ncordsx = int(cellx)
    ncordsy = int(celly + 1)

    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if(trailclass.vistited != True):
            neigboors.append(trailclass)
        else:
            pass
    except:
        pass
    ncordsx = int(cellx)
    ncordsy = int(celly - 1)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if(trailclass.vistited != True):
            neigboors.append(trailclass)
        else:
            pass

    except:
        pass
    ncordsx = int(cellx + 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if (trailclass.vistited != True):
            neigboors.append(trailclass)
        else:
            pass

    except:
        pass
    ncordsx = int(cellx - 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if (trailclass.vistited != True):
            neigboors.append(trailclass)
        else:
           pass

    except:
        pass
    return neigboors

def makemaze(input_class):
    global currentcell
    global spaceleft
    neighbouringcells  = getneighbouring(input_class)
    lengthofn  = len(neighbouringcells)
    if(lengthofn == 0):
        spaceleft = False
        print("done")
    else:
        currentcell = neighbouringcells[random.randint(0, lengthofn-1)]
        currentcell.ispart()
        stack.append(currentcell)
        for cells in neighbouringcells:
            cells.isvisited()


def runmakemaze(start):
    global currentcell
    global spaceleft
    makemaze(start)
    while(spaceleft == True):
        makemaze(currentcell)

stack = []
spaceleft = True
setStart(0)
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
