import os
from typing import Dict, Union

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/day7_input.txt") as file:
    data = file.read()

output = data

directory_map = {}

def determine_action(current_dir, line):
    if line.startswith("$ cd"):
        change_dir(current_dir, line)
    if line == "$ ls":
        pass
    if line.startswith("dir "):
        # enter dir layer
        pass
    if line[0].isdigit():
        # add entry for size to dir layer
        pass

def return_to_root(line):
    return []

def return_one_dir_up(current_dir):
    return current_dir[:-1]

def change_dir(current_dir, command):
    # TODO strip dir and navigate
    if command== "$ cd /":
        return return_to_root()
    if command == "$ cd ..":
        return return_one_dir_up(command)
    _, _, dir = command.split(" ")
    empty_dir = {dir: None}
    return current_dir.append(empty_dir)

current_dir = []
for line in output:
    # loop through commands
    # read and navigate
    # populate dict with each file
    # sum files under 100000
    pass