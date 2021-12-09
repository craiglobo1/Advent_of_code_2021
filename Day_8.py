from typing import *

"""
  0:      1:      2:      3:      4:
 aaaa            aaaa    aaaa        
b    c       c       c       c  b    c
b    c       c       c       c  b    c
                 dddd    dddd    dddd
e    f       f  e            f       f
e    f       f  e            f       f
 gggg            gggg    gggg        

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b       b            c  b    c  b    c
b       b            c  b    c  b    c
 dddd    dddd            dddd    dddd
     f  e    f       f  e    f       f
     f  e    f       f  e    f       f
 gggg    gggg            gggg    gggg
"""

with open("d8_input.txt", "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]


def parse_lines(lines):
    signal_patterns = []
    output_values = []
    for line in lines:
        signal_pattern, output_value = line.split("|")
        signal_patterns.append(
            list(filter(lambda x: x != "", signal_pattern.split(" "))))
        output_values.append(
            list(filter(lambda x: x != "", output_value.split(" "))))
    return signal_patterns, output_values


def pt1(lines):
    _, output_values = parse_lines(lines)
    total_unique_val = 0
    for output_value in output_values:
        for number in output_value:
            if len(number) in [2, 4, 3, 7]:
                total_unique_val += 1
    return total_unique_val


def deduce_digit_mapping(signal_pattern):
    new_seg_map = {}
    for segments in signal_pattern:
        match len(segments):
            case 2:
               new_seg_map[1] = set(segments)
            case 3:
               new_seg_map[7] = set(segments)
            case 4:
               new_seg_map[4] = set(segments)
            case 7:
               new_seg_map[8] = set(segments)
    
    for segments in signal_pattern:
        match len(segments):
            case 6:
                # 0 6 9 | 3
                six_pattern = new_seg_map[8].difference(new_seg_map[1])
                if six_pattern.issubset(segments):
                    new_seg_map[6] = set(segments)
                zero_pattern = new_seg_map[8].difference(new_seg_map[4])
                if zero_pattern.issubset(segments) and not six_pattern.issubset(segments):
                    new_seg_map[0] = set(segments)
                if new_seg_map[4].issubset(segments):
                    new_seg_map[9] = set(segments)
    
    for segments in signal_pattern:
        match len(segments):
            case 5:
                # 2 | 3 5 
                if new_seg_map[7].issubset(segments):
                    new_seg_map[3] = set(segments)
                five_pattern = new_seg_map[9].difference(new_seg_map[1])
                if five_pattern.issubset(segments):
                    new_seg_map[5] = set(segments)
                two_pattern = new_seg_map[8].difference(new_seg_map[9])
                if two_pattern.issubset(segments):
                    new_seg_map[2] = set(segments)                
    return { "".join(sorted(v)) : k for k, v in new_seg_map.items()}

    

def pt2(lines):
    signal_patterns, output_values = parse_lines(lines)
    sum_of_output_values = 0
    for i in range(len(signal_patterns)):
        cur_mapping = deduce_digit_mapping(signal_patterns[i])
        number = 0
        for j, digit_seg in enumerate(output_values[i]):
            digit =cur_mapping["".join(sorted(digit_seg))]
            exp = len(output_values[i]) - j -1
            number += 10**exp * digit
        sum_of_output_values += number
    return sum_of_output_values


print(pt1(lines))
print(pt2(lines))

