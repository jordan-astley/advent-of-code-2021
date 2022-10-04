# commands = ['forward 5',
#             'down 5',
#             'forward 8',
#             'up 3',
#             'down 8',
#             'forward 2']


def read_vals(filename: str)->list:
    commands = []
    with open(filename, 'r') as sonar_vals:
        commands = [line.strip() for line in sonar_vals] # remove \n
    return commands

def solver(commands):
    f = 0
    x = 0
    forward = 'forward'
    up = 'up'
    down = 'down'

    for command in commands:
        if command.startswith(forward) == True:
            chars = len(command)
            letters = len(forward)
            input = int(command[letters:chars])
            f += input
        elif command.startswith(up) == True:
            chars = len(command)
            letters = len(up)
            input = int(command[letters:chars])
            x -= input
        elif command.startswith(down) == True:
            chars = len(command)
            letters = len(down)
            input = int(command[letters:chars])
            x += input
        else:
            print('invalid command')
    
    print(f'{f},{x}')
    resolve = f*x
    print(resolve)
    return resolve

def solverWaim(commands):
    y = x = aim = 0 # x = horizontal, y = depth
    forward = 'forward'
    up = 'up'
    down = 'down'

    for command in commands:
        if command.startswith(forward) == True: # forward
            chars = len(command)
            letters = len(forward)
            input = int(command[letters:chars])
            x += input
            y += aim*input
        elif command.startswith(up) == True: # up decreases aim
            chars = len(command)
            letters = len(up)
            input = int(command[letters:chars])
            aim -= input
        elif command.startswith(down) == True: # down increase aim
            chars = len(command)
            letters = len(down)
            input = int(command[letters:chars])
            aim += input
        else:
            print('invalid command')
    resolve = x*y
    print(f"final values of horizontal: {x}, depth: {y}\nresolve = {resolve}")

commands = read_vals('katas/puzzle_inputs/dive.txt')
# solver(commands)
solverWaim(commands)
