puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    lines = input.split('\n')
    commands = [('noop', None) if l == 'noop' else ('addx', int(l.split(' ')[1])) for l in lines]
    return commands

def to_cycles(commands):
    cycles = []
    for (c,n) in commands:
        if c == 'noop':
            cycles.append(0)
        elif c == 'addx':
            cycles.append(0)
            cycles.append(n)
    return cycles

def run(cycles):
    
    def pixel(i, x):
        if x-1 <= i%40 <= x+1:
            return '#'
        else:
            return '.'
            
    x = 1
    screen = [None]*len(cycles)
    for i in range(0, len(cycles)):
        screen[i] = pixel(i, x)
        x += cycles[i]

    return screen

def draw(screen):
    for i in range(0,240,40):
        print(''.join(screen[i:i+39]))
        
draw(run(to_cycles(parse(puzzle_input))))