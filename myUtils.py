import cv2
import numpy as np
import math


################### Constants ####################
# Solid colors (alpha = 255)
WHITE = (255,255,255,255)
BLACK = (0,0,0, 255)                      
##################################################

def rotate(src, angle):
    angle = np.radians(angle)
    R = np.array([[np.cos(angle), -np.sin(angle)], 
                  [np.sin(angle), np.cos(angle)]])
    
    return R.dot(src.reshape(2,1))

def createHexagon(center, diagonal, ori=0.0):
    center = np.array(center).reshape(2,1)
    vertices = []
    
    vertex0 = np.array(([diagonal, 0]), dtype='double').reshape(2,1)
    vertex0 = rotate(vertex0,30.0 + ori)
    for i in range(6):
        v = rotate(vertex0, 60.0*i) + center
        vertices.append( np.round(v.reshape(1,2)).astype('int') )
    return vertices

def hexagonPattern(startx, starty, endx, endy, diagonal, ori = 0.0, padding=0):
    centers  = []
    vertices = []
    
    offsetx = round( 2.0*diagonal * math.cos( math.radians(30.0 + ori) )) + padding
    offsety = round( 3.0*diagonal * math.sin( math.radians(30.0 + ori) )) + padding

    offsetx = int(offsetx)
    offsety = int(offsety)
    
    for i, y in enumerate(range(starty, endy, offsety)):
        if (i % 2) == 0:
            stx = startx
        else:
            stx = int(startx + offsetx/2)
        for x in range(stx, endx, offsetx):
            center = [x,y]
            centers.append(center)
            vertices.append(createHexagon(center, diagonal, ori))
    return [vertices, centers]

def drawHexagons(image, hexagons, thickness=2, filled=False, color=(0,0,0,255)):
    hexagons = np.array(hexagons).reshape(-1,6,2)
    if filled:
        cv2.fillPoly(image, hexagons, color, lineType=cv2.LINE_AA)
    else:
        cv2.polylines(image, hexagons, True, color=color, thickness=thickness, lineType=cv2.LINE_AA)

def enumerateHexagons(image, positions, diagonal, offsetx=0, offsety=0, scale=0.7, color=BLACK, font=cv2.FONT_HERSHEY_PLAIN):
    radius = int(round(diagonal * math.cos( math.radians(30) )))
    for n,c in enumerate(positions):
        pt = (c[0] + offsetx - radius, c[1] + offsety + radius//3)
        cv2.putText(image, '{:04d}'.format(n), org=pt, fontFace=font, fontScale=scale, color=color, thickness=2)