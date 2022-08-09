
class assign_adjacent_locs:
    def __init__(self, input:list, xy:tuple) -> None:
        self.input = input
        self.x, self.y = xy
        self.inputHeightIndex = len(input)-1
        self.inputWidthIndex = len(input[self.y])-1
        self.value = input[self.y][self.x]

        if self.y != 0:
            self.up = input[self.y-1][self.x]
        else:
            self.up = None


        if self.y >= self.inputHeightIndex:
            self.down = None
        else:
            self.down = input[self.y+1][self.x]
        

        if self.x != 0:
            self.left = input[self.y][self.x-1]
        else:
            self.left = None
       
        
        if self.x >= self.inputWidthIndex:
            self.right = None
        else:
            self.right = input[self.y][self.x+1]
        

    # up = input[y-1][x]
    # down = input[y+1][x]
    # left = input[y][x-1]
    # right = input[y][x+1]
    # value = input[y][x]
    # inputHeightIndex = len(input)-1 # highest index in input
    # inputWidthIndex = len(input[y])-1 # highest index in input[y] list
    