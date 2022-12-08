puzzle_input = open("./day8_a_puzzle_input.txt", "r").read()

def parse(input):
    lines = input.split('\n')
    return [[int(n) for n in line] for line in lines]

def generate_tree_neighbors(trees):
    h = len(trees)
    w = len(trees[0])
    
    trees_with_neighbors = []
    
    for row_idx in range(h):
        for col_idx in range(w):
            row = trees[row_idx]
            col = [trees[x][col_idx] for x in range(h)]
            
            tree = trees[row_idx][col_idx]
            left_neighbors = row[0:col_idx]
            right_neighbors = row[(col_idx+1):w]
            top_neighbors = col[0:row_idx]
            bottom_neighbors = col[(row_idx+1):h]
            
            trees_with_neighbors.append((tree, [left_neighbors, right_neighbors, top_neighbors, bottom_neighbors]))
    
    return trees_with_neighbors
            
def to_is_visible(trees_with_neighbors):
    def not_hidden_by(tree, neighbors):
        return all([n < tree for n in neighbors])
    
    def is_visible(tree, neighbors):
        return any([not_hidden_by(tree, n) for n in neighbors])
    
    return [(tree, is_visible(tree, neighbors))  for (tree, neighbors) in trees_with_neighbors]
            
def count_visible_trees(trees_visible):
    return [t_v[1] for t_v in trees_visible].count(True)
    
print(count_visible_trees(to_is_visible(generate_tree_neighbors(parse(puzzle_input)))))