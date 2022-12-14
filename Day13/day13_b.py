puzzle_input = open("./puzzle_input.txt", "r").read()

class Node:
    def __init__(self, children):
        self.children = children
        
    def __repr__(self):
        return f'{type(self).__name__}({self.children})'

divider_signal1 = Node([Node([2])])
divider_signal2 = Node([Node([6])])

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
    signals = [l for l in input.split('\n') if l != '']
    return [parse_node(list(s)) for s in signals]

def add_divider_signals(signals):
    signals.append(divider_signal1)
    signals.append(divider_signal2)
    return signals

def node_compare(l,r):
    def isNode(x):
        return isinstance(x, Node)
        
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

def sort_signals(signals):
    
    def bubble_sort(signal_list):
        for i in range(len(signal_list)):
            for j in range(len(signal_list) - 1):
                if i == j:
                    continue
                x, y = signal_list[i], signal_list[j]
                if node_compare(x, y):
                    signal_list[j] = x
                    signal_list[i] = y

        return signal_list
    
    return bubble_sort(signals)

def get_product_of_divider_signal_indeces(signals):
    p = 1
    for i in range(len(signals)):
        if node_compare(signals[i], divider_signal1) is None or node_compare(signals[i], divider_signal2) is None:
            p *= (i+1)
    return p

print(get_product_of_divider_signal_indeces(sort_signals(add_divider_signals(parse(puzzle_input)))))
