puzzle_input = open("./puzzle_input.txt", "r").read()

def parse(input):

    def parse_range(range_str):
        x = range_str.split('-')
        return (int(x[0]), int(x[1]))

    lines = input.split('\n')
    range_pairs = [l.split(',') for l in lines]
    return [(parse_range(rp[0]), parse_range(rp[1])) for rp in range_pairs]
    
def count_overlapping_ranges(range_pairs):

    def overlap_each_other(range_pair):
          
        def overlaps(range1, range2):
            return range1[0] <= range2[0] <= range1[1] or range1[0] <= range2[1] <= range1[1] 
        
        r1 = range_pair[0]
        r2 = range_pair[1]
        return overlaps(r1, r2) or overlaps(r2, r1)

    return [True for rp in range_pairs if overlap_each_other(rp)].count(True)

print(count_overlapping_ranges(parse(puzzle_input)))