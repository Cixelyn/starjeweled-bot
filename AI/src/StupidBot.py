import BotTemplate

class StupidBot(BotTemplate):

    ##
    ## Constructor
    ##
    
    def __init__(self):
        
        pass
        
    ##
    ## Returns a pair of squares to swap
    ##
    ## @param board a 2D array of shapes to compare
    ## @return an array of size 2, representing squares to swap
    ##
    
    def getMove(self, board):
        
        for 