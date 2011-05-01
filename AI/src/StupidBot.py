from BotTemplate import BotTemplate

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
        
        quadsChecked = 0
        
        while ( quadsChecked < 4 ):
        
            quadsChecked += 1
            self.state = ( self.state + 1 ) % 4
        
            ## top-left
            if ( self.state == 0 ):
                for y in xrange(0, board.numRows / 2, 1):
                    for x in xrange(0, board.numCols / 2, 1):
                        ## swap right
                        swapH = board.swap(x, y, x + 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x + 1, y) ):
                            return [[x, y], [x + 1, y]]
                        ## swap down
                        swapV = board.swap(x, y, x, y + 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                            return [[x, y], [x, y + 1]]
                
            ## bottom-left
            if ( self.state == 1 ):
                for y in xrange(board.numRows - 1, (board.numRows / 2) - 1, -1):
                    for x in xrange(0, board.numCols / 2, 1):
                        ## swap right
                        swapH = board.swap(x, y, x + 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x + 1, y) ):
                            return [[x, y], [x + 1, y]]
                        ## swap up
                        swapV = board.swap(x, y, x, y - 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y - 1) ):
                            return [[x, y], [x, y - 1]]
                
            ## top-right
            if ( self.state == 2 ):
                for y in xrange(0, board.numRows / 2, 1):
                    for x in xrange(board.numCols - 1, (board.numCols / 2) - 1, -1):
                        ## swap left
                        swapH = board.swap(x, y, x - 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x - 1, y) ):
                            return [[x, y], [x - 1, y]]
                        ## swap down
                        swapV = board.swap(x, y, x, y + 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y + 1) ):
                            return [[x, y], [x, y + 1]]
                
            ## bottom-right
            if ( self.state == 3 ):
                for y in xrange(board.numRows - 1, (board.numRows / 2) - 1, -1):
                    for x in xrange(board.numCols - 1, (board.numCols / 2) - 1, -1):
                        ## swap left
                        swapH = board.swap(x, y, x - 1, y)
                        if ( swapH.hasTripleAt(x, y) or swapH.hasTripleAt(x - 1, y) ):
                            return [[x, y], [x - 1, y]]
                        ## swap up
                        swapV = board.swap(x, y, x, y - 1)
                        if ( swapV.hasTripleAt(x, y) or swapV.hasTripleAt(x, y - 1) ):
                            return [[x, y], [x, y - 1]]
        
        ## if we reach here, there are no valid moves on the board
        
        return None


if __name__ == "__main__":
    b = [['x', 'x', 'b', 'x', 'k', 'y', 'p', 'g'],
['r', 'p', 'g', 'y', 'g', 'p', 'g', 'p'],
['p', 'k', 'p', 'r', 'p', 'r', 'k', 'y'],
['k', 'g', 'b', 'k', 'g', 'b', 'p', 'g'],
['b', 'p', 'y', 'b', 'y', 'g', 'y', 'p'],
['r', 'p', 'g', 'p', 'g', 'p', 'r', 'y'],
['k', 'k', 'g', 'r', 'y', 'k', 'p', 'b'],
['p', 'y', 'p', 'r', 'r', 'p', 'g', 'g']]


    
    bot = StupidBot()
    from Board import Board
    print bot.getMove(Board(b))
    
    
