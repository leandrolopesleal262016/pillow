from PIL import Image, ImageChops
import glob, os

image1 = "test-image.png" 
#image2 = "imagens\jarvis.jpg"


# Carrega pro python
img1 = Image.open(image1)
# img2 = Image.open(image2)

print("img1 original",img1.size, img1.mode)
# print("img2 original",img2.size, img2.mode)

# img = Image.open(path)
# width, height = img1.size
# for x in range(width):
#     for y in range(height):
#         r, g, b  = img1.getpixel((x, y))
#         print("R: {:3}, G: {:3}, B: {:3}".format(r, g, b))
matriz = []
width, height = img1.size
for x in range(width):
    for y in range(height):
        r, g, b  = img1.getpixel((x, y))
        
        rgb = (r,0,0)
        matriz.append(rgb)

#matriz = tuple(matriz)

img1.putdata(matriz)

# for x in range(width):
#     for y in range(height):
#         print(img1.putpixel((x,y), matriz[y]))
        
# img1.putpixel((x,y), matriz)

img1.save("img_red.jpeg","JPEG")


# redimensionar 
# size = 500,500
# img1.resize(size).show()
# img1.save("img1_ampliada.jpeg","JPEG")
# print("img1 resize", img1.size)

# img2.resize(size).show()
# img2.save("img2_ampliada.jpeg","JPEG")
# print("img2 resize", img2.size)

# Sobreposição das imagens
# merged = ImageChops.multiply(img1,img2)
# merged.resize(size).show()

# Escala de cinza
# greyscale = img1.convert('L')
# greyscale.show() 




# miniatura
# size = 128,128
# img1.thumbnail(size)
# img1.save("img1.thumbnail","JPEG") # salva na pasta atual a miniatura da imagem
# img1.show()
# print("img1 thumbnail", img1.size)

# img1.rotate(45).show()


