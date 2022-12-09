puzzle_input = open("./puzzle_input.txt", "r").read()

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
            left_neighbors = list(reversed(row[0:col_idx]))
            right_neighbors = row[(col_idx+1):w]
            top_neighbors = list(reversed(col[0:row_idx]))
            bottom_neighbors = col[(row_idx+1):h]
            
            trees_with_neighbors.append((tree, dict(left=left_neighbors, right=right_neighbors, top=top_neighbors, bottom=bottom_neighbors)))
    
    return trees_with_neighbors
            
def calculate_scenic_scores(trees_with_neighbors):
    def scenic_score(tree, neighbors):
        score = 0
        for n in neighbors:
            score += 1
            if tree <= n:
                break;
            
        return score
    
    trees_with_scores = []
    for (tree, neighbors) in trees_with_neighbors:
        left = scenic_score(tree, neighbors['left'])
        right = scenic_score(tree, neighbors['right'])
        top = scenic_score(tree, neighbors['top'])
        bottom = scenic_score(tree, neighbors['bottom'])
    
        trees_with_scores.append((tree, (left*right*bottom*top)))
    
    return trees_with_scores
        
            
def find_max_scenic_score(trees_scores):
    return max([s for (_, s) in trees_scores])
    
print(find_max_scenic_score(calculate_scenic_scores(generate_tree_neighbors(parse(puzzle_input)))))