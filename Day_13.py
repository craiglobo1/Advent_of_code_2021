if 1:
    filename = "d13_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

def formatLines(lines):
    breakIdx = None
    for i in range(len(lines)-1, -1, -1):
        line = lines[i]
        if line == "":
            breakIdx = i
            break

    coordStrs = lines[:breakIdx]
    foldStrs = lines[breakIdx+1:]

    coordVals = [tuple(map(lambda x: int(x), val.split(','))) for val in coordStrs]
    foldStrs = [ val[11:] for val in foldStrs]
    foldVals = []

    for i,val in enumerate(foldStrs):
        if val[0] == "x":
            foldVals.append((int(val[2:]), 0))
        if val[0] == "y":
            foldVals.append((0, int(val[2:])))
    
    return coordVals, foldVals

def pt1(lines):
    coordVals, foldVals = formatLines(lines)
    fold = foldVals[0]
    page = set()
    foldIdx = int(fold[0] == 0)
    for coord in coordVals:
        diff = coord[foldIdx] - fold[foldIdx]
        if diff > 0:
            coord = list(coord)
            coord[foldIdx] = coord[foldIdx]-2*diff
            coord = tuple(coord)
            
        page.add(coord)

    return len(page)

def pt2(lines):
    coordVals, foldVals = formatLines(lines)
    for fold in foldVals:
        page = set()
        foldIdx = int(fold[0] == 0)
        for coord in coordVals:
            diff = coord[foldIdx] - fold[foldIdx]
            if diff > 0:
                coord = list(coord)
                coord[foldIdx] = coord[foldIdx]-2*diff
                coord = tuple(coord)
            page.add(coord)
        coordVals = page

    xMax = max([val[0] for val in coordVals])
    yMax = max([val[1] for val in coordVals])
    pageStr = ""
    for y in range(yMax+1):
        for x in range(xMax+1):
            if (x, y) in coordVals:
                pageStr += "#"
            else:
                pageStr += "."
        pageStr += "\n"
    
    return pageStr



print(pt1(lines))
print(pt2(lines))