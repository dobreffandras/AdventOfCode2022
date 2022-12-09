puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    
    def parse_starting_stack(drawing):
        lines = drawing.split('\n')
        last_line = lines[len(lines)-1]
        stacks = dict([(last_line[i], []) for i in range(1, len(last_line), 4)])
        
        for li in range(len(lines)-1):
            line = lines[li]
            for i in range(1, len(line), 4):
                if line[i] != ' ':
                    stacks[last_line[i]].append(line[i])
        
        return stacks
        
        
    def parse_rearrangement_proc(instructions):
        lines = instructions.split('\n')
        steps = []
        for line in lines:
            x = [int(s) for s in line.split() if s.isdigit()]
            steps.append((x[0], str(x[1]), str(x[2])))

        return steps

    parts = input.split('\n\n')
    starting_stack = parse_starting_stack(parts[0])
    rearrangement_proc = parse_rearrangement_proc(parts[1])
    
    return (starting_stack, rearrangement_proc)

def run_rearrangement(data):

    def move(s, n, frm, to):
        to_move = s[frm][0:n]
        to_move.reverse()
        to_move.extend(s[to])
        s[to] = to_move
        s[frm] = s[frm][n:]
        
    stacks = data[0]
    rearrangement_steps = data[1]
    
    for step in rearrangement_steps:
        move(stacks, step[0], step[1], step[2])

    return stacks

def read_top_elements(stacks):
    return str.join('', [s[0] for s in stacks.values()])

print(read_top_elements(run_rearrangement(parse(puzzle_input))))