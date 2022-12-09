puzzle_input = open("./puzzle_input.txt", "r").read()

def find_first_four_different_index(datastream):
    for i in range(0, len(datastream)-3):
        if(len(set(datastream[i:i+4])) == 4):
            return i+4

print(find_first_four_different_index(puzzle_input))