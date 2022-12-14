puzzle_input = open("./puzzle_input.txt", "r").read()

class Node:
    def __init__(self, children):
        self.children = children
        
    def __repr__(self):
        return f'{type(self).__name__}({self.children})'

def parse_node(input, indent=''):
    children = []
    current_digits = []
    while input:
        i = input.pop(0)
        if i.isdigit():
            current_digits.append(i)
        if i == ',' and current_digits:
            number = int(''.join(current_digits))
            children.append(number)
            current_digits = []
        if i == '[':
            children.append(parse_node(input, indent + " "))
        if i == ']':
            if current_digits:
                number = int(''.join(current_digits))
                children.append(number)
            return Node(children)
    return children[0]
    

def parse(input):
    pairs = [p.split('\n') for p in input.split('\n\n')]
    return [(parse_node(list(p[0])), parse_node(list(p[1]))) for p in pairs]

def calculate_correctness_of_pairs(signal_pairs):
    def isNode(x):
        return isinstance(x, Node)

    def node_compare(l,r):
        if isNode(l) and isNode(r):
            lc = l.children
            rc = r.children
            
            for i in range(min(len(lc), len(rc))):
                ln = lc[i]
                rn = rc[i]
                c = node_compare(ln, rn)
                if c is not None:
                    return c
            
            if len(lc) < len(rc):
                return True
            elif len(rc) < len(lc):
                return False
            else:
                return None
        elif isNode(l) and not isNode(r):
            return node_compare(l, Node([r]))
        elif not isNode(l) and isNode(r):
            return node_compare(Node([l]), r)
        elif not isNode(l) and not isNode(r):
            if l < r:
                return True
            elif r < l:
                return False
            else:
                return None
    return [node_compare(l, r) for (l, r) in signal_pairs]

def correct_pair_indeces(correctness_of_pairs): 
    pairs_in_right_order = []
    i = 1
    for c in correctness_of_pairs:
        if c:
            pairs_in_right_order.append(i)
        i+=1
    return pairs_in_right_order

print(sum(correct_pair_indeces(calculate_correctness_of_pairs(parse(puzzle_input)))))
