import math
import os
import random
import sys
import time
from array import *

import numpy
import openpyxl
import pygame
import pyinputplus as pyip
from pygame.locals import *
import make2Darray
import box
global button, lastcell, currentcell
button = True
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bluer = (0, 50, 255)
r=31
b= r
r = 500/r
display_width = 560
display_height =560
display= pygame.display.set_mode((display_width, display_height))
pygame.init()
t = []
startingthing = 0
j=0

def makeboxes():

    for i in range(1,b):
        for l in range(1,b):
            t.append(box.part(i*r,l*r,r,r,black,display))
makeboxes()
TDArray = make2Darray.main(b,t)

def setStart(row):
    startingpos = random.randint(0,b-2)
    startingclass  = TDArray[row, startingpos]

    startingclass.isdepth == True
    startingclass.hitboxstatus = False
    startingclass.boxstatus = False
    startingclass.vistited = True
    startingclass.inmaze = True
    startingclass.istart = True
    return startingclass

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
        if (isavalid == True):

            neigboors.append(trailclass)
    except:
        pass
    ncordsx = int(cellx)
    ncordsy = int(celly - 1)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = getneighbourof(trailclass, input)
        if(isavalid == True):
            neigboors.append(trailclass)

    except:
        pass
    ncordsx = int(cellx + 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = getneighbourof(trailclass, input)
        if (isavalid == True):
            neigboors.append(trailclass)
    except:
        pass
    ncordsx = int(cellx - 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = getneighbourof(trailclass, input)

        if (isavalid == True):
            neigboors.append(trailclass)
    except:
        pass
    return neigboors
def makemaze(input_class):
    global currentcell
    global startingthing
    global spaceleft
    neighbouringcells  = getneighbouring(input_class)
    lengthofn  = len(neighbouringcells)
    if(lengthofn == 0):
        currentcell = stack.pop()
        currentcell.is_stack()

        if(len(stack) == 0):
           spaceleft = False
    else:
        currentcell = neighbouringcells[random.randint(0, lengthofn-1)]
        currentcell.ispart()
        currentcell.isvisited()
        stack.append(currentcell)
        for cells in neighbouringcells:
            pass
    half1 = round(len(TDArray[1]) / 2)-1
    half2 = round(len(TDArray[1]) / 2)-1
    middle = TDArray[half1][half2]
    for x in range(0,5):

        if(middle.inmaze == True):
            middle.is_end()
            endcell = middle
            return endcell
        else:
            half1 += 1
            half2 += 1
            middle = TDArray[half1][half2]
def runmakemaze(start):
    global currentcell
    global spaceleft
    makemaze(start)
    while(spaceleft == True):
        endcell = makemaze(currentcell)
    return endcell
def getneighbouringdepth(input, loops, lastcell):
    cellx = numpy.where(TDArray == input)
    cellx = cellx[0]
    celly = numpy.where(TDArray == input)
    celly = celly[1]
    neigboors = []
    ncordsx = int(cellx)
    ncordsy = int(celly + 1)



    trailclass = TDArray[ncordsx, ncordsy]
    isavalid = trailclass.inmaze == True

    if (isavalid and trailclass != lastcell and trailclass.isdepth == False):
        neigboors.append(trailclass)
    ncordsx = int(cellx)
    ncordsy = int(celly - 1)
    trailclass = TDArray[ncordsx, ncordsy]
    isavalid = trailclass.inmaze == True

    if (isavalid and trailclass != lastcell and trailclass.isdepth == False):
        neigboors.append(trailclass)


    ncordsx = int(cellx + 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = trailclass.inmaze == True

        if (isavalid and trailclass != lastcell and trailclass.isdepth == False):
           neigboors.append(trailclass)

    except:
        pass
    ncordsx = int(cellx - 1)
    ncordsy = int(celly)
    try:
        trailclass = TDArray[ncordsx, ncordsy]
        isavalid = trailclass.inmaze == True

        if (isavalid and trailclass != lastcell and trailclass.isdepth == False):
            neigboors.append(trailclass)
    except:
        pass
    return neigboors
def depth(input_class, loops, prev):
    
    global currentcell
    global startingthing
    global spaceleft, lastcell, stack

    lastcell = prev
    neighbouringcells  = getneighbouringdepth(input_class, loops, lastcell)
    lengthofn  = len(neighbouringcells)
    times = 0
    stack = list(dict.fromkeys(stack))
    if(currentcell.x == endcell.x and currentcell.y == endcell.y):

        print(currentcell.x, currentcell.y)
        
        return True
    if(lengthofn == 0):

        go = stack.pop(len(stack)-1)
        currentcell = go
    else:
        ban = False
        for r in TDArray:
            for c in r:
                c.iscurrentcell = False


        if((lengthofn > 1 or loops < 2) and ban == False):
            stack.append(currentcell)
            currentcell.is_instack()


        lastcell = currentcell
        currentcell = neighbouringcells[random.randint(0, lengthofn-1)]
        currentcell.isdef() 
        currentcell.isvisited()
        currentcell.iscurrent()
stack = []
spaceleft = True
startingclass = setStart(0)
endcell = runmakemaze(startingclass)
clock = pygame.time.Clock()
def main(startclass):

    global spaceleft
    global stack
    global keys
    global distance, lastcell 
    runpygame = True
    pygame.display.set_caption("Maze")
    while runpygame:
        
        display.fill((black))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                runpygame  = False
                pygame.quit()
                quit()
        random.randint(0,b)
        global currentcell
        global lastcell
        global stack, banned
        stack = [startclass]
        banned = []
        loops = 0
        now = time.time()
        depth(startclass, loops, startingclass)
        done = False
        while (True):
            done = depth(currentcell, loops, lastcell)
            loops += 1
            for r in TDArray:
                for c in r:
                    c.draw(display, b, button)
                    xw = c.x + c.w
                    yw = c.y + c.w
            pygame.draw.rect(display, red, (15, 15, 486, 486), 4)
            pygame.draw.rect(display, white, (startclass.x, startclass.y, 16.129032258064516, 16.129032258064516), 2)
            pygame.draw.rect(display, red, (endcell.x, endcell.y, 16.129032258064516, 16.129032258064516), 2)
            pygame.display.update()
            if (done == True):
                print("It took: " + str(loops) + " loops to sort")
                timetook = round((time.time() - now), 3)
                print("It took: " + str(timetook) + " seconds to sort ")
                avg = round(timetook / loops, 6)
                print("Each action took on average: " + str(avg) + " seconds")
                '''
                wb = openpyxl.load_workbook('avg.xlsx')
                                    sheet = wb['1']  # Get a sheet from the workbook.
                anotherSheet = wb.active
                c1val = sheet["C1"].value
                c1 = sheet["C1"]
                c1.value =int(c1val+1)
                writing = sheet["A"+str(c1val)]
                writing.value = timetook
                wb.save("avg.xlsx")'''
                return

main(startingclass)

