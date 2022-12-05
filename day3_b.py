puzzle_input = open("./day3_a_puzzle_input.txt", "r").read()

def parse(input):
    lines = input.split('\n')
    def create_rucksack(line):
        l = int(len(line)/2)
        return (line[0:l], line[l:len(line)])

    return [lines[i:i+3] for i in range(0, len(lines), 3)]

def calculate_group_priorities(groups):
    
    def priority(element):
        o = ord(element)
        if o < 97:
            return o - 38
        else:
            return o - 96

    def group_badge_priority(group):
        c1 = group[0]
        c2 = group[1]
        c3 = group[2]
        
        badge = next(x for x in c1 if x in c2 and x in c3)
        return priority(badge)
    
    return [group_badge_priority(r) for r in groups]

print(sum(calculate_group_priorities(parse(puzzle_input))))