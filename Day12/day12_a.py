from queue import PriorityQueue

puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    lines = [list(line) for line in input.split('\n')]
    start_pos = None
    end_pos = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                start_pos = (i,j)
                lines[i][j] = 'a'
            elif lines[i][j] == 'E':
                end_pos = (i,j)
                lines[i][j] = 'z'
    return (start_pos, end_pos, lines)
            
    
def to_neighbourhood(height_map):
    def get_neighbours(i,j):
        (left, top, right, bottom) = None, None, None, None
        if 0 < i:
            top = (i - 1, j)
        if 0 < j:
            left = (i, j - 1)
        if i < len(height_map)-1:
            bottom = (i + 1, j)
        if j < len(height_map[0])-1:
            right = (i, j + 1)
        return (left, top, right, bottom)

    def if_allowed(n, c):
        if not n:
            return None
        (ni, nj) = n
        return n if ord(height_map[ni][nj]) in range(ord(c)+2) else None

    neighbourhood = dict()
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            c = height_map[i][j]
            (left, top, right, bottom) = get_neighbours(i, j)
            l = if_allowed(left, c)
            t = if_allowed(top, c)
            r = if_allowed(right, c)
            b = if_allowed(bottom, c)
            neighbourhood[(i,j)] = (l, t, r, b)

    return neighbourhood
    
def dijkstra(G, start, goal):
    """ Uniform-cost search / dijkstra 
        Source: https://gist.github.com/qpwo/cda55deee291de31b50d408c1a7c8515
    """
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()
  
    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get() # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else: # if todo ran out
            break # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor in G[vertex]:
            if neighbor in visited: continue # skip these to save time
            old_cost = cost.get(neighbor, float('inf')) # default to infinity
            new_cost = cost[vertex] + 1
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return cost
    
def draw_neighbourhood(nx, W, H):
    arrows = {
        (False, False, False, False): ' ',
        (True, False, False, False): ' ',
        (False, True, False, False): ' ',
        (False, False, True, False): ' ',
        (False, False, False, True): ' ',
        (True, True, False, False): '\u2518',
        (True, False, True, False): '\u2500',
        (True, False, False, True): '\u2510',
        (False, True, True, False): '\u2514',
        (False, True, False, True): '\u2502',
        (False, False, True, True): '\u250C',
        (False, True, True, True): '\u251C',
        (True, False, True, True): '\u252C',
        (True, True, False, True): '\u2524',
        (True, True, True, False): '\u2534',
        (True, True, True, True): '\u253C'
        }

    d = [['#' for _ in range(W)] for __ in range(H)]
    for i in range(H):
        for j in range(W):
            (l, t, r, b) = nx[(i,j)]
            d[i][j] = arrows[(bool(l), bool(t), bool(r), bool(b))]
    print('\n'.join([''.join(x) for x in d]))

def normalize(neighbourhood):
    return dict([(n,[x for x in neighbourhood[n] if x is not None]) for n in neighbourhood])

(s, e, h_map) = parse(puzzle_input)
w = len(h_map[0])
h = len(h_map)
neighbourhood = to_neighbourhood(h_map)
draw_neighbourhood(neighbourhood, w, h)
costs = dijkstra(normalize(neighbourhood), s, e)
print(costs[e])