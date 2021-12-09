from typing import *

if 1:
    filename = "d9_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

def inHeightMap(point, maxWidth, maxHeight):
    return point[0] >= 0 and point[0] < maxWidth and point[1] >= 0 and point[1] < maxHeight

def getAdjacentPoints(heights, loc):
    offsets = [ [-1,0], [1,0], [0, 1], [0,-1]]
    points = []
    for offset in offsets:
        if inHeightMap([loc[0] + offset[0], loc[1] + offset[1]], len(heights), len(heights[0])):
            points.append(heights[loc[0] + offset[0]][loc[1] + offset[1]])
    return points


def getAdjacentPointLocs(heights, loc):
    offsets = [ [-1,0], [1,0], [0, 1], [0,-1]]
    points = []
    for offset in offsets:
        if inHeightMap([loc[0] + offset[0], loc[1] + offset[1]], len(heights), len(heights[0])):
            points.append([loc[0] + offset[0], loc[1] + offset[1]])
    return points

def pt1(lines):

    heights = [ list(row) for row in lines]
    heights = [ [ int(val) for val in row] for row in lines]

    risk_levels = []
    for i, row in enumerate(heights):
        for j, val in enumerate(row):
            Ap = getAdjacentPoints(heights, (i,j))
            if val < min(Ap):
                risk_levels.append(val + 1) 

    return sum(risk_levels)

def getBasin(heights, loc, found : Set):
    found.add(tuple(loc))
    ApLocs = getAdjacentPointLocs(heights, loc)
    ApLocs = list(filter(lambda x: heights[x[0]][x[1]] != 9, ApLocs))
    for val in ApLocs:
        if tuple(val) not in found:
            getBasin(heights, val, found)
    
    return found
        
    

def pt2(lines):
    heights = [ list(row) for row in lines]
    heights = [ [ int(val) for val in row] for row in lines]

    basins = []
    for i, row in enumerate(heights):
        for j, val in enumerate(row):
            Ap = getAdjacentPoints(heights, (i,j))
            if val < min(Ap):
                basin = getBasin(heights, (i, j), set())
                basins.append(basin)

    lengthBasins = [ len(val) for val in basins]
    lengthBasins.sort()
    return lengthBasins[-1] * lengthBasins[-2] * lengthBasins[-3]

print(pt1(lines))
print(pt2(lines))
