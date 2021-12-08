filename = "d1_input.txt"
with open(filename, 'r') as rf:
    values = rf.readlines()

values = [ int(val) for val in values]

increased = 0
for i in range(3, len(values)):
    prev_sum =  values[i-1] + values[i-2] + values[i-3]
    cur_sum = values[i] + values[i-1] + values[i-2]
    print(prev_sum, cur_sum)
    if cur_sum > prev_sum:
        increased += 1

print(increased)



    