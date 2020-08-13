import pygame
from pygame.locals import *
import os
import sys
import time
import pyinputplus as pyip
from array import *
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
        box.hitbox = (self.x, self.y, self.w, self.l)

    def draw(win,self):
        if(b >33):
            pygame.draw.rect(display, box.color, (box.x, box.y, box.w, box.l),2)
        elif (b >45):
            pygame.draw.rect(display, box.color, (box.x, box.y, box.w, box.l),1)
        else:
            pygame.draw.rect(display, box.color, (box.x, box.y, box.w, box.l),3)
    def isStart():
        pass
t = []
TDArray = [[]]
varnamelist = []
j=0
run = True
display_width = 550
display_height =550
pygame.init()
display= pygame.display.set_mode((display_width, display_height))
display.fill((black))
def maketheboxes(vari):
    for i in range(1,b):
        for l in range(1,b):
            vari = box(i*r,l*r,r,r,thing,display)
            vari.draw(display)
def runmakeboxes():
    for x in range(1,(b*b+1)):
        varname  = "box"+str(x)
        varnamelist.append(varname)
        maketheboxes(varname)
    make2D()
def make2D():
    num = 0
    for y in range(0,b):
        insert = []
        for x in range(0,b):
            insert.append(varnamelist[num])
            num+=1
        TDArray.insert(y,insert)

runmakeboxes()
pygame.display.set_caption("Maze")

while run:
    display.fill((black))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run  = False
    for r in TDArray:
        for c in r:
            #c.draw(display)
            print(c)


    pygame.display.update()




pygame.quit()
quit()
