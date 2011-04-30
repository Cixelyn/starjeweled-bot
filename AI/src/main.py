'''Main Script to Run Bots'''

import pythoncom, pyHook, sys
from time import sleep
from Board import Board
from StupidBot import StupidBot
from StarJeweledBot import StarjeweledBot



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


    while True:
        pythoncom.PumpWaitingMessages()
        board = bot.getBoard();
        move = ai.getMove(Board(board))

        if move==None:
            print 'board reset!'
            bot.sendKeys('z')
        else:
            print move
            bot.swapTile(move)

        sleep(0.1)



    

        

