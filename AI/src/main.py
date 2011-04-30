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


    reset = 0
    tank = 0
    while True:
        pythoncom.PumpWaitingMessages()
        board = bot.getBoard();
        move = ai.getMove(Board(board))

        print move
        
        if move==None:
            reset+=1
            if reset > 10:                    
                print 'board reset!'
                print bot.getBoard()
                bot.clickButton('reset')
        else:
            reset = 0
            bot.swapTile(move)


        tank+=1
        if tank>23:
            bot.clickButton('colossus')
            tank=0

        sleep(0.1)



    

        

