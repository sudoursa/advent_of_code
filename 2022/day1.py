import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/day1_input.txt") as file:
    data = file.read()
    calorie_list = data.split('\n')

calories_per_elf={}
elf=1
for calories in calorie_list:
    if calories == '':
        elf+=1
        continue
    if calories_per_elf.get(elf):
        calories_per_elf[elf] += int(calories)
    else: 
        calories_per_elf[elf] = int(calories)


top_three_elves= []

for elf in range(3):
    top_three_elves.append(max(calories_per_elf.values()))
    del calories_per_elf[max(calories_per_elf, key=calories_per_elf.get)]

print(sum(top_three_elves))