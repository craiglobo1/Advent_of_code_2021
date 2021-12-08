depth = 0
length = 0
aim = 0

filename = "d2_input.txt"

with open(filename, "r") as rf:
    for line in rf:
        command, value = line.split(" ")
        value = int(value)
        match command:
            case "forward":
                length += value
                depth += aim*value
            case "up":
                aim -= value
            case "down":
                aim += value
            case _ :
                print(f"invalid command {command}")
                exit()

print(depth, length, depth*length)  