# working board line object
# line on the bingo board, column or row.
# the col or row is given as a list input, created in the main script

# this creates an object that has the associated methods for:
#           - checking if all the numbers in the row have been checked off (win)
#           - searching the row for the called out number to check it off

class working_board_line:
    def __init__(self, workingLine:list):
        self.line = workingLine

    def check_off_called_value_in_line(self, calledOutNum):
        for item in range(len(self.line)):
            if self.line[item] == calledOutNum:
                self.line[item] = f'{self.line[item]}x'
        return self.line
