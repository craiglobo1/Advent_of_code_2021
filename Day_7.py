from typing import *

with open("d7_input.txt", "r") as rf:
    lines = rf.readlines()
    lines = [ val.strip()for val in lines]

crab_postions = lines[0].split(",")
crab_postions = [ int(val) for val in crab_postions]

max_pos = max(crab_postions)
min_pos = min(crab_postions)

leastfuelUsed = 99999999999999999999999999999999999999999999999999999999999999999

for i in range(min_pos, max_pos+1):
    fuelUsed = 0
    for pos in crab_postions:
        fuelDiff = abs(pos - i)
        fuelUsed += 0.5*fuelDiff**2 + 0.5*fuelDiff
    
    if fuelUsed < leastfuelUsed:
        leastfuelUsed = fuelUsed

print(leastfuelUsed)