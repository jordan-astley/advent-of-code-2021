# A more elegant solution to puzzle 9 part 1 # 
# After researching solutions online, I realised my own was far from
# the most efficient.

# USAGE #
#           cd to location of this file
#           run $ python bettersolution.py <name of inputfile>
#           returns answer to the terminal

from re import L
import sys

def main(filename):

    # filename = 'input9.txt'
    with open(filename, "r") as INFILE:
        lines = [list(line) for line in INFILE.read().strip().split()]
        input = [[int(number) for number in line] for line in lines]

    answer, lowPointsIndices = find_low_points(input)
    print("answer = %d" % answer)
    print(lowPointsIndices)


def find_low_points(input):
    rowLen = len(input[0])
    colLen = len(input)
    # print('rowlen = %d, colLen = %d' % (rowLen,colLen))
    directionsY = (1,0,-1,0)
    directionsX = (0,1,0,-1)
    lowPoints = []
    lowPointsIndices = []
    currVals = []
    # iterate thru all rows and collumns
    for y in range(len(input)):
        for x in range(len(input[y])):

            # set each direction index
            for d in range(len(directionsY)):
                vertVal = y + directionsY[d]
                horizVal = x + directionsX[d]
            
                # print(f"y={y},x={x},vertVal={vertVal},horizVal={horizVal}")

                # Check surrounding points are in grid 
                if 0 <= horizVal <= rowLen-1 and 0 <= vertVal <= colLen-1:
                    currVals.append(input[vertVal][horizVal])

            if all(i > input[y][x] for i in currVals):
                lowPoints.append(input[y][x])
                lowPointsIndices.append((y,x))
                # print(lowPoints)

            # print()
            currVals.clear()

    # calculate answer
    return sum(list(map(lambda x: x+1, lowPoints))), lowPointsIndices

#  def find_list_of_basin_sizes(input, lowPointsIndices):
#     currBasin = [] # stores indices of points inside current basin
#     currVal = None

#     # each low point starts a new basin
#     # for lowPoint in lowPointsIndices:
#     y, x = lowPointsIndices[2]

#         # check left of point on curr row
#         if x != 0:
#             dis2leftside = 


#             while currVal != 9:
#                 for 





if __name__ == "__main__":
    main(sys.argv[1])
