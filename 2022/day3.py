import os
import string

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/day3_input.txt") as file:
    data = file.read()
    rucksacks = data.split("\n")

def create_value_map():
    alpha = string.ascii_lowercase + string.ascii_uppercase
    value_dict = {}
    for letter_value, letter,  in enumerate(alpha, 1):
        value_dict[letter] = letter_value
    return value_dict
        
value_map = create_value_map()
common_item_sum = 0

for rucksack in rucksacks:
    midpoint = len(rucksack)//2
    first_compartment, second_compartment = rucksack[:midpoint], rucksack[midpoint:]
    common_item = list(set(first_compartment)&set(second_compartment))
    common_item_sum += value_map[common_item[0]]
    # print(f"common item is {common_item}, value of item is {value_map[common_item[0]]}, sum so far is {common_item_sum}")

elves_by_group = list(zip(*[iter(rucksacks)]*3))
grouped_badge_sum = 0
for elf_group in elves_by_group:
    first_sack, second_sack, third_sack = elf_group
    common_item = list(set(first_sack)&set(second_sack)&set(third_sack))
    grouped_badge_sum += value_map[common_item[0]]
    print(f"common item is {common_item}, value of item is {value_map[common_item[0]]}, sum so far is {grouped_badge_sum}")
    

