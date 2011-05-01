from random import randint
from screenbot import Bot
from imaging import FindJewels,FindEnergy

startX, startY = (1237,112)
tileSize = 80

buttonSize = 60
buttonPos = {
    'tank':     (1596,876),
    'reset':    (1365,1077),
    'colossus': (1673,876),
    'ultralisk':(1673,953),
    'ghost':    (1442,953),
    'hydralisk':(1442,876),
    'mutalisk': (1519,876),
}
    


class StarjeweledBot(Bot):

    def clickTile(self,(x,y)):
        posx = startX + x*tileSize + randint(10,70)
        posy = startY + y*tileSize + randint(10,70)
        self.click((posx,posy))
        
    def swapTile(self,(tile1,tile2)):
        self.clickTile(tile1)
        self.clickTile(tile2)

    def getBoard(self,img):
        return FindJewels(img)

    def getEnergy(self,img):
        return FindEnergy(img)

    def clickButton(self,name):
        (x,y) = buttonPos[name]
        posx = x + randint(10,buttonSize)
        posy = y + randint(10,buttonSize)
        self.click((posx,posy))

        
        

if __name__ == "__main__":
    bot = StarjeweledBot("StarCraft II")
    bot.clickButton('tank')
