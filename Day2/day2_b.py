puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    round_notes = input.split('\n')
    rounds = [r.split(' ') for r in round_notes]
    return rounds

def calculate_round_scores(rounds):
    def shape_score(rnd):
        shapes = { 
            'A': { 
                'X': 3, # loose against Rock -> Scissors(3)
                'Y': 1, # draw with Rock -> Rock(1)
                'Z': 2  # win against Rock -> Paper(2)
            }, 
            'B': {
                'X': 1, # loose against Paper -> Rock(1)
                'Y': 2, # draw with Paper -> Paper(2)
                'Z': 3  # win against Paper -> Scissors(3)
            }, 
            'C': { 
                'X': 2, # loose against Scissors -> Paper(2)
                'Y': 3, # draw with Scissors -> Scissors(3)
                'Z': 1  # win against Scissors -> Rock(1)
            } 
        }
        return shapes[rnd[0]][rnd[1]]

    def outcome_score(rnd):
        rules = { 'X': 0, 'Y': 3, 'Z': 6 }
        return rules[rnd[1]]
    
    return [shape_score(r) + outcome_score(r) for r in rounds]

print(sum(calculate_round_scores(parse(puzzle_input))))