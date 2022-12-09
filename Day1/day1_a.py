puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):
    elf_inventories = input.split('\n\n')
    elves_calorie_notes = [inv.split('\n') for inv in elf_inventories]
    elves_calories = [[int(cal) for cal in elf_cal] for elf_cal in elves_calorie_notes]
    return elves_calories

def max_collected_calories(elves_calories):
    return max([sum(elf_calories) for elf_calories in elves_calories])
    

print(max_collected_calories(parse(puzzle_input)))
