from typing import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if 0:
    filename = "d11_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

def flash(energy_levels, row, col, flashed : Set):
    if (row, col) in flashed:
        return energy_levels, flashed
    flashed.add((row, col))
    energy_levels[row][col] = 0

    offsets = [ (i,j) for i in range(-1, 2) for j in range(-1, 2)]
    offsets.remove((0,0))
    for offset in offsets:
        o_row, o_col = offset[0]+row, offset[1]+col
        try:
            if energy_levels[o_row][o_col] > 9:
                flash(energy_levels, o_row, o_col, flashed)
            else:
                    energy_levels[o_row][o_col] += 1
        except:
            pass

    
    return energy_levels, flashed



energy_levels = [list(map( lambda x: int(x),val)) for val in lines]

steps = 2

for step in range(steps):
    for i, row in enumerate(energy_levels):
        for j, col in enumerate(row):
            energy_levels[i][j] += 1
    
    print("\n".join([ "".join(list(map(lambda x: str(x), row))) for row in energy_levels]))
    flashed = set()
    for i, row in enumerate(energy_levels):
        for j, col in enumerate(row):
            if energy_levels[i][j] > 9:
                energy_levels, flashed = flash(energy_levels, i, j, flashed)
    print()



