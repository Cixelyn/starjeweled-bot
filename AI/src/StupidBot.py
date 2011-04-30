import BotTemplate

class StupidBot(BotTemplate):

    ##
    ## Constructor
    ##
    
    def __init__(self):
        
        self.state = -1
        
    ##
    ## Returns the first pair of squares that can be swapped
    ##
    ## @param board a 2D array of shapes to compare
    ## @return an array of size 2, representing squares to swap
    ##
    
    def getMove(self, board):
        
        state = ( state + 1 ) % 4
        
        if ( state == 0 ):
            for y in xrange(0, self.numRows, 1):
                for x in xrange(0, self.numCols / 2, 1):
                    swapH = board.swap(x, y, x + 1, y)
                    if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x + 1, y) ):
                        return [[x, y], [x + 1, y]]
                    swapV = board.swap(x, y, x, y + 1)
                    if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                        return [[x, y], [x, y + 1]]
            ## nothing found on the left side of the board
            state = 2
        if ( state == 1 ):
            for y in xrange(self.numRows / 2, self.numRows, 1):
                for x in xrange(0, self.numCols / 2, 1):
                    swapH = board.swap(x, y, x + 1, y)
                    if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x + 1, y) ):
                        return [[x, y], [x + 1, y]]
                    swapV = board.swap(x, y, x, y + 1)
                    if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                        return [[x, y], [x, y + 1]]
            ## nothing found on the left side of the board
            state = 2
            
        if ( state == 2 ):
            for y in xrange(0, self.numRows, 1):
                for x in xrange(self.numCols / 2, 0, -1):
                    swapH = board.swap(x, y, x - 1, y)
                    if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x - 1, y) ):
                        return [[x, y], [x - 1, y]]
                    swapV = board.swap(x, y, x, y + 1)
                    if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                        return [[x, y], [x, y + 1]]
            ## nothing found on the right side of the board
            state = 0
        if ( state == 3 ):
            for y in xrange(self.numRows / 2, self.numRows, 1):
                for x in xrange(self.numCols / 2, 0, -1):
                    swapH = board.swap(x, y, x - 1, y)
                    if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x - 1, y) ):
                        return [[x, y], [x - 1, y]]
                    swapV = board.swap(x, y, x, y + 1)
                    if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                        return [[x, y], [x, y + 1]]
            ## nothing found on the right side of the board
            state = 0