puzzle_input = open("./day6_a_puzzle_input.txt", "r").read()

def find_first_four_different_index(datastream):
    for i in range(0, len(datastream)-13):
        if(len(set(datastream[i:i+14])) == 14):
            return i+14

print(find_first_four_different_index(puzzle_input))