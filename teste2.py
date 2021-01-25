
from PIL import Image, ImageChops
import os
import sys


def convertRedImage(imageSrc:str)->Image:
    
    img = Image.open(imageSrc)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x,y), (r,0,0))

    return img

def convertGreenImage(imageSrc:str)->Image:
    
    img = Image.open(imageSrc)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x,y), (0,g,0))

    return img

def convertBlueImage(imageSrc:str)->Image:
    
    img = Image.open(imageSrc)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x,y), (0,0,b))
    return img

if __name__ == "__main__":   
    original = sys.argv[1]
    convertGreenImage(original).save("greenConverted.jpg")
    convertRedImage(original).save("redConverted.jpg")
    convertBlueImage(original).save("blueConverted.jpg")
    




