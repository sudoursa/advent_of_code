import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/day4_input.txt") as file:
    elf_pairs = []
    for line in file.readlines():
        elf_pairs.append(line.strip().split(","))
    
print(elf_pairs)

def convert_to_numbers(pairs):
    result = []
    for pair in pairs.split(','):
        a, b = pair.split('-')
        a, b = int(a), int(b)
        result.extend(range(a, b + 1))
    return result
                
sections_as_ints = []
for pair in elf_pairs:
    for sections in pair:
        sections_as_ints.append(convert_to_numbers(sections))

group_set = list(zip(*[iter(sections_as_ints)]*2))

contained_pairs = 0
for pair in group_set:
    if set(pair[0]).issubset(pair[1]):
        contained_pairs +=1
    elif set(pair[1]).issubset(pair[0]):
        contained_pairs +=1

# print(contained_pairs)


overlapping_pairs = 0
for pair in group_set:
    if any(section in pair[0] for section in pair[1]):
        overlapping_pairs += 1

# print(overlapping_pairs)

