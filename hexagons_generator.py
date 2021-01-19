import cv2
import numpy as np
import myUtils

#################### Parameters ###################
# Algumas definições:
# [px]: indica que a unidade está em pixels
## Basic options
showImage = False # show the image result (True or False)
saveImage = True # save the image result (True or False)
imageName = 'result' # name of the image

# Dimensões da imagem de saída [px]
# largura [px]
width = 600
# altura [px]
height= 480

## Parâmetros relacionados à geração dos hexagonos
# Espaço entre os hexagonos [px]
padding   = 10
# Tamanho do hexagono (do centro dele até qualquer um dos vertices) [px]
diagonal  = 50
# espessura das bordas dos hexagonos (caso a opção filled seja habilitada, essa opção não terá efeito)
# [px]
thickness = 2
# cor do hexagono em RGBa (R:red, G:green, B:blue, a: alpha (transparência))
# Cada um dos valores deve estar no intervalo [0,255]
# alpha = 255 => 100% transparente
# (R,G,B,alpha)
color  = (255,0,0, 255)
# Rotaciona os hexagonos
# unidade em graus [degree]
#(beta test / bugado)
orientation = 0
# Onde começa a desenhar os hexagonos
# coordenada x de inicio [px]
startx    = diagonal
# coordenada y de inicio [px]
starty    = diagonal
# onde termina de desenhar os hexagonos
# ultima coordenada x
endx      = width - diagonal
# ultima coordenada y
endy      = height - diagonal
# habilita o hexagonos preenchidos (True para habilitar / False para desabilitar)
filled = False

## Parâmetros relacionados a númeração dos hexagonos
enable_enumeration = True
# Font options (pick up one and change the number_font)
# Lista de fontes disponiveis, basta copiar um desses nomes e atribuir na variavel: number_font
# cv2.FONT_HERSHEY_COMPLEX
# cv2.FONT_HERSHEY_COMPLEX_SMALL
# cv2.FONT_HERSHEY_PLAIN
# cv2.FONT_HERSHEY_SCRIPT_COMPLEX
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
# cv2.FONT_HERSHEY_TRIPLEX
# cv2.FONT_ITALIC
number_font  = cv2.FONT_HERSHEY_PLAIN
# Tamanho dos caracteres no intervalo [0, inf],
number_scale = 2.0
# cor dos números em RGBA
number_color = (0,0,0,255) #[RGB-A]
# deslocamento extra nos números no eixo x (x cresce da direita pra esquerda na imagem ->)
number_offsetx = 0
# deslocamento extra nos números no eixo x (y cresce de cima pra baixo na imagem \/)
number_offsety = 0
###################################################

if __name__ == '__main__':
    print('[INFO] Creating blank image...')
    ## Create image
    image = np.ones((height, width, 4), dtype='uint8')*255
    image[:,:,3] = np.zeros_like(image[:,:,3])    
    print('Done.')

    print('[INFO] Generating hexagons...')
    ## Create hexagons
    hexagons, centers = myUtils.hexagonPattern(startx, 
                                               starty,
                                               endx, 
                                               endy, 
                                               diagonal, 
                                               padding=padding, 
                                               ori=orientation)
    print('Done.')

    print('[INFO] Drawing...')
    ## Draw hexagons
    color = [color[2],color[1],color[0],color[3]]
    number_color = [number_color[2],number_color[1],number_color[0],number_color[3]]
    if enable_enumeration:
        myUtils.enumerateHexagons(image=image, 
                                  positions=centers,
                                  diagonal=diagonal,
                                  offsetx=number_offsetx, 
                                  offsety=number_offsety,
                                  scale= number_scale, 
                                  color=number_color,
                                  font=number_font)
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