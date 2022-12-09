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
    H = (0,0)
    T = (0,0)
    visited_points = {T}
    for move in moves:
        (x, y) = H
        if move == 'L':
            H = (x-1, y)
        elif move == 'U':
            H = (x, y+1)
        elif move == 'R':
            H = (x+1, y)
        elif move == 'D':
            H = (x, y-1)
        
        T = newTPos(H, T)
        visited_points.add(T)
    
    return visited_points
        
print(len(run(transform_to_moves(parse(puzzle_input)))))