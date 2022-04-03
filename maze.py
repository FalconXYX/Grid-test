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
        self.l = l+2
        self.w = w+2
        self.color = color
        self.hitbox = (self.x, self.y, self.w, self.l)
        self.hitboxstatus = True
        self.boxstatus = True
        self.vistited = False
        self.inmaze  = False
        self.istack = False
    def draw(self,win):
        if(self.hitboxstatus == True):
            if(b >33):
                pygame.draw.rect(display, self.color, (self.x, self.y,  self.w,  self.w))
            elif (b >45):
                pygame.draw.rect(display, self.color, (self.x, self.y,  self.w,  self.w))
            else:
                pygame.draw.rect(display, self.color, (self.x, self.y, self.w,  self.w))
    def isStart(self):
        self.hitboxstatus = False
        self.boxstatus = False
        self.vistited = True
    def ispart(self):
        self.hitboxstatus = False
        self.boxstatus = False
        self.vistited = True
        self.inmaze = True
    def isvisited(self):
        self.vistited = True
    def unvisit(self):
        self.vistited = False
    def is_stack(self):
        self.istack = True
    def is_end(selfself):
        pass
pygame.init()
t = []
startingthing = 0
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
global startingclass
def setStart(row):
    global startx
    global starty
    global startingclass

    startingpos = random.randint(0,b-2)
    startingclass  = TDArray[row, startingpos]
    startingclass.isStart()
    startx = startingclass.x
    starty = startingclass.y
    runmakemaze(startingclass)
def getneighbourof(input,current):
    cellx = numpy.where(TDArray == input)
    cellx = cellx[0]
    celly = numpy.where(TDArray == input)
    celly = celly[1]
    iffour = []
    ncordsx = int(cellx)
    ncordsy = int(celly + 1)

    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if (trailclass.vistited != True):
            iffour.append(trailclass)
        elif (trailclass == current):
            iffour.append(trailclass)
    except:
        pass
    ncordsx = int(cellx)
    ncordsy = int(celly - 1)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if (trailclass.vistited != True):
            iffour.append(trailclass)
        elif (trailclass == current):
            iffour.append(trailclass)

    except:
        pass
    ncordsx = int(cellx + 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if (trailclass.vistited != True):
            iffour.append(trailclass)
        elif (trailclass == current):
            iffour.append(trailclass)
    except:
        pass
    ncordsx = int(cellx - 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        if(trailclass.vistited != True):
            iffour.append(trailclass)
        elif(trailclass == current):
            iffour.append(trailclass)
    except:
        pass
    print(len(iffour))
    print(iffour)
    if(len(iffour) == 4):
        return True
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
        isavalid = getneighbourof(trailclass, input)
        print("no", isavalid)
        if (isavalid == True):
            print("works")
            neigboors.append(trailclass)
    except:
        pass
    ncordsx = int(cellx)
    ncordsy = int(celly - 1)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = getneighbourof(trailclass, input)
        print("no", isavalid)
        if(isavalid == True):
            neigboors.append(trailclass)

    except:
        pass
    ncordsx = int(cellx + 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = getneighbourof(trailclass, input)
        print("no", isavalid)
        if (isavalid == True):
            neigboors.append(trailclass)
    except:
        pass
    ncordsx = int(cellx - 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = getneighbourof(trailclass, input)
        print(isavalid)
        if (isavalid == True):
            neigboors.append(trailclass)
    except:
        pass
    return neigboors
def makemaze(input_class):
    global currentcell
    global startingthing
    global spaceleft
    global endx
    global endy
    neighbouringcells  = getneighbouring(input_class)
    lengthofn  = len(neighbouringcells)
    if(lengthofn == 0):


        currentcell = stack.pop()
        currentcell.is_stack()

        if(len(stack) == 0):
           spaceleft = False
           print("done")
    else:
        currentcell = neighbouringcells[random.randint(0, lengthofn-1)]
        currentcell.ispart()
        currentcell.isvisited()
        stack.append(currentcell)
        for cells in neighbouringcells:
            pass
    half1 = round(len(TDArray[1]) / 2) - 1
    half2 = round(len(TDArray[1]) / 2) - 1
    middle = TDArray[half1][half2]
    for x in range(0, 5):
        if (middle.inmaze == True):
            middle.is_end()
            break
        else:
            half1 += 1
            half2 += 1
            middle = TDArray[half1][half2]


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
    pygame.draw.rect(display, red, (15, 15, 486, 486), 4)
    #pygame.draw.rect(display, black, (startx-10, starty, 26.129032258064516, 16.329032258064516))
    #pygame.draw.rect(display, green, (startx, starty, 16.129032258064516, 16.129032258064516), 2)
    #pygame.draw.rect(display, red, (44, 44, 16.129032258064516, 16.129032258064516), 2)

    pygame.display.update()




pygame.quit()
quit()
