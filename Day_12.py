if 1:
    filename = "d12_input.txt"
else:
    filename = "sample.txt"

with open(filename, "r") as rf:
    lines = rf.readlines()
    lines = [val.strip()for val in lines]

map = {}
for line in lines:
    froms, to = line.split("-")
    if froms not in map:
        map[froms] = []

    if to not in map:
        map[to] = []
    map[froms].append(to)
    map[to].append(froms)

print(map)

def traverse_map(map, to, visited):
    print(to)
    visited.add(to)
    if to == "end":
        return
    for node in map[to]:
        if to not in visited:
            traverse_map(map, node, visited)

traverse_map(map, "start", set())