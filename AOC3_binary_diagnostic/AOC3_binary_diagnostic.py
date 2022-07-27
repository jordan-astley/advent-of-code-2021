
def read_vals(filename: str)->list:
    with open(filename, 'r') as values:
        lines = [line.strip() for line in values] # remove \n
    return lines

def findmostCommon(list):
    mcb = min(set(list), key=list.count)
    return mcb

def findleastCommon(list):
    lcb = max(set(list), key=list.count)
    return lcb

def findGamma(codes):
    i_listNthdigits = []
    gamma = ''
    for digit in range(len(codes[0])): # auto get amount of bits per line
        for i in range(len(codes)):
            i_listNthdigits.append(codes[i][digit])
        gamma += findmostCommon(i_listNthdigits)
        i_listNthdigits.clear()
    return int(gamma, 2)

def findEpsilon(codes):
    i_listNthdigits = []
    eps = ''
    for digit in range(len(codes[0])): # auto get amount of bits per line
        for i in range(len(codes)):
            i_listNthdigits.append(codes[i][digit])
        eps += findleastCommon(i_listNthdigits)
        i_listNthdigits.clear()
    return int(eps, 2)



def findmostCommon2(list):
    mcb = 0
    ones = list.count('1')
    zeroes = list.count('0')
    if (ones > zeroes) or (ones == zeroes):
        mcb = 1
    else:
        mcb = 0
    return mcb

def findleastCommon2(list):
    lcb = 0
    ones = list.count('1')
    zeroes = list.count('0')
    if (ones > zeroes) or (ones == zeroes):
        lcb = 0
    else:
        lcb = 1
    return lcb

def appendDigitN(codes,digit):
    listNthdigits = []
    for code in range(len(codes)): # iterate over list of codes
        if codes[code] == '':
                continue
        else:
            listNthdigits.append(codes[code][digit]) # repeatedly create list of nth digit bits
    return listNthdigits

def filterCodes(codes, Bit, digit):
    for code in range(len(codes)): # filter codes list for 1or0 in specific digit
        if codes[code] == '':
            continue
        if codes[code][digit] != str(Bit):
            codes[code] = ''

def checkVals(codes): # checks if reached final value
    numOfClears = codes.count('')
    linescount = len(codes)
    if numOfClears == (linescount-1): # if final value, 1 less clear elements in list than len(list)
        return True
    else:
        return False

def findOxygenatorRating(list):
    codes = list.copy()
    numberLength = len(codes[0])
    for digit in range(numberLength): # iterate for each digit, automatically find max no.
        listNthdigits = appendDigitN(codes,digit)
        mostCommonBit = findmostCommon2(listNthdigits) # returns 1 if equal
        filterCodes(codes, mostCommonBit, digit) # clears lines in codes that don't have mcb in correct digit
        listNthdigits.clear()
        if checkVals(codes) == True:
            break
    O2rating = [x for x in codes if (x != '')][0]
    # O2rating = O2rating[0]
    
    return O2rating

def findCarbonDioxideRating(list):
    codes = list.copy()
    numberLength = len(codes[0])
    for digit in range(numberLength): # iterate for each digit, automatically find max no.
        listNthdigits = appendDigitN(codes,digit)
        leastCommonBit = findleastCommon2(listNthdigits) # returns 1 if equal
        filterCodes(codes, leastCommonBit, digit) # clears lines in codes that don't have mcb in correct digit
        listNthdigits.clear()
        # print(f"lcb{leastCommonBit} in digit{digit}")
        if checkVals(codes) == True:
            break
    CO2rating = [x for x in codes if (x != '')][0]
    return CO2rating
    
def convert2dec(x):
    return int(x,2)

list = read_vals('puzzle_inputs/binary.txt')
# list = ['00100',
#         '11110',
#         '10110',
#         '10111',
#         '10101',
#         '01111',
#         '00111',
#         '11100',
#         '10000',
#         '11001',
#         '00010',
#         '01010']

O2rating = findOxygenatorRating(list)
O2rating = convert2dec(O2rating)
print(f"o2 rating = {O2rating}")
CO2rating = findCarbonDioxideRating(list)
CO2rating = convert2dec(CO2rating) 
print(f"co2 rating = {CO2rating}")

print(f"life support rating = {O2rating*CO2rating}")
# gamma = findGamma(codes)
# eps = findEpsilon(codes)
# print("gamma = %d, epsilon = %d, power consumption = %d" %(gamma,eps,(gamma*eps)))
