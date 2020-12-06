with open('input.txt') as fp:
    lines = fp.readlines()

seatIDs = []

for line in lines:
    rowMin = 0
    rowMax = 127
    for i in range(7):
        if line[i] == "F":
            rowMax = rowMax - (((rowMax - rowMin) + 1)/2)
        elif line[i] == "B":
            rowMin += ((rowMax-rowMin) + 1)/2
    if rowMin != rowMax:
        print("Something went wrong with rows!")
    row = rowMin
    columnMin = 0
    columnMax = 7
    for i in range(3):
        if line[7+i] == "L":
            columnMax = columnMax - (((columnMax - columnMin) + 1)/2)
        elif line[7+i] == "R":
            columnMin += ((columnMax-columnMin) + 1)/2
    if columnMin != columnMax:
        print("Something went wrong with columns!")
    column = columnMin
    seatIDs.append((row * 8) + column)

seatIDs.sort()
print("Highest ID: " + str(seatIDs[-1]))

for i in range(len(seatIDs)):
    if seatIDs[i] + 1 != seatIDs[i+1]:
        print("My seat: " + str(seatIDs[i] + 1))
        break


