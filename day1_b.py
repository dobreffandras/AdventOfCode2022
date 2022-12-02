puzzle_input = open("./day1_a_puzzle_input.txt", "r").read()

def parse(input):
    elf_inventories = input.split('\n\n')
    elves_calorie_notes = [inv.split('\n') for inv in elf_inventories]
    elves_calories = [[int(cal) for cal in elf_cal] for elf_cal in elves_calorie_notes]
    return elves_calories

def max_collected_calories(elves_calories):
    total_calories = [sum(elf_calories) for elf_calories in elves_calories]
    top3 = sorted(total_calories, reverse=True)[:3]
    return sum(top3)
    

print(max_collected_calories(parse(puzzle_input)))
