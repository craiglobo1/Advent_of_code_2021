from typing import *

with open("d8_input.txt", "r") as rf:
    lines = rf.readlines()
    lines = [ val.strip()for val in lines]

signal_patterns = []
output_values = []
for line in lines:
    signal_pattern, output_value = line.split("|")
    signal_patterns.append(signal_pattern.split(" "))
    output_values.append(output_value.split(" "))
print(signal_patterns)
print(output_values)

