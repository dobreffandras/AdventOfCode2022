puzzle_input = open("./puzzle_input.txt", "r").read()

sand_source = (500,0)
    
def parse(input):
    def parse_coord(c):
        s = c.split(',')
        return (int(s[0]), int(s[1]))
        
    lines = input.split('\n')
    return [[parse_coord(c) for c in line.split(' -> ')] for line in lines]
    
def create_rocks(paths):
    def sign(n):
        return 0 if not n else (1 if 0 < n else -1)
    
    rocks = set()
    for path in paths:
        path_points = [(path[i], path[i+1]) for i in range(len(path)-1)]
        for (source, dest) in path_points:
            (x, y) = source
            (dest_x, dest_y) = dest
            while x != dest_x or y != dest_y:
                rocks.add((x,y))
                (x, y) = (x + sign(dest_x - x), y + sign(dest_y - y))
            rocks.add((dest_x, dest_y))
    return rocks
            
def draw_field(rocks, sands):
    objects = list(rocks) + [sand_source] + list(sands)
    x_values = [x for (x, _) in objects]
    y_values = [y for (_, y) in objects]
    field = []
    for i in range(min(y_values), max(y_values)+2):
        field.append([])
        for j in range(min(x_values), max(x_values)+1):
            pixel = '#' if (j,i) in rocks else '+' if (j,i) == sand_source else 'o' if (j,i) in sands else '.'
            field[i-min(y_values)].append(pixel)
    print('\n'.join([''.join(line) for line in field]))

def pour_sand(rocks):
    lowest_rock_y = max([y for (_, y) in rocks])
    def comes_to_rest(sand, rocks, sands):
        objects = rocks.union(sands)
        (sx, sy) = sand
        if (sx, sy + 1) in objects and (sx - 1, sy + 1) in objects  and (sx + 1, sy + 1) in objects \
            or sy == lowest_rock_y+1:
            return True
        else:
            return False
    def move_sand(sand, rocks, sands):
        objects = rocks.union(sands)
        (sx, sy) = sand
        if (sx, sy + 1) in objects:
            if (sx - 1, sy + 1) in objects:
                if (sx + 1, sy + 1) in objects:
                    # stay in position
                    return (sx, sy)
                else:
                    return (sx + 1, sy + 1)
            else:
                return (sx - 1, sy + 1)
        else:
            return (sx, sy + 1)
    sands = set()
    covered_sands = set()
    try:
        while True:
            if len(covered_sands) % 100 == 0:
                draw_field(rocks, sands)
            sand = sand_source
            while not comes_to_rest(sand, rocks, sands.union(covered_sands)):
                sand = move_sand(sand, rocks, sands)
                (_,y) = sand
            (sx, sy) = sand
            item_below = (sx, sy + 1)
            if item_below in sands:
                sands.remove(item_below)
                covered_sands.add(item_below)
            sands.add(sand)
            if sand == sand_source:
                raise StopIteration

    except:
        return (rocks, sands.union(covered_sands))
    

(rocks, sands) = pour_sand(create_rocks(parse(puzzle_input)))
draw_field(rocks, sands)
print(len(sands))