'''Main Script to Run Bots'''
import pythoncom, pyHook, sys
from time import sleep
from Board import Board
from StupidBot import StupidBot
from StarJeweledBot import StarjeweledBot
from random import randint


###
### SETUP BUILD ORDER HERE
###
bo = [('colossus',700),('mutalisk',200)]



def OnKbEvent(event):
    print event.ScanCode
    if(event.ScanCode==41):
        print 'exiting'
        sys.exit()


if __name__ == "__main__":

    #Setup Keyboard Hooking
    hm = pyHook.HookManager()
    hm.KeyDown = OnKbEvent
    hm.HookKeyboard()

    #Initialize Bot
    ai = StupidBot()
    bot = StarjeweledBot("Starcraft II")
    resetDelay = buildNumber = buildDelay = 0

    #Main Loop
    while True:

        #Image Analysis Code
        pythoncom.PumpWaitingMessages()
        img = bot.capture()
        board = bot.getBoard(img)
        energy = bot.getEnergy(img)
        move = ai.getMove(Board(board))
        print move

        #Reset Code
        if move==None:
            resetDelay+=1
            buildDelay+=1
            if resetDelay > 10:                    
                print 'board reset!'
                print bot.getBoard(img)
                bot.clickButton('reset')
        else:
            resetDelay = 0
            bot.swapTile(move)

        #Building Code
        i = buildNumber%len(bo)
        if energy>bo[i][1]:
            sleep(0.1)
            bot.clickButton(bo[i][0])
            buildNumber+=1
            buildDelay=0


        #Delay
        sleep(0.1)


