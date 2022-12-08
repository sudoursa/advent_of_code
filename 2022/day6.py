import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/day6_input.txt") as file:
    data = file.read()


signal = []
for count, character in enumerate(data):
    if count <= 13: # 3 for signal
        signal.append(character)
        continue
    if len(set(signal)) != 14: # 4 for signal
        del signal[0]
        signal.append(character)
        continue
    else: 
        print(f"character is {character} signal ends at {count} and unique characters are {''.join(signal)}")
        break    