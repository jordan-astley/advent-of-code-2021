test = [199,200,208,210,200,207,240,269,260,263]

def read_vals(filename: str)->list:
    values_list = []
    with open(filename, 'r') as sonar_vals:
        values_list = [int(line.strip()) for line in sonar_vals] # remove \n
    return values_list

def count_increases(values_list):
    increase = 0
    decrease = 0
    for i in range(len(values_list)-1):
        if values_list[i+1] > values_list[i]:
            increase += 1
        if values_list[i+1] < values_list[i]:
            decrease += 1
    print('increases = %d, decrease = %d' % (increase, decrease))

def slidingWindowInc(values_list):
    increase = decrease = no_change = 0
   
    for i in range(len(values_list)-3):
        window1 = sum(values_list[i:i+3])
        window2 = sum(values_list[i+1:i+4])

        if i == 0:
            print(f"{window1} (N/A - no previous sum)")
        if window1 < window2:
            # print(f"{window2} (increased)")
            # print(f"{sum(values_list[i:i+3])} < {sum(values_list[i+1:i+4])}")
            increase += 1
        if window1 > window2:
            # print(f"{window2} (decreased)")
            # print(f"{sum(values_list[i:i+3])} > {sum(values_list[i+1:i+4])}")
            decrease += 1
        if window1 == window2:
            # print(f"{window2} (no change)")
            # print(f"{sum(values_list[i:i+3])} = {sum(values_list[i+1:i+4])}")
            no_change += 1

    print("Sliding window inc = %d"%increase)
    return increase


values_list = read_vals('puzzle_inputs/sonar.txt')
# print(values_list)
count_increases(values_list)
slidingWindowInc(values_list)
# count_increases(test)