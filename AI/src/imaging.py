import numpy as np

startX, startY = (1237,112)
offsetX, offsetY = (15,44)
tileSize = 80

colors = {
    254 : 'y',
    87  : 'g',
    40  : 'b',
    63  : 'k',
    106 : 'p',
    240 : 'r', 
}

def FindJewels(img):
    '''Assuming we get the raw PIL array from screen capture'''

    board = [[0]*8 for i in range(8)]
        
    for x in range(8):
        for y in range(8):
            (samplex,sampley) = (startX+offsetX+tileSize*x,
                                 startY+offsetY+tileSize*y)

            board[x][y] = colors.setdefault(img.getpixel((samplex,sampley))[0],'x')
    return board


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    img = plt.imread('tests/screenshot.png')
    board = FindJewels(img)
