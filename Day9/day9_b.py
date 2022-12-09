import math

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    command_signs = [line.split(' ') for line in input.split('\n')]
    return [(direction, int(steps)) for (direction, steps) in command_signs]

def transform_to_moves(move_commands):
    return ''.join([direction*steps for (direction, steps) in move_commands])

def newTPos(newH, prevT):
    def sign(n):
        return 0 if not n else (1 if 0 < n else -1)
    
    (xH, yH) = newH
    (xT, yT) = prevT
    dX = xH-xT
    dY = yH-yT
    dist = dist = math.sqrt(dX**2 + dY**2)
    if 2 <= dist:
        xT = xT+sign(dX)
        yT = yT+sign(dY)

    return (xT, yT)
    
def run(moves):
    rope = [(0,0)]*10
    visited_points = {rope[-1]}
    newHPos = {
        'L': lambda x,y: (x-1, y),
        'U': lambda x,y: (x, y+1),
        'R': lambda x,y: (x+1, y),
        'D': lambda x,y: (x, y-1)
    }
    for move in moves:
        (xH, yH) = rope[0]
        rope[0] = newHPos[move](xH, yH)
        for t_idx in range(1, len(rope)):
            curr = rope[t_idx]
            prev = rope[t_idx-1]
            rope[t_idx] = newTPos(prev, curr)
        visited_points.add(rope[-1])
    
    return visited_points
        
print(len(run(transform_to_moves(parse(puzzle_input)))))