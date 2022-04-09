import pygame
from pygame.locals import *
import os
import sys
import time
import pyinputplus as pyip
import random
import numpy
from array import *
import neat
import math
import openpyxl
global button, endx, endy, lastcell, currentcell
button = True
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bluer = (0, 5000, 255)
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
        self.isstack = False
        self.istart = False
        self.isend = False
        self.isdepth = False
        self.iscurrentcell = False
    def draw(self,win):
        global button
        if(self.hitboxstatus == True):
            if(b >33):
                pygame.draw.rect(display, self.color, (self.x, self.y,  self.w,  self.w))
            elif (b >45):
                pygame.draw.rect(display, blue, (self.x, self.y,  self.w,  self.w))
            else:
                pygame.draw.rect(display, blue, (self.x, self.y, self.w,  self.w))
        if (self.isdepth == True and button == True):
            if (b > 33):
                pygame.draw.rect(display, self.color, (self.x, self.y, self.w-0.5, self.w-0.5))
            elif (b > 45):
                pygame.draw.rect(display, self.color, (self.x, self.y, self.w-0.5, self.w-0.5))
            else:
                pygame.draw.rect(display, self.color, (self.x, self.y, self.w-0.5, self.w-0.5))
        if (self.isdepth == True and button == True and self.iscurrentcell == True):
            if (b > 33):
                pygame.draw.rect(display, red, (self.x, self.y, self.w-0.5, self.w-0.5))
            elif (b > 45):
                pygame.draw.rect(display, red, (self.x, self.y, self.w-0.5, self.w-0.5))
            else:
                pygame.draw.rect(display, red, (self.x, self.y, self.w-0.5, self.w-0.5))

        if (self.isdepth == True and button == True and self.isstack == True):


            if (b > 33):
                pygame.draw.rect(display, white, (self.x, self.y, self.w - 0.5, self.w - 0.5))
            elif (b > 45):
                pygame.draw.rect(display, white, (self.x, self.y, self.w - 0.5, self.w - 0.5))
            else:
                pygame.draw.rect(display, white, (self.x, self.y, self.w - 0.5, self.w - 0.5))
    def isStart(self):
        self.hitboxstatus = False
        self.boxstatus = False
        self.vistited = True
        self.inmaze = True
        self.istart = True
    def ispart(self):
        self.hitboxstatus = False
        self.boxstatus = False
        self.vistited = True
        self.inmaze = True
    def isdef(self):
        self.hitboxstatus = False
        self.boxstatus = False
        self.vistited = True
        self.inmaze = True
        self.isdepth = True
        self.color = green
    def isvisited(self):
        self.vistited = True
    def unvisit(self):
        self.vistited = False
    def is_stack(self):
        self.istack = True
    def is_instack(self):
        self.isstack = True
    def is_end(self):
        global endx
        global endy
        self.isend = True
        self.color = red
        endx = self.x
        endy = self.y
    def iscurrent(self):
        self.iscurrentcell = True
pygame.init()
t = []
startingthing = 0
j=0

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

    startingclass.isdepth == True
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
    global endx
    global endy
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
    global spaceleft, endx, endy, lastcell, stack

    lastcell = prev
    neighbouringcells  = getneighbouringdepth(input_class, loops, lastcell)
    lengthofn  = len(neighbouringcells)
    times = 0
    stack = list(dict.fromkeys(stack))
    if(currentcell.x == endx and currentcell.y == endy):

        print(currentcell.x, currentcell.y)
        print(endx,endy)
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
runmakemaze(startingclass)


clock = pygame.time.Clock()
def main(startclass):

    global spaceleft
    global stack
    global keys
    global distance, lastcell
    runpygame = True

    pygame.display.set_caption("Maze")


    for s in TDArray[0]:
        if (s.istart == True):
            starty = s.y
            startx = s.x
    

    while runpygame:
        clock.tick(60)

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
                    c.draw(display)
                    xw = c.x + c.w
                    yw = c.y + c.w
                    

            pygame.draw.rect(display, red, (15, 15, 486, 486), 4)
            #pygame.draw.rect(display, black, (startclass.x-11, startclass.y, 26.129032258064516, 15.329032258064516))

            pygame.draw.rect(display, white, (startclass.x, startclass.y, 16.129032258064516, 16.129032258064516), 2)
            pygame.draw.rect(display, red, (endx, endy, 16.129032258064516, 16.129032258064516), 2)
            time.sleep(0.01)
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

