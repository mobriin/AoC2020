with open('input.txt') as fp:
    lines = [line.rstrip() for line in fp]
lines2 = lines
def countSurounding1(x, y):
    count = 0
    if y != 0:
        if x != 0 and lines[y-1][x-1] == "#":
            count += 1 
        if lines[y-1][x] == "#":
            count += 1 
        if x != len(lines[y-1]) - 1 and lines[y-1][x+1] == "#":
            count += 1
    if x != 0 and lines[y][x-1] == "#":
        count += 1
    if x != len(lines[y]) - 1 and lines[y][x+1] == "#":
        count += 1
    if y != len(lines) - 1:
        if x != 0 and lines[y+1][x-1] == "#":
            count += 1 
        if lines[y+1][x] == "#":
            count += 1 
        if x != len(lines[y+1]) - 1 and lines[y+1][x+1] == "#":
            count += 1
    return count

def countSurounding2(x, y):
    count = 0
    dist = 1
    while dist <= y and dist <= x:
        if lines2[y-dist][x-dist] == "#":
            count += 1
            break
        elif lines2[y-dist][x-dist] == "L":
            break
        dist += 1

    dist = 1
    while dist <= y:
        if lines2[y-dist][x] == "#":
            count += 1
            break
        elif lines2[y-dist][x] == "L":
            break
        dist += 1

    dist = 1
    while dist <= y and dist + x < len(lines2[y]):
        if lines2[y-dist][x+dist] == "#":
            count += 1
            break
        elif lines2[y-dist][x+dist] == "L":
            break
        dist += 1

    dist = 1
    while dist <= x:
        if lines2[y][x-dist] == "#":
            count += 1
            break
        elif lines2[y][x-dist] == "L":
            break
        dist += 1

    dist = 1
    while x + dist < len(lines2[y]):
        if lines2[y][x+dist] == "#":
            count += 1
            break
        elif lines2[y][x+dist] == "L":
            break
        dist += 1

    dist = 1
    while dist + y < len(lines2) and dist <= x:
        if lines2[y+dist][x-dist] == "#":
            count += 1 
            break
        elif lines2[y+dist][x-dist] == "L":
            break
        dist += 1

    dist = 1
    while dist + y < len(lines2):
        if lines2[y+dist][x] == "#":
            count += 1 
            break
        elif lines2[y+dist][x] == "L":
            break
        dist += 1

    dist = 1
    while dist + y < len(lines2) and dist + x < len(lines2[y]):
        if lines2[y+dist][x+dist] == "#":
            count += 1
            break
        elif lines2[y+dist][x+dist] == "L":
            break
        dist += 1
    return count

while True:
    newSeating = []
    for y in range(len(lines)):
        newSeating.append("")
        for x in range(len(lines[y])):
            count = countSurounding1(x, y)
            if lines[y][x] == "L":
                if count == 0:
                    newSeating[y] += "#"
                else:
                    newSeating[y] += "L"
            elif lines[y][x] == "#":
                if count >= 4:
                    newSeating[y] += "L"
                else:
                    newSeating[y] += "#"
            else:
                newSeating[y] += "."
    if newSeating == lines:
        break
    lines = newSeating

count = 0
for i in lines:
    for x in i:
        if x == "#":
            count += 1
print("Answer 1: " + str(count))

while True:
    newSeating = []
    for y in range(len(lines2)):
        newSeating.append("")
        for x in range(len(lines2[y])):
            count = countSurounding2(x, y)
            if lines2[y][x] == "L":
                if count == 0:
                    newSeating[y] += "#"
                else:
                    newSeating[y] += "L"
            elif lines2[y][x] == "#":
                if count >= 5:
                    newSeating[y] += "L"
                else:
                    newSeating[y] += "#"
            else:
                newSeating[y] += "."
    if newSeating == lines2:
        break
    lines2 = newSeating
count = 0
for i in lines2:
    for x in i:
        if x == "#":
            count += 1
print("Answer 2: " + str(count))