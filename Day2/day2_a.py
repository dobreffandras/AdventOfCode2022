puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    round_notes = input.split('\n')
    rounds = [r.split(' ') for r in round_notes]
    return rounds

def calculate_round_scores(rounds):
    def shape_score(rnd):
        shape_score = { 'X': 1, 'Y': 2, 'Z': 3 }
        return shape_score[rnd[1]]

    def outcome_score(rnd):
        rules = { 'A': { 'X': 3, 'Y': 6, 'Z': 0 }, 'B': { 'X': 0, 'Y': 3, 'Z': 6 }, 'C': { 'X': 6, 'Y': 0, 'Z': 3 } }
        return rules[rnd[0]][rnd[1]]
    
    return [shape_score(r) + outcome_score(r) for r in rounds]

print(sum(calculate_round_scores(parse(puzzle_input))))