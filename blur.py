
from PIL import Image, ImageChops
import os
import sys

class blur():
    def __init__(self,imageSrc:str):
        self.image = Image.open(imageSrc)
        self.w,self.h =  self.image.size
    
    def getAroundPixels(self,x,y):
        #4, 6 , 9
        pos = [
            [(x-1,y-1),(x,y-1),(x+1,y-1)],
            [(x-1,y),(x,y),(x+1,y)],
            [(x-1,y+1),(x,y+1),(x+1,y+1)]
        ]

        inRangeLT = lambda v: True if v[0]>=0 and v[1] >=0 else False  #função que determina se o pixel esta fora da imagem a esquerda e a cima
        inRangeRD = lambda v: True if v[0]<self.w and v[1]<self.h else False #função que determina se o pixel esta fora da imagem a direita e a baixo

        pos = [[y for y in x if inRangeLT(y) and inRangeRD(y) ] for x in pos] # loop que constroi a listagem com apenas os pixels validos

        return pos
    
    def calcBlur(self,x,y):
        roudPixels = self.getAroundPixels(x,y)

        pos = [[{"x":y[0],"y":y[1],"RGB":self.image.getpixel((y[0], y[1]))} for y in x] for x in roudPixels]

        qtd = sum([len(x) for x in pos])
        cr = int(sum([sum([y["RGB"][0] for y in x]) for x in pos])/qtd)
        cg = int(sum([sum([y["RGB"][1] for y in x]) for x in pos])/qtd)
        cb = int(sum([sum([y["RGB"][2] for y in x]) for x in pos])/qtd)

        return (cr,cg,cb)

    def convertBlur(self):
        for x in range(self.w):
            for y in range(self.h):
                r,g,b = self.calcBlur(x,y)
                self.image.putpixel((x,y), (r,g,b))

image = blur("test-image.png")

image.convertBlur()



