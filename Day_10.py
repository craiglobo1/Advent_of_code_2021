from typing import *

if 1:
    filename = "d10_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

openToClose = {"(" :")", "{" : "}", "[" : "]" , "<" :">"}
closeToOpen = { v:k for k, v in openToClose.items()}

def getPair(char):
    if char in openToClose:
        return openToClose[char]
    else:
        return closeToOpen[char]

def pt1(lines):
    illegal_chars = []

    error_score_table = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }
    for line in lines:
        stack = []
        for char in line:
            if char in openToClose:
                stack.append(char)
            else:
                openPair = getPair(char)
                topOfStack = stack.pop()
                if openPair != topOfStack:
                    illegal_chars.append(char)

    error_score = sum([ error_score_table[char] for char in illegal_chars])
    return error_score

def pt2(lines):
    score_table = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    total_scores = []
    for line in lines:
        stack = []
        corruptLine = False
        for char in line:
            if char in openToClose:
                stack.append(char)
            else:
                openPair = getPair(char)
                topOfStack = stack.pop()
                if openPair != topOfStack:
                    corruptLine = True
                    break

        if len(stack) != 0 and not corruptLine:
            stack.reverse()
            stack = [ getPair(x) for x in stack ]
            total_score = 0
            for val in stack:
                total_score *= 5
                total_score += score_table[val]
            total_scores.append(total_score)
    total_scores.sort()
    return total_scores[len(total_scores) // 2]


print(pt1(lines))
print(pt2(lines))

