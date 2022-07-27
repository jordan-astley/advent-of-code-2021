# read the puzzle input
def read_bingo_boards(filename: str)->list:
    with open(filename, 'r') as values:
        lines = [line.strip() for line in values][1:] # remove \n
    return lines

# get the bingo callouts as separate variable
def read_num_callouts(filename: str)->list:
    with open(filename, "r") as file:
        bingoNums = [bingoNums.strip() for bingoNums in file][0] # first line has rand integers list
    return bingoNums.split(',')


class puzzle_input:
    def __init__(self, givenFilePath) -> None:
        self.filePath = givenFilePath

    def read_puzzle_input(self)->list:
        with open(self.filePath,"r") as puzzleInput:
            self.lines = [line.strip() for line in puzzleInput] # strip() to remove \n
                                                           # no following [] since want entire file contents
        return self.lines
    
    def format_puzzle_input(self)->list:
        coords = self.read_puzzle_input()
        coords = [item.split(' -> ') for item in coords]

        # for index1,_ in enumerate(coords):
        #     for index2,__ in enumerate(coords[index1]):
        #         coords[index1][index2] = coords[index1][index2].split(',')
        for i,pairCoords in enumerate(coords):
            for coord1,coord2 in pairCoords:
                coords
            
            

        return coords



    # def return_coords(self, file_path):