from typing import *

with open("d6_input.txt", "r") as rf:
    lines = rf.readlines()
    lines = [ val.strip()for val in lines]

def pt1(lines):

    values = [ int(val) for val in lines[0].split(",")]

    days = 80
    for _ in range(days):
        for i, val in enumerate(values):
            if val == 0:
                values[i] = 7
                values.append(9)
            
            values[i] -= 1

    return len(values)

def pt2(lines):
    intial_values = [ int(val) for val in lines[0].split(",")]
    fishClock = { i: 0 for i in range(9)}
    for val in intial_values:
        fishClock[val] += 1

    no_of_days = 256
    for day in range(no_of_days):
        oldZeroTimer = fishClock[0]
        for timer, amt in list(fishClock.items())[1:]:
            fishClock[timer-1] = amt
        fishClock[8] = 0

        if oldZeroTimer > 0:
            fishClock[6] += oldZeroTimer
            fishClock[8] += oldZeroTimer

    return sum(map(lambda i: i[1], fishClock.items()))


print(pt1(lines))
print(pt2(lines))


