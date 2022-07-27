# filePath = "vents_test.txt"
filePath = "AOC5_hydrothermal_vents\\vents.txt"

def read_puzzle_input(filePath)->list:
    with open(filePath,"r") as puzzleInput:
        lines = [line.strip() for line in puzzleInput] # strip() to remove \n
                                                       # no following [] since want entire file contents
    return lines

listOfcoords = read_puzzle_input(filePath)
# listOfcoords

# def format_puzzle_input(listOfcoords)->list:
coords = [item.split(' -> ') for item in listOfcoords]
# coords

for index,element in enumerate(coords):
    coords[index] = [item.split(',') for item in coords[index]]
# coords

for coordinatePairIndex,element in enumerate(coords):
    for coordinateSubIndex,_ in enumerate(element):
        coords[coordinatePairIndex][coordinateSubIndex] = [int(item) for item in coords[coordinatePairIndex][coordinateSubIndex]]
# coords 

test1 = [[0,9],[5,9]]
test2 = [[2,2],[2,1]]
test3 = [[9,4],[3,4]]
test4 = [[10,0],[0,0]]
test5 = [[0,10],[0,0]]

def parallelx(coordinatePair)->bool:
    if coordinatePair[0][1] == coordinatePair[1][1]:
        return True # line has 2 equal y values, so is parallel with x axis
    elif coordinatePair[0][0] == coordinatePair[1][0]:
        return False # line has 2 equal x values, so it parallel with y axis
    else:
        return ValueError

def set_xvalues_from_pair_of_coordinates(coordinatePair):
    if (coordinatePair[0][0]) > (coordinatePair[1][0]): # case where x1 is greater than x2
        x_values = list(range(coordinatePair[1][0]+1, coordinatePair[0][0], 1))
        x_values.reverse()
    else:
        x_values = list(range(coordinatePair[0][0]+1, coordinatePair[1][0], 1))
    # list of points between on the axis, excluding the original two values
    y = coordinatePair[0][1] # y coordinates are equal so assign y to one of them

    return x_values, y

def set_yvalues_from_pair_of_coordinates(coordinatePair):
    if (coordinatePair[0][1]) > (coordinatePair[1][1]): # case where x1 is greater than x2
        y_values = list(range(coordinatePair[1][1]+1, coordinatePair[0][1], 1))
        y_values.reverse() 
    else:   
        y_values = list(range(coordinatePair[0][1]+1, coordinatePair[1][1], 1))
    # list of points between on the axis, excluding the original two values
    x = coordinatePair[0][0] # x coordinates are equal so assign x to one of them
    return y_values, x


def make_line_between_points(coordinatePair):
    n = 1
    if parallelx(coordinatePair) == True:
        x_values,y = set_xvalues_from_pair_of_coordinates(coordinatePair)
        for item in x_values:
            coordinatePair.insert(n,[item,y])
            n += 1
    elif parallelx(coordinatePair) == False:
        y_values,x = set_yvalues_from_pair_of_coordinates(coordinatePair)
        for item in y_values:
            coordinatePair.insert(n,[x,item])
            n += 1
    if parallelx(coordinatePair) == ValueError:
        pass

    return coordinatePair

# print(make_line_between_points(test1))
# print(make_line_between_points(test2))
# print(make_line_between_points(test3))
# print(make_line_between_points(test4))
# print(make_line_between_points(test5))

for index,coordinatePair in enumerate(coords):
    coords[index] = make_line_between_points(coordinatePair)
    
# coords

# [:] fix for removing items from list 
# without destroying the indexes
# Creates a copy of the list.
# Alternatively create new list with items to delete and then 'for item not in'

for item in coords[:]:
    if (item[0][0] != item[-1][0]) and (item[0][1] != item[-1][1]):
        # if neither x1 = x2 or y1 = y2 remove this item
        coords.remove(item)
# coords

dismantledLinesCoords = [item for elem in coords for item in elem]
dismantledLinesCoords = [str(item) for item in dismantledLinesCoords]
# print(dismantledLinesCoords) # flat list of strings

uniquePoints = set(dismantledLinesCoords)

totalledPoints_dict = {}
for item in uniquePoints:
    totalledPoints_dict[item] = dismantledLinesCoords.count(item)
# totalledPoints_dict

# this for loop took over 4 minutes to run...

counter = 0
for key in totalledPoints_dict:
    if totalledPoints_dict[key] >= 2:
        counter += 1
print(counter)