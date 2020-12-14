with open('c:\\repos\\AoC2020\\12\\input.txt') as fp:
    lines = [line.rstrip() for line in fp]

directions = {"E" : (1, 0), "S" : (0, -1),  "W" : (-1, 0), "N" : (0, 1)}
rotations = {"R" : 1, "L" : -1}
speed = [10, 1]
x1 = 0
x2 = 0
y1 = 0
y2 = 0
dir = "E"
for i in lines:
    if i[0] in directions:
        x1 += directions[i[0]][0]*int(i[1:])
        y1 += directions[i[0]][1]*int(i[1:])
        speed[0] += directions[i[0]][0]*int(i[1:])
        speed[1] += directions[i[0]][1]*int(i[1:])
    elif i[0] in rotations:
        dirList = list(directions)
        turns = int(rotations[i[0]]*int(i[1:])/90) % 4
        dir = dirList[(dirList.index(dir) + turns) % 4]
        if turns == 1:
            temp = speed[0]
            speed[0] = speed[1]
            speed[1] = -temp
        elif turns == 2:
            speed[0] *= -1
            speed[1] *= -1
        elif turns == 3:
            temp = speed[0]
            speed[0] = -speed[1]
            speed[1] = temp
    else: 
        x1 += directions[dir][0]*int(i[1:])
        y1 += directions[dir][1]*int(i[1:])
        x2 += int(i[1:])*speed[0]
        y2 += int(i[1:])*speed[1]
print("Answer 1: " + str(abs(x1)+abs(y1)))
print("Answer 2: " + str(abs(x2)+abs(y2)))