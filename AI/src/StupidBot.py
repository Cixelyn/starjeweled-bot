from BotTemplate import BotTemplate

class StupidBot(BotTemplate):

    ##
    ## Constructor
    ##
    
    def __init__(self):
        
        self.state = -1
        self.checkedLeft = False
        self.checkedRight = False
        
    ##
    ## Returns the first pair of squares that can be swapped
    ##
    ## @param board a 2D array of shapes to compare
    ## @return an array of size 2, representing squares to swap
    ##
    
    def getMove(self, board):
        
        self.checkedLeft = False
        self.checkedRight = False
        self.state = ( self.state + 1 ) % 4
        
        while ( not self.checkedLeft or not self.checkedRight ):
        
            if ( self.state == 0 ):
                for y in xrange(0, board.numRows - 1, 1):
                    for x in xrange(0, board.numCols / 2, 1):
                        swapH = board.swap(x, y, x + 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x + 1, y) ):
                            self.checkedLeft = False
                            self.checkedRight = False
                            return [[x, y], [x + 1, y]]
                        swapV = board.swap(x, y, x, y + 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                            self.checkedLeft = False
                            self.checkedRight = False
                            return [[x, y], [x, y + 1]]
                ## nothing found on the left side of the board
                self.state = 2
                self.checkedLeft = True
                
            if ( self.state == 1 ):
                for y in xrange(board.numRows / 2, board.numRows - 1, 1):
                    for x in xrange(0, board.numCols / 2, 1):
                        swapH = board.swap(x, y, x + 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x + 1, y) ):
                            self.checkedLeft = False
                            self.checkedRight = False
                            return [[x, y], [x + 1, y]]
                        swapV = board.swap(x, y, x, y - 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y - 1) ):
                            self.checkedLeft = False
                            self.checkedRight = False
                            return [[x, y], [x, y - 1]]
                ## nothing found on the left side of the board
                self.state = 2
                self.checkedLeft = True
                
            if ( self.state == 2 ):
                for y in xrange(0, board.numRows - 1, 1):
                    for x in xrange(board.numCols - 1, (board.numCols / 2) - 1, -1):
                        swapH = board.swap(x, y, x - 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x - 1, y) ):
                            return [[x, y], [x - 1, y]]
                        swapV = board.swap(x, y, x, y + 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                            return [[x, y], [x, y + 1]]
                ## nothing found on the right side of the board
                self.state = 0
                self.checkedRight = True
                
            if ( self.state == 3 ):
                for y in xrange(board.numRows / 2, board.numRows - 1, 1):
                    for x in xrange(board.numCols - 1, (board.numCols / 2) - 1, -1):
                        swapH = board.swap(x, y, x - 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x - 1, y) ):
                            return [[x, y], [x - 1, y]]
                        swapV = board.swap(x, y, x, y - 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y - 1) ):
                            return [[x, y], [x, y - 1]]
                ## nothing found on the right side of the board
                self.state = 0
                self.checkedRight = True
        
        ## if we reach here, there are no valid moves on the board
        
        return None


if __name__ == "__main__":
    b = [['g', 'r', 'r', 'k', 'p', 'g', 'b', 'g'], ['p', 'b', 'y', 'b', 'y', 'b', 'p', 'p'], ['b', 'r', 'r', 'g', 'b', 'k', 'k', 'g'], ['b', 'k', 'p', 'y', 'r', 'p', 'b', 'y'], ['y', 'r', 'g', 'r', 'g', 'r', 'y', 'p'], ['x', 'b', 'y', 'g', 'b', 'y', 'b', 'g'], ['p', 'r', 'b', 'p', 'g', 'p', 'y', 'p'], ['k', 'y', 'r', 'y', 'k', 'g', 'b', 'g']]

    
    bot = StupidBot()
    from Board import Board
    print bot.getMove(Board(b))
    
    
