import cv2
import numpy as np
import myUtils
#################### Parameters ###################
# Basic options
showImage = True # show the image result (True or False)
saveImage = False # save the image result (True or False)
imageName = 'result_04' # name of the image

# Image dimensions [pixel]
width = 500 #[px]
height= 500 #[px]

# Hexagons parameters
padding   = 0   #[px], distance between hexagons
diagonal  = 20  #[px]
thickness = 2   #[px], edge thickness
color  = (0,0,0, 255) #[RGB Alpha], alpha in [0,255] (0:transparent, 255:opaque)
orientation = 0 #[degree] (beta test / bugado)
filled = False

# Numerates
# cv2.FONT_HERSHEY_COMPLEX
# cv2.FONT_HERSHEY_COMPLEX_SMALL
# cv2.FONT_HERSHEY_PLAIN
# cv2.FONT_HERSHEY_SCRIPT_COMPLEX
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
# cv2.FONT_HERSHEY_TRIPLEX
# cv2.FONT_ITALIC
hexagons_enumerated = False
number_font  = cv2.FONT_HERSHEY_PLAIN
number_scale = cv2.getFontScaleFromHeight(number_font, height, thickness=thickness)
number_color = (0,0,0,255) #[RGB-A]
###################################################

if __name__ == '__main__':
    print('[INFO] Creating blank image...')
    ## Create image
    image = np.ones((height, width, 4), dtype='uint8')*255
    image[:,:,3] = np.zeros_like(image[:,:,3])    
    print('Done.')

    print('[INFO] Generating hexagons...')
    ## Create hexagons
    hexagons, centers = myUtils.hexagonPattern(0,0,width, height, diagonal, padding=padding, ori=orientation)
    print('Done.')

    print('[INFO] Drawing...')
    ## Draw hexagons
    if hexagons_enumerated:
        myUtils.enumerateHexagons(image, centers, diagonal, scale=scale, color=number_color)
    myUtils.drawHexagons(image, hexagons, thickness=thickness, color=color, filled=filled)
    print('Done.')

    # Show image
    if showImage:
        cv2.imshow('Result', image)
    # Save image
    if saveImage:
        print("Salving Image...")
        cv2.imwrite(f'{imageName}.png', image)
        print(f"Image saved: {imageName}.png")
    
    # necessary to show the image
    cv2.waitKey(0)