class Board:
    
    shapes = ['r', 'g', 'b', 'k', 'y', 'p', 'x']
    array = None
    mark = None
    numCols = -1
    numRows = -1
    
    def __init__(self, array):
        
        assert ( array != None and len(array) > 0 and len(array[0]) > 0 ), "Invalid board!"
        for x in xrange(len(array)):
            for y in xrange(len(array[0])):
                assert ( array[x][y][0] in self.shapes ), "Invalid board!"
                if ( array[x][y] == 'x' ):
                    array[x][y] += ' ' + str(x) + ' ' + str(y)
        self.array = array 
        self.numCols = len(self.array)
        self.numRows = len(self.array[0])
        self.mark = [[0 for row in xrange(self.numRows)] for col in xrange(self.numCols)]
    
    ##
    ## Checks if dimensions are valid
    ##
    
    def isValid(self, X, Y):
        
        return not ( X < 0 or X >= len(self.array) or Y < 0 or Y >= len(self.array[0]) )
    
    ##
    ## Gets the value of the board at [X,Y]
    ##
    
    def get(self, X, Y):
        
        if ( not self.isValid(X, Y) ):
            return None
        else:
            return self.array[X][Y]
    
    ##
    ## Returns if there is a triple anywhere on the board
    ##
        
    def hasTripleAnywhere(self):
        
        for Y in xrange(self.numRows):
            for X in xrange(self.numCols):
                if ( self.get(X, Y) == self.get(X + 1, Y) and self.get(X + 1, Y) == self.get(X + 2, Y) ):
                    return True
                if ( self.get(X, Y) == self.get(X, Y + 1) and self.get(X, Y + 1) == self.get(X, Y + 2) ):
                    return True
        return False
        
    ##
    ## Returns if there is a triple at [X,Y]
    ##
        
    def hasTripleAt(self, X, Y):
        
        assert self.isValid(X, Y), "Invalid board location."
        
        if ( self.get(X - 2, Y) == self.get(X - 1, Y) and self.get(X - 1, Y) == self.get(X, Y) ):
            return True
        elif ( self.get(X - 1, Y) == self.get(X, Y) and self.get(X, Y) == self.get(X + 1, Y) ):
            return True
        elif ( self.get(X, Y) == self.get(X + 1, Y) and self.get(X + 1, Y) == self.get(X + 2, Y) ):
            return True
        elif ( self.get(X, Y - 2) == self.get(X, Y - 1) and self.get(X, Y - 1) == self.get(X, Y) ):
            return True
        elif ( self.get(X, Y - 1) == self.get(X, Y) and self.get(X, Y) == self.get(X, Y + 1) ):
            return True
        elif ( self.get(X, Y) == self.get(X, Y + 1) and self.get(X, Y + 1) == self.get(X, Y + 2) ):
            return True
        else:
            return False

    ##
    ## Returns a new board with the given squares swapped
    ##
    
    def swap(self, X1, Y1, X2, Y2):

        assert ( self.isValid(X1, Y1) and self.isValid(X2, Y2) ), "Invalid board location."
        self.mark[X1][Y1] += 1
        self.mark[X2][Y2] += 1
        newArray = [[value for value in column] for column in self.array]
        (newArray[X1][Y1], newArray[X2][Y2]) = (newArray[X2][Y2], newArray[X1][Y1])
        return Board(newArray)
    
    
