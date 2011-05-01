'''Main Script to Run Bots'''

import pythoncom, pyHook, sys
from time import sleep
from Board import Board
from StupidBot import StupidBot
from StarJeweledBot import StarjeweledBot
from random import randint


def OnKbEvent(event):
    print event.ScanCode
    if(event.ScanCode==41):
        print 'exiting'
        sys.exit()


if __name__ == "__main__":

    hm = pyHook.HookManager()
    hm.KeyDown = OnKbEvent
    hm.HookKeyboard()
    
    ai = StupidBot()
    bot = StarjeweledBot("Starcraft II")


    reset = 0
    build = 0
    while True:
        pythoncom.PumpWaitingMessages()
        img = bot.capture()
        board = bot.getBoard(img)
        energy = bot.getEnergy(img)
        move = ai.getMove(Board(board))

        print move
        
        if move==None:
            reset+=1
            if reset > 10:                    
                print 'board reset!'
                print bot.getBoard(img)
                bot.clickButton('reset')
        else:
            reset = 0
            bot.swapTile(move)


        build+=1
        if energy>500:
            bot.clickButton('colossus')

        sleep(0.05)


