import numpy as np

startX, startY = (1237,112)
offsetX, offsetY = (15,44)
tileSize = 80

colors = {
    (254,254,172) : 'y',
    (87,201,33)  : 'g',
    (40,146,246)  : 'b',
    (63,63,62)  : 'k',
    (106,34,113) : 'p',
    (240,62,25) : 'r', 
}

def FindJewels(img):
    '''Assuming we get the raw PIL array from screen capture'''

    board = [[0]*8 for i in range(8)]
        
    for x in range(8):
        for y in range(8):
            (samplex,sampley) = (startX+offsetX+tileSize*x,
                                 startY+offsetY+tileSize*y)

            board[x][y] = colors.setdefault(img.getpixel((samplex,sampley)),'x')
    return board




eStartX,eStartY = (1228,810)
eEndX = 1881
eWidth = 654

def FindEnergy(img):
    for x in range(eWidth+1): #include up to width limit
        if img.getpixel((eStartX + x , eStartY))==(0,0,0):
            break
    return x/float(eWidth)*1000





if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import Image
    img = Image.fromarray(plt.imread('../../tests/screenshot.png'))
    board = FindJewels(img)
