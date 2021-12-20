from copy import copy

if 1:
    filename = "d14_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

startPolymer = lines.pop(0)
lines.pop(0)
patterns = {}
for line in lines:
    pattern, value = line.split(" -> ")
    patterns[pattern] = value

def pt1(startPolymer, patterns):
    curPolymer = startPolymer
    for _ in range(10):
        nextPolymer = ""
        for i in range(len(curPolymer)-1):
            curPattern = curPolymer[i:i+2]
            if curPattern in patterns:
                nextPolymer += curPattern[0] + patterns[curPattern]
            else:
                nextPolymer += curPattern[0]
        nextPolymer += curPolymer[-1]
        curPolymer = nextPolymer

    allChars = set(curPolymer)
    maxOccurs = -1
    minOccurs = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    for char in allChars:
        no_of_occurs = curPolymer.count(char)
        if no_of_occurs > maxOccurs:
            maxOccurs = no_of_occurs
        if no_of_occurs < minOccurs:
            minOccurs = no_of_occurs
    return maxOccurs-minOccurs

# optimizated datatype for pt 1
def pt2(startPolymer, patterns):
    curPolymer = {}
    for i in range(len(startPolymer)-1):
        curPattern = startPolymer[i:i+2]
        if curPattern in curPolymer:
            curPolymer[curPattern] += 1
        else:
            curPolymer[curPattern] = 1

    for _ in range(40):
        nextPolymer = {}
        for pat, amt in curPolymer.items():
            if pat in patterns:
                newPatOne = pat[0] + patterns[pat]
                newPatTwo = patterns[pat] + pat[1]
                amtOfPat = curPolymer[pat]
                curPolymer[pat] = 0
                if newPatOne in nextPolymer:
                    nextPolymer[newPatOne] += amtOfPat
                else:
                    nextPolymer[newPatOne] = amtOfPat

                if newPatTwo in nextPolymer:
                    nextPolymer[newPatTwo] += amtOfPat
                else:
                    nextPolymer[newPatTwo] = amtOfPat
        curPolymer = nextPolymer
    
    charAmt = {}
    charAmt[startPolymer[-1]] = 1
    for pat, val in curPolymer.items():
        if pat[0] in charAmt:
            charAmt[pat[0]] += val
        else:
            charAmt[pat[0]] = val
    
    maxOccur = max(charAmt.values())
    leastOccur = min(charAmt.values())
    return maxOccur - leastOccur
        
        

print(pt1(startPolymer, patterns))
print(pt2(startPolymer, patterns))





