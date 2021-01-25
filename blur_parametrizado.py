from PIL import Image, ImageChops
import os
import sys

class blur():
    def __init__(self,imageSrc:str):
        self.image = Image.open(imageSrc)
        self.w,self.h =  self.image.size
    
    def getAroundPixels(self,x,y,radius):       
       
        cntr = [-radius+x for x in range(radius*2+1)]
        pos = [[(x-xx,y-yy) for xx in cntr] for yy in cntr]       

        inRangeLT = lambda v: True if v[0]>=0 and v[1] >=0 else False  
        inRangeRD = lambda v: True if v[0]<self.w and v[1]<self.h else False 

        pos = [[y for y in x if inRangeLT(y) and inRangeRD(y) ] for x in pos] 

        return pos
    
    def calcBlur(self,x,y,radius):

        roudPixels = self.getAroundPixels(x,y,radius)

        pos = [[{"x":y[0],"y":y[1],"RGB":self.image.getpixel((y[0], y[1]))} for y in x] for x in roudPixels]

        qtd = sum([len(x) for x in pos])
        cr = int(sum([sum([y["RGB"][0] for y in x]) for x in pos])/qtd)
        cg = int(sum([sum([y["RGB"][1] for y in x]) for x in pos])/qtd)
        cb = int(sum([sum([y["RGB"][2] for y in x]) for x in pos])/qtd)

        return (cr,cg,cb)

    def convertBlur(self,radius):

        for x in range(self.w):
            for y in range(self.h):
                r,g,b = self.calcBlur(x,y,radius)
                self.image.putpixel((x,y), (r,g,b))
 

if __name__ == "__main__":   
    method = "-blur" #sys.argv[1]
    image = "test-image.png" #sys.argv[2])
    radius = 5 # radius = (sys.argv[3])
    weight = 1 # weight = (sys.argv[4])
    if method == "-blur":
        image = blur(image) 
        image.convertBlur(radius)
        image.image.save(f"test-image-blur-radius{radius}-weight{weight}.png")  
    
    else:
        print("metodo não conhecido!")

    
    




