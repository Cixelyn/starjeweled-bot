from random import randint
from screenbot import Bot
from imaging import FindJewels

startX, startY = (1237,112)
tileSize = 80

class StarjeweledBot(Bot):

    def clickTile(self,(x,y)):
        posx = startX + x*tileSize + randint(10,70)
        posy = startY + y*tileSize + randint(10,70)
        self.click((posx,posy))
        
    def swapTile(self,(tile1,tile2)):
        self.clickTile(tile1)
        self.clickTile(tile2)

    def getBoard(self):
        return FindJewels(self.capture())

    def resetBoard(self):
        posx = 1365 + randint(10,60)
        posy = 1077 + randint(10,60)
        self.click((posx,posy))
        

if __name__ == "__main__":
    bot = StarjeweledBot("StarCraft II")
    bot.swapTile((1,1),(1,2))
    bot.swapTile((5,5),(4,5))
    bot.swapTile((3,1),(3,2))
