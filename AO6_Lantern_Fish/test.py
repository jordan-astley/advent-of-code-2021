# filePath = "AO6_Lantern_Fish\\lanterntest.txt"
filePath = "AO6_Lantern_Fish\\lanternfish.txt"

with open(filePath,"r") as puzzleInput:
    input = [line for line in puzzleInput][0].split(",")
lanternfish = [int(item) for item in input]

def run_sim(lanternfish,days):

    for _ in range(days):
        nextday = []
        for i in (lanternfish):
            if i==0: # if value is 0, reset to 6, add a new fish
                nextday.append(6)
                nextday.append(8)
            else: # otherwise minus 1 from the timer value for the fish
                nextday.append(i-1)
        lanternfish = nextday
    return lanternfish


lanternfish = run_sim(lanternfish,days=80)
print(len(lanternfish))

    # for day in range(days):
    #     counter = 0 # number of new fish to be added per simulation day

    #     for i,value in enumerate(lanternfish):
    #         if value == 0: # if value is 0 reset timer and create a new fish
    #             lanternfish[i] = 6
    #             counter += 1 
    #         else: # otherwise minus 1 from the timer value for the fish
    #             lanternfish[i] =  value - 1
            
    #     if (counter == 0) is False: # check if any new fish need to be added
    #         for _ in range(counter):
    #             lanternfish.append(8) # add an 8 to the list counter number of times

    #     # print(lanternfish, counter)
    # return lanternfish