from operator import index
from obj_working_board_line import working_board_line
from time import sleep


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

# Convert the puzzle input into desired format
def board_lists_converter(bingoBoards: list)->list:
    listOfLists = [listOfLists.split() for listOfLists in bingoBoards] # .split() separate the numbers to stings
                                                                       # each element becomes a list, numbers are individual strings
    BOARDSIZE = 6    
    processedBingoBoards = []
    for i in range(0, len(listOfLists), BOARDSIZE):
        processedBingoBoards.append(listOfLists[i:i+BOARDSIZE])
    return processedBingoBoards

# removed empty lines from puzzle input
def remove_emptylists(processedBingoBoards: list)->list:
    for i in range(len(processedBingoBoards)): # always the first element
            del processedBingoBoards[i][0]
    return processedBingoBoards

# add 'x' to each number on the bingo boards that == called number for the round
def check_off_called_value_in_bingo_boards(calledOutNum: str, bingoBoards: list)-> list:
    numberOfBoards = len(bingoBoards)
    NUMS_PER_LINE = 5
    for board in range(numberOfBoards): # check each board
        for row in range(NUMS_PER_LINE):
            workingRow = working_board_line(bingoBoards[board][row])
            bingoBoards[board][row] = workingRow.check_off_called_value_in_line(calledOutNum)
    return bingoBoards

def check_row(board: list)->bool: # checks individual row for bingo!
    for row in range(len(board)):
        if all(element.endswith("x") for element in board[row]) == True:
              return True
    return False

def check_col(board: list)->bool: # checks a collumn for bingo!    
    dimension = len(board)
    for col_index in range(dimension):
        # construct collumns from lists
        working_col = [element[col_index] for element in board]
        if all(element.endswith("x") for element in working_col) == True:
            return True
    return False

# looks at a bingo board and checks the rows/columns for a win
def check_for_winner(bingoBoards: list):
    numberOfBoards = len(bingoBoards)
    winningBoards = []
    bingoFlag = False
    for board in range(numberOfBoards): # check each board in turn
        if (check_row(bingoBoards[board]) or check_col(bingoBoards[board])) == True:
            winningBoards.append(board) # save the list index to store the boards that win, in case there are two.
            bingoFlag = True
    return winningBoards, bingoFlag

def play_bingo_rounds(bingoNums: list, bingoBoards: list)-> None:
    round = 0
    bingoFlag = check_for_winner(bingoBoards)[1]
    while bingoFlag == False:
        print(f"Round {round}")
        calledOutNum = str(bingoNums[round])
        print(f"{calledOutNum}!!!")
        bingoBoards = check_off_called_value_in_bingo_boards(calledOutNum, bingoBoards)
        winningBoards,bingoFlag = check_for_winner(bingoBoards)
        round += 1
        
    print(f"We have a winner, boards: {winningBoards}")
    # if len(winningBoards) > 1:
    #     for item in winningBoards:
    #         print_winning_board(bingoBoards[item])
    # else:
    print_board(bingoBoards[winningBoards[0]])
    print_final_score(bingoBoards[winningBoards[0]],calledOutNum)

def print_board(board: list):
    for row in board:
        print(row)
        
def print_final_score(board,calledOutNum): # discovered there is not two winners at once
    sum_a = 0
    dimension_index = range(5)
    for row in board:
        for num in dimension_index:
            if row[num].endswith('x') == False:
                sum_a += int(row[num])

    final_score = (sum_a)*(int(calledOutNum))
    print(f"Final Score is {sum_a} x {calledOutNum} = {final_score}")

def delete_completed_boards(bingoBoards, boardsToDel): # called every round
    for i in bingoBoards[:]:
        if i in boardsToDel:
            bingoBoards.remove(i)
            boardsToDel.remove(i)
    return bingoBoards

def return_incomplete_boards(bingoBoards: list):
    boardsToDel = []

    for board in bingoBoards: # print all uncompleted boards each round
        print_board(board)
        print() # print empty line
    
    for board in bingoBoards[:]: # check each board in turn and delete completed boards
        if len(bingoBoards) == 1:
            break # have reached the final board, numberOfBoards = 2, which is now no longer true so break
        if (check_row(board) or check_col(board)) == True:
            boardsToDel.append(board)

        bingoBoards = delete_completed_boards(bingoBoards,boardsToDel)
    
    return bingoBoards # when returned len(bingoBoards) is == 1, the main loop will break 

def play_bingo_rounds_2_final(bingoNums: list, bingoBoards: list)-> None:
    round = 0

    while len(bingoBoards) != 1: # wait until final board is found to exit loop
                                 # when len(bingoBoards) == 1, all boards have been completed
                                 # indicating this is the final board to complete
        print(f"Round {round}")
        calledOutNum = str(bingoNums[round])
        print(f"{calledOutNum}!!!")

        bingoBoards = check_off_called_value_in_bingo_boards(calledOutNum, bingoBoards)
        bingoBoards = return_incomplete_boards(bingoBoards)

        round += 1

    while (check_col(bingoBoards[0]) or check_row(bingoBoards[0])) is not True:
        print(f"Round {round}")
        calledOutNum = str(bingoNums[round])
        print(f"{calledOutNum}!!!")
        bingoBoards = check_off_called_value_in_bingo_boards(calledOutNum, bingoBoards)
        round += 1
        print_board(bingoBoards[0])

    calledOutNum = str(bingoNums[round-1]) # -1 to get back to last num after round advancement
    bingoBoards = check_off_called_value_in_bingo_boards(calledOutNum,bingoBoards)
    print("######################################")
    print_board(bingoBoards[0]) # 0 since only one left so first element
    print_final_score(bingoBoards[0],calledOutNum)


bingoNums = read_num_callouts("katas/puzzle_inputs/bingo.txt") # returns list of numbers
# bingoNums = read_num_callouts("katas/puzzle_inputs/bingotest.txt") # returns list of numbers
bingoBoards = read_bingo_boards("katas/puzzle_inputs/bingo.txt") # list object containing bingoboards
# bingoBoards = read_bingo_boards("katas/puzzle_inputs/bingotest.txt") # list object containing bingoboards
bingoBoards = remove_emptylists(board_lists_converter(bingoBoards)) # each bingo board is a list, contain each line as a list
                                                                    # the boards are stored in a list of all bingo boards
# play_bingo_rounds(bingoNums,bingoBoards)
play_bingo_rounds_2_final(bingoNums,bingoBoards)






# test1 = [['31', '5', '70', '8', '88'],
#          ['38', '63', '14', '91', '56'], 
#          ['22', '67', '17', '47', '74'], 
#          ['93', '52', '69', '29', '53'], 
#          ['33', '66', '64', '19', '73']]

# test2 = [['31', '5', '70', '8', '88'], 
#          ['38', '63', '14', '91', '56'], 
#          ['22', '67', '17', '47', '74'], 
#          ['93x', '52x', '69x', '29x', '53x'], 
#          ['33', '66', '64', '19', '73']]

# test3 = [['31', '5', '70x', '8', '88'], 
#          ['38', '63', '14x', '91', '56'], 
#          ['22', '67', '17x', '47', '74'], 
#          ['93', '52', '69x', '29', '53'], 
#          ['33', '66', '64x', '19', '73']]

