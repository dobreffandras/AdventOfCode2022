import re

puzzle_input = open("./puzzle_input.txt", "r").read()

class Monkey:
    def build_next_monkey(condition_num, for_true, for_false):
        def condition(x):
            return for_true if x % condition_num == 0 else for_false
        return condition
        
    def __init__(self, number, items, operation, condition, monkey_for_true, monkey_for_false):
        self.number = number
        self.items = items
        self.operation = operation
        self.next_monkey = Monkey.build_next_monkey(condition, monkey_for_true, monkey_for_false)
        
    def __str__(self):
        return f"{type(self).__name__}(#{self.number}, items={self.items})"

def parse(input):
    monkey_name_pattern = re.compile("Monkey (\d)")
    starting_items_pattern = re.compile("  Starting items: (.*)")
    op_with_num_pattern = re.compile("  Operation: new = old ([+\*]) (\d+)")
    op_with_var_pattern = re.compile("  Operation: new = old ([+\*]) old")
    test_condition_pattern = re.compile("  Test: divisible by (\d+)")
    monkey_for_true_pattern = re.compile("    If true: throw to monkey (\d+)")
    monkey_for_false_pattern = re.compile("    If false: throw to monkey (\d+)")
    
    def parse_operation(line):
        if op_with_num_pattern.match(line):
            operator = op_with_num_pattern.search(line).group(1)
            num = int(op_with_num_pattern.search(line).group(2))
            if operator == '+':
                return lambda x: x + num
            elif operator == '*':
                return lambda x: x * num
        elif op_with_var_pattern.match(line):
            operator = op_with_var_pattern.search(line).group(1)
            if operator == '+':
                return lambda x: x + x
            elif operator == '*':
                return lambda x: x * x
    
    def parse_monkey_block(block):
        lines = block.split('\n')
        num = int(monkey_name_pattern.search(lines[0]).group(1))
        items = [int(i) for i in starting_items_pattern.search(lines[1]).group(1).split(', ')]
        operation = parse_operation(lines[2])
        condition_num = int(test_condition_pattern.search(lines[3]).group(1))
        monkey_for_true = int(monkey_for_true_pattern.search(lines[4]).group(1))
        monkey_for_false = int(monkey_for_false_pattern.search(lines[5]).group(1))
        return Monkey(num, items, operation, condition_num, monkey_for_true, monkey_for_false)

    return dict([(m.number, m) for m in [parse_monkey_block(monkey_block) for monkey_block in input.split('\n\n')]])
    
def run(monkeys):
    activities = dict([(m,0) for m in monkeys])
    for round_num in range(1, 21):
        for monkey_num in monkeys:
            monkey = monkeys[monkey_num]
            while monkey.items:
                activities[monkey_num] += 1
                item = monkey.items.pop(0)
                worry_level = monkey.operation(item)
                worry_level = divmod(worry_level, 3)[0]
                receiver_monkey = monkeys[monkey.next_monkey(worry_level)]
                receiver_monkey.items.append(worry_level)
    
    activities_sorted = sorted(activities.values(), reverse=True)
    return activities_sorted[0]*activities_sorted[1]
    

print(run(parse(puzzle_input)))