from typing import *

with open("d3_input.txt", "r") as rf:
    lines = rf.readlines()
    lines = [ val.strip()for val in lines]

def pt1(lines : List[str]) -> int:
  no_of_bits = 12

  no_of_ones = [0 for i in range(no_of_bits)]
  most_common_bits = ""

  for i in range(no_of_bits):
      for j in range(len(lines)):
          no_of_ones[i] += int(lines[j][i])
      if no_of_ones[i] > len(lines) - no_of_ones[i]:
          most_common_bits += "1"
      else:
          most_common_bits += "0"

  least_common_bits = list(map(lambda x : str(int(not int(x))), most_common_bits))
  least_common_bits = "".join(least_common_bits)

  mcb_denary = int(most_common_bits, 2)
  lcb_denary = int(least_common_bits, 2)
  return mcb_denary*lcb_denary

def get_most_common_bit(bit_number, bits_list):
  no_of_ones = 0
  for i in range(len(bits_list)):
    if bits_list[i][bit_number] == "1":
      no_of_ones += 1
  
  return int(no_of_ones >= len(bits_list) - no_of_ones)
    

def pt2(lines : List[str]) -> int:
  filtered_diagnositic = lines
  for i in range(len(lines[0])):
    most_common_bit = get_most_common_bit(i, filtered_diagnositic)
    filtered_diagnositic = list(filter(lambda x : x[i] == str(most_common_bit), filtered_diagnositic))
    print(most_common_bit, filtered_diagnositic)
    if len(filtered_diagnositic) == 1:
      break

  oxygen_generator_rating = filtered_diagnositic[0]
  filtered_diagnositic = lines
  for i in range(len(lines[0])):
    least_common_bit = int(not get_most_common_bit(i, filtered_diagnositic))
    filtered_diagnositic = list(filter(lambda x : x[i] == str(least_common_bit), filtered_diagnositic))
    if len(filtered_diagnositic) == 1:
      break
  CO2_scrubber_rating = filtered_diagnositic[0]

  CO2_scrubber_rating = int(CO2_scrubber_rating, 2)
  oxygen_generator_rating = int(oxygen_generator_rating, 2)
  print(CO2_scrubber_rating, oxygen_generator_rating)
  
  return CO2_scrubber_rating * oxygen_generator_rating

print(pt2(lines))