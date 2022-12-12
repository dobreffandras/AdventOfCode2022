puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    lines = input.split('\n')
    commands = [('noop', None) if l == 'noop' else ('addx', int(l.split(' ')[1])) for l in lines]
    return commands
   
def run(commands):
    signal_strength_by_cycle_nums = dict()
    
    def save_signal_strength_if_needed(c, x):
        if (c - 20) % 40 == 0:
            signal_strength_by_cycle_nums[c] = c*x
    
    x = 1
    cycle_num = 1
    for (c,n) in commands:
        if c == 'noop':
            save_signal_strength_if_needed(cycle_num, x)
            cycle_num += 1
        elif c == 'addx':
            save_signal_strength_if_needed(cycle_num, x)
            cycle_num += 1
            save_signal_strength_if_needed(cycle_num, x)
            cycle_num += 1
            x += n

    return signal_strength_by_cycle_nums
   
def sum_signal_strengths(signal_by_cycle):
    return sum(signal_by_cycle.values())
   
print (sum_signal_strengths(run(parse(puzzle_input))));