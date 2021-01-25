from PIL import Image, ImageChops
import os
import sys

"""
execute with:  python esss_test_4.py -blur "test-image.png" 3 10 for test
"""

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

    def calcBlur(self,x,y,radius,weight):
        roudPixels = self.getAroundPixels(x,y,radius)

        center=int((radius*2+1)/2)
        pos = [[{"x":y[0],"y":y[1],"RGB":self.image.getpixel((y[0], y[1]))} for y in x] for x in roudPixels]

        qtd = sum([len(x) for x in pos])-1 + weight
        calcweight = lambda obj,ps: obj["RGB"][ps]*weight if obj["x"]==x and obj["y"]==y else obj["RGB"][ps]
        cr = int(sum([sum([calcweight(i,0) for i in v]) for v in pos])/qtd)
        cg = int(sum([sum([calcweight(i,1) for i in v]) for v in pos])/qtd)
        cb = int(sum([sum([calcweight(i,2) for i in v]) for v in pos])/qtd)

        return (cr,cg,cb)

    def convertBlur(self,radius,weight):

        for x in range(self.w):
            for y in range(self.h):
                r,g,b = self.calcBlur(x,y,radius,weight)
                self.image.putpixel((x,y), (r,g,b))


if __name__ == "__main__":   
    method = sys.argv[1]
    image = sys.argv[2]
    radius = int(sys.argv[3])
    weight = int(sys.argv[4])
    if method == "-blur":
        image = blur(image) 
        image.convertBlur(radius,weight)
        image.image.save(f"test-image-blur-radius{radius}-weight{weight}.png")  
    
    else:
        print("metodo não conhecido!")

    
    




