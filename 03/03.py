with open('input.txt') as fp:
    lines = fp.readlines()

## R3D1
treeCount_3_1 = 0
pos = 0
for i in lines:
    if i[pos] == '#':
        treeCount_3_1 += 1
    pos += 3
    if pos > 30:
        pos -= 31
print("Answer 1:" + str(treeCount_3_1))

## R1D1
treeCount_1_1 = 0
pos = 0
for i in lines:
    if i[pos] == '#':
        treeCount_1_1 += 1
    pos += 1
    if pos > 30:
        pos -= 31
print("R1D1: " + str(treeCount_1_1))

## R5D1
treeCount_5_1 = 0
pos = 0
for i in lines:
    if i[pos] == '#':
        treeCount_5_1 += 1
    pos += 5
    if pos > 30:
        pos -= 31
print("R5D1: " + str(treeCount_5_1))

## R7D1
treeCount_7_1 = 0
pos = 0
for i in lines:
    if i[pos] == '#':
        treeCount_7_1 += 1
    pos += 7
    if pos > 30:
        pos -= 31
print("R7D1: " + str(treeCount_7_1))

## R1D2
treeCount_1_2 = 0
pos = 0
row = 0
for i in lines:
    if row % 2 == 0:
        if i[pos] == '#':
            treeCount_1_2 += 1
        pos += 1
        if pos > 30:
            pos -= 31
    row += 1
print("R1D2: " + str(treeCount_1_2))

print("Answer 2: " + str(treeCount_3_1 * treeCount_1_1 * treeCount_5_1 * treeCount_1_2 * treeCount_7_1))

