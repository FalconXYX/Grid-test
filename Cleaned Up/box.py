black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bluer = (0, 50, 255)
import pygame
class part():
    def __init__(self,x,y,l,w,colorin,display):
        self.x = x
        self.y = y
        self.l = l+2
        self.w = w+2
        self.colour = colorin
        self.hitbox = (self.x, self.y, self.w, self.l)
        self.hitboxstatus = True
        self.boxstatus = True
        self.vistited = False
        self.inmaze  = False
        self.istack = False
        self.isstack = False
        self.isend = False
        self.isdepth = False
        self.iscurrentcell = False
    def draw(self,dis,area,buttontemp):
        if(self.hitboxstatus == True):
            if(area >33):
                pygame.draw.rect(dis, blue, (self.x, self.y,  self.w,  self.w))
            elif (area >45):
                pygame.draw.rect(dis, blue, (self.x, self.y,  self.w,  self.w))
            else:
                pygame.draw.rect(dis, blue, (self.x, self.y, self.w,  self.w))
        else:
            if (self.isdepth == True and buttontemp == True):
                self.colour = green
            if (self.isdepth == True and buttontemp == True and self.iscurrentcell == True):
                self.colour = red     
            if (self.isdepth == True and buttontemp == True and self.isstack == True):
                self.colour = white
            colortemp = self.colour
            
            if (area > 33):
                pygame.draw.rect(dis, self.colour, (self.x, self.y, self.w-0.5, self.w-0.5))
            elif (area > 45):
                pygame.draw.rect(dis, self.colour, (self.x, self.y, self.w-0.5, self.w-0.5))
            else:
                pygame.draw.rect(dis, colortemp, (self.x, self.y, self.w-0.5, self.w-0.5))
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
    def isvisited(self):
        self.vistited = True
    def unvisit(self):
        self.vistited = False
    def is_stack(self):
        self.istack = True
    def is_instack(self):
        self.isstack = True
    def is_end(self):
        self.isend = True
        self.colour = red
    def iscurrent(self):
        self.iscurrentcell = True
