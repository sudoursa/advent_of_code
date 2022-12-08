import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/day5_input.txt") as file:
    stacks, instructions = file.read().split("\n\n")

STACK_LENGTH = 4

def get_column_number(stacks):
    return int(stacks.split("\n")[-1][-2])


def create_ordered_stacks(stack_count, stacks):
    stacks = stacks.split("\n")[:-1]
    stack_map = defaultdict(list)
    for stack in stacks:
        columns = [stack[i:i+STACK_LENGTH].strip() for i in range(0, len(stack), STACK_LENGTH)]
        for stack_id, package in enumerate(columns, 1):
            stack_map[stack_id].append(package) if package else None
    return(stack_map)

def convert_to_simple_instructions(instructions):
    instructions = instructions.split("\n")
    simple_instructions = []
    for instruction in instructions:
        simple_instructions.append([int(i) for i in instruction.split() if i.isdigit()])
    return simple_instructions

def process_instructions_on_9000(simple_instructions, stack_map):
    for instruction in simple_instructions:
        package_count, from_stack, to_stack = instruction
        for _ in range(package_count):
            stack_map[to_stack].insert(0, stack_map[from_stack][0])
            del stack_map[from_stack][0]
    return stack_map

def process_instructions_on_9001(simple_instructions, stack_map):
    for instruction in simple_instructions:
        package_count, from_stack, to_stack = instruction
        move_list = stack_map[from_stack][0:package_count]
        del stack_map[from_stack][0:package_count]
        for i in range(len(move_list)):
            stack_map[to_stack].insert(i, move_list[i])
    return stack_map


# end_state = process_instructions_on_9000(convert_to_simple_instructions(instructions),create_ordered_stacks(get_column_number(stacks), stacks))
end_state = process_instructions_on_9001(convert_to_simple_instructions(instructions),create_ordered_stacks(get_column_number(stacks), stacks))

for stack in range(1, get_column_number(stacks)+1):
    print(end_state[stack][0][1], end="")
