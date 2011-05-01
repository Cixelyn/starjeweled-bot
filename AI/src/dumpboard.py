from StupidBot import StupidBot
from StarJeweledBot import StarjeweledBot
from random import randint

#Quick Debugging Script to Dump the Current Game State
    
ai = StupidBot()
bot = StarjeweledBot("Starcraft II")

c = bot.capture()
b = bot.getBoard(c)
e = bot.getEnergy(c)

print "Energy: %s" % e
