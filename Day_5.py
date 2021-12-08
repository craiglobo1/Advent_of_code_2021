from typing import *
import re

with open("d5_input.txt", "r") as rf:
    lines = rf.readlines()
    lines = [ val.strip()for val in lines]

def pt1(lines):
    board = [ [ 0 for _ in range(1000)] for _ in range(1000) ]

    for val in lines:
        start_point, end_point = val.split(" -> ")
        start_point = [ int(num) for num in start_point.split(",")]
        end_point = [ int(num) for num in end_point.split(",")]
        if start_point[0] == end_point[0]:
            if end_point[1] < start_point[1]:
                temp = end_point[1]
                end_point[1] = start_point[1]
                start_point[1] = temp
            for i in range(start_point[1], end_point[1]+1):
                board[i][start_point[0]] += 1
        
        elif start_point[1] == end_point[1]:
            if end_point[0] < start_point[0]:
                temp = end_point[0]
                end_point[0] = start_point[0]
                start_point[0] = temp
            for i in range(start_point[0], end_point[0]+1):
                board[start_point[1]][i] += 1
        else:
            print("Invalid point combo:", start_point, end_point)

    overlap_points = [ val for row in board for val in row]
    overlap_points = list(filter(lambda x : x > 1, overlap_points))
    return len(overlap_points)

def calculate_m(pt1, pt2):
    if  (pt2[0] - pt1[0]) == 0:
        return 9999
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

def pt2(lines):
    board_size = 1000
    board = [ [ 0 for _ in range(board_size)] for _ in range(board_size) ]

    for val in lines:
        start_point, end_point = val.split(" -> ")
        start_point = [ int(num) for num in start_point.split(",")]
        end_point = [ int(num) for num in end_point.split(",")]
        m = calculate_m(start_point, end_point)
        if start_point[0] == end_point[0]:
            if end_point[1] < start_point[1]:
                temp = end_point[1]
                end_point[1] = start_point[1]
                start_point[1] = temp
            for i in range(start_point[1], end_point[1]+1):
                board[i][start_point[0]] += 1
        
        elif start_point[1] == end_point[1]:
            if end_point[0] < start_point[0]:
                temp = end_point[0]
                end_point[0] = start_point[0]
                start_point[0] = temp
            for i in range(start_point[0], end_point[0]+1):
                board[start_point[1]][i] += 1
        elif m == 1 or m == -1:
            c = start_point[1] - m*start_point[0] 
            if start_point[0] > end_point[0]:
                temp = end_point
                end_point = start_point
                start_point = temp
            for x in range(start_point[0], end_point[0]+1):
                y = int(m*x + c)
                board[y][x] += 1
            
        else:
            print("Invalid point combo:", start_point, end_point)

        overlap_points = [ val for row in board for val in row]
        overlap_points = list(filter(lambda x : x > 1, overlap_points))
        return len(overlap_points)

print(pt1(lines))
print(pt2(lines))





