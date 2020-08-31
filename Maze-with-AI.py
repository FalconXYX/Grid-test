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
        self.istart = False
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
        self.inmaze = True
        self.istart = True
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
    def is_end(self):
        global endx
        global endy
        self.color = red
        endx = self.x
        endy = self.y
class person():
    def __init__(self,x,y,l,w,display):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.color = color
        self.vel = 0.2
        self.deaths = 0
        self.distance = 1
        self.hitbox = (self.x, self.y, self.w, self.l)
        self.count = 0
    def move(self):

        if keys[K_ESCAPE]:
            run = False
    def draw(self,win):
        pygame.draw.rect(display, red, (self.x, self.y, self.w, self.w))
    def death(self,win):
        self.x = startx+4
        self.y =starty+2
        self.deaths +=1


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
global startingclass
def setStart(row):
    global startingclass
    startingpos = random.randint(0,b-2)
    startingclass  = TDArray[row, startingpos]
    startingclass.isStart()
    print(startingclass.isStart())
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
        if (startingthing == 0):
            startingthing = 1
            currentcell.is_end()

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
def runmakemaze(start):
    global currentcell
    global spaceleft
    makemaze(start)
    while(spaceleft == True):
        makemaze(currentcell)
stack = []
spaceleft = True
setStart(0)

clock = pygame.time.Clock()
def main(genomes, config):
    global spaceleft
    global stack
    global keys
    global distance
    runpygame = True

    pygame.display.set_caption("Maze")
    players = []
    ge = []
    nets = []
    for _,g in genomes:
        for s in TDArray[0]:
            if (s.istart == True):
                starty = s.y
                startx = s.x
        players.append(person(startx + 4, starty + 2, 4, 4, display))
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)

    while runpygame:
        clock.tick(60)

        display.fill((black))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                runpygame  = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if (len(players) < 1):
            runpygame == False
            break

        for player in players:
            player.move()
            noaction = True
            number = players.index(player)
            p = [player.x,player.y,player.distance]
            output = nets[number].activate(p)
            if output[0] >= 0.5 and output[0] <= 1:
                if (player.y > 18):
                    player.y -= player.vel
                    noaction == False
            if output[0] >= 0 and output[0] <= 0.5:
                if player.x > 21:
                    player.x -= player.vel
                    noaction == False
            if output[0] >= 0 and output[0] <= -0.5:
                if player.y < 495:
                    player.y += player.vel
                    noaction == False
            if output[0] >= -0.5 and output[0] <= -1:
                if player.x < 494:
                        player.x += player.vel
                        noaction == False
            if(noaction == True):
                player.count +=1
                if(player.count > 150):
                    ge[number].fitness -= 1
                    players.pop(number)
                    ge.pop(number)
                    nets.pop(number)
                    player.count = 0

        random.randint(0,b)

        for r in TDArray:
            for c in r:
                c.draw(display)
                xw = c.x+c.w
                yw = c.y+c.w
                for player in players:
                    if (c.inmaze == False):
                        if(player.x > c.x and player.x < xw):
                            if(player.y > c.y and player.y < yw):

                                x= players.index(player)
                                ge[x].fitness -=3
                                players.pop(x)
                                ge.pop(x)
                                nets.pop(x)
                                try:
                                    additive = 45-(player.distance / 10)
                                    print(additive)
                                    ge[x].fitness += additive
                                except:
                                    runpygame == False
                                    break






                    if (c.inmaze == True):
                        if(player.x > endx and player.x < endx+c.w):
                            if(player.y > endy and player.y < endy+c.w):
                                ge[x].fitness == 1000
        for player in players:
            x = players.index(player)
            ge[x].fitness += 0.01

        for player in players:
            xdiff = player.x
            ydiff = player.y
            xdiff = xdiff*xdiff
            ydiff = ydiff*ydiff
            distance = xdiff+ydiff
            player.distance  = round(math.sqrt(distance))

        pygame.draw.rect(display, red, (15, 15, 486, 486), 4)
        #pygame.draw.rect(display, black, (startx-10, starty, 26.129032258064516, 15.329032258064516))
        for player in players:
            player.draw(display)
        pygame.draw.rect(display, green, (startx, starty, 16.129032258064516, 16.129032258064516), 2)
        pygame.draw.rect(display, red, (endx, endy, 16.129032258064516, 16.129032258064516), 2)
        pygame.display.update()


def runsim(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)
    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))
    # Run for up to 50 generations.
    winner = p.run(main, 75)
    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))



local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config-feedforward.txt')
runsim(config_path)


