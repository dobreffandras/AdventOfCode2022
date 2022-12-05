puzzle_input = open("./day3_a_puzzle_input.txt", "r").read()

def parse(input):
    lines = input.split('\n')
    def create_rucksack(line):
        l = int(len(line)/2)
        return (line[0:l], line[l:len(line)])

    return [create_rucksack(line) for line in lines]

def calculate_priorities(rucksacks):
    
    def priority(element):
        o = ord(element)
        if o < 97:
            return o - 38
        else:
            return o - 96

    def rucksack_priority(rucksack):
        c1 = rucksack[0]
        c2 = rucksack[1]
        
        faulty_item = next(x for x in c1 if x in c2)
        return priority(faulty_item)
    
    return [rucksack_priority(r) for r in rucksacks]

print(sum(calculate_priorities(parse(puzzle_input))))