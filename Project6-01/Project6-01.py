# -*- coding: utf-8 -*-
"""
Created on Fri May  5 08:47:39 2023

@author: thegs
"""
from PIL import Image
im=Image.open("Image.jpg")
img=im.load()

x,y =im.size
x1=0
y1=0
while(x1<x):
    [r,g,b]=img[x1,y1]
    r = int(round( ( r / 255.0 ) * 5 ) * 51)
    g = int(round( ( g / 255.0 ) * 5 ) * 51)
    b = int(round( ( b / 255.0 ) * 5 ) * 51)
    value = (r,g,b)
    im.putpixel((x1,y1), value)    
    x1+=1
    if(x1==x and y1!=y):
        x1=0
        y1+=1
    if(y1==y):
        break
im.save("output.jpg")