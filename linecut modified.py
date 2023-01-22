# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:53:08 2023

@author: Sagar Dam
"""
''' 
This is a code to get the linecuts through some point of any greyscale image. The point index should be given and 
the lines are in some 10 degree interval. By changing the linecut degree intervals, we can take any number of 
linecuts through the given point. 
'''

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from PIL import Image, ImageDraw

# Load the image
image_path='D:\\data Lab\\frog\\Granouille allignment\\16jan2023\\ids raw\\5_33.png'
image = io.imread(image_path)
image2 = Image.open(image_path)

point=[100,400]    #The point for which the linecut is needed.
x=point[0]
y=point[1]

X=image.shape[0]-1
Y=image.shape[1]-1

theta_degree=np.linspace(0,90,10)
theta=theta_degree*np.pi/180
#print(theta)
phi_degree=np.linspace(80,10,8)
phi=phi_degree*np.pi/180
#print(phi)

def draw_on_image(image,x,y):
    draw = ImageDraw.Draw(image)
    draw.line((start_point[1],start_point[0],end_point[1],end_point[0]), fill=(255, 0, 0), width=2)
    return(image)
    
def linecut_function(start_point,end_point,image,image2):
    # Use the numpy function linspace to get the coordinates of the line
    num=round(np.sqrt((start_point[0]-end_point[0])**2+(start_point[1]-end_point[1])**2))
    x, y = np.linspace(start_point[0], end_point[0], num), np.linspace(start_point[1], end_point[1], num)
    image2=draw_on_image(image2, start_point,end_point)
    # Get the grayscale values along the line
    gray_values = image[x.astype(int),y.astype(int)]
    linecut=[]
    for i in range(len(gray_values)):
        linecut_value=np.sqrt((gray_values[i][0])**2+(gray_values[i][1])**2+(gray_values[i][2])**2)
        linecut.append(linecut_value)
        
    return(linecut,image2)

#plt.imshow(image)


for i in range(len(theta)):
    if(np.tan(theta[i])<=(x/(Y-y))):
        start_point=[round(x+y*np.tan(theta[i])),round(0)]
        end_point=[round(x-(Y-y)*np.tan(theta[i])),round(Y)]
        linecut,image2=linecut_function(start_point,end_point,image,image2)
        plt.plot(linecut)
        plt.title("theta=%d"%(theta_degree[i]))
        plt.xlabel('start: %f'%start_point[0]+',%f'%start_point[1]+'\n end: %f'%end_point[0]+',%f'%end_point[1])
        plt.show()
    elif((x/(Y-y))<np.tan(theta[i])<=((X-x)/y)):
        start_point=[round(x+y*np.tan(theta[i])),round(0)]
        end_point=[round(0),round(y+x/np.tan(theta[i]))]
        linecut,image2=linecut_function(start_point,end_point,image,image2)
        plt.plot(linecut)
        plt.title("theta=%d"%(theta_degree[i]))
        plt.xlabel('start: %f'%start_point[0]+',%f'%start_point[1]+'\n end: %f'%end_point[0]+',%f'%end_point[1])

        plt.show()
    elif(((X-x)/y<np.tan(theta[i])<np.tan(89.5*np.pi/180))):
        start_point=[round(X),round(y-(X-x)/np.tan(theta[i]))]
        end_point=[round(0),round(y+x/np.tan(theta[i]))]
        linecut,image2=linecut_function(start_point,end_point,image,image2)
        plt.plot(linecut)
        plt.title("theta=%d"%(theta_degree[i]))
        plt.xlabel('start: %f'%start_point[0]+',%f'%start_point[1]+'\n end: %f'%end_point[0]+',%f'%end_point[1])
        plt.show()
    else:
        start_point=[round(X),round(y)]
        end_point=[round(0),round(y)]
        linecut,image2=linecut_function(start_point,end_point,image,image2)
        plt.plot(linecut)
        plt.title("theta=%d"%(theta_degree[i]))
        plt.xlabel('start: %f'%start_point[0]+',%f'%start_point[1]+'\n end: %f'%end_point[0]+',%f'%end_point[1])
        plt.show()
        
for i in range(len(phi)):
    if(np.tan(phi[i])<=((X-x)/(Y-y))):
        start_point=[round(x-y*np.tan(phi[i])),round(0)]
        end_point=[round(x+(Y-y)*np.tan(phi[i])),round(Y)]
        linecut,image2=linecut_function(start_point,end_point,image,image2)
        plt.plot(linecut)
        plt.title("theta=%d"%(180-phi_degree[i]))
        plt.xlabel('start: %f'%start_point[0]+',%f'%start_point[1]+'\n end: %f'%end_point[0]+',%f'%end_point[1])
        plt.show()
    elif(((X-x)/(Y-y))<np.tan(phi[i])<=(x/y)):
        start_point=[round(x-y*np.tan(phi[i])),round(0)]
        end_point=[round(X),round(y+(X-x)/np.tan(phi[i]))]
        linecut,image2=linecut_function(start_point,end_point,image,image2)
        plt.plot(linecut)
        plt.title("theta=%d"%(180-phi_degree[i]))
        plt.xlabel('start: %f'%start_point[0]+',%f'%start_point[1]+'\n end: %f'%end_point[0]+',%f'%end_point[1])
        plt.show()
    else:
        start_point=[round(0),round(y-x/np.tan(phi[i]))]
        end_point=[round(X),round(y+(X-x)/np.tan(phi[i]))]
        linecut,image2=linecut_function(start_point,end_point,image,image2)
        plt.plot(linecut)
        plt.title("theta=%d"%(180-phi_degree[i]))
        plt.xlabel('start: %f'%start_point[0]+',%f'%start_point[1]+'\n end: %f'%end_point[0]+',%f'%end_point[1])
        plt.show()

image2=np.asarray(image2)
plt.imshow(image2)