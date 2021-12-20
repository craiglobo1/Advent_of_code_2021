from queue import PriorityQueue
from copy import copy

if 1:
    filename = "d15_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

riskMap = [ [ int(val) for val in list(line)] for line in lines]

def getAdj(x,y):
    yield x + 1 , y
    yield x     , y + 1
    yield x - 1 , y
    yield x     , y - 1

def findCost(riskMap):
    pq = PriorityQueue()
    pq.put((0,0,0))
    N = len(riskMap)
    M = len(riskMap[0])
    costs = {}
    costs[(0,0)] = 0
    visited = set()

    while not pq.empty():
        cur_cost, row, col = pq.get()
        if (row, col) in visited:
            continue

        visited.add((row, col))
        costs[(row, col)] = cur_cost

        if row == N - 1 and col == M -1:
            return costs[(N-1, M-1)]

        for rr, cc in getAdj(row, col):
            if not (0 <= rr < N and 0 <= cc < M):
                continue
            
            pq.put((cur_cost + riskMap[rr][cc], rr, cc))

def pt2(riskMap):
    N = len(riskMap)
    M = len(riskMap[0])
    addWrap = lambda x : x%9 + 1
    for row in range(len(riskMap)):
        for _ in range(4):
            riskMap[row] = riskMap[row] + list(map(addWrap, riskMap[row][-N:]))

    newRiskMap = copy(riskMap)
    for i in range(4):
        newRiskMap = [list(map(addWrap, row)) for row in newRiskMap]
        riskMap += newRiskMap
        
    return findCost(riskMap)

def displayRk(riskMap):
    riskMap = [ [ str(val) for val in row] for row in riskMap]
    riskMap = list(map(lambda row: "".join(row), riskMap))
    riskMap = "\n".join(riskMap)

    print(riskMap)


print(findCost(riskMap))
print(pt2(riskMap))