with open('input.txt') as fp:
    lines = fp.readlines()

commands = []
for line in lines:
    temp = line.replace("\n", "").split(" ")
    commands.append((temp[0], temp[1]))

rowsExecuted = []
acc = 0
row = 0
while(True):
    if row in rowsExecuted:
        break
    rowsExecuted.append(row)
    command = commands[row]
    if command[0] == "nop":
        row += 1
    elif command[0] == "acc":
        row += 1
        acc += int(command[1])
    elif command[0] == "jmp":
        row += int(command[1])
print("Answer 1: " + str(acc))

row = 0
replaceCount = 0
replaceJmp = True
replaceNop = False
complete = False
while row < len(commands) or not complete:
    rowsExecuted = []
    acc = 0
    row = 0
    nopCount = 0
    jmpCount = 0
    replaced = False
    while(True):
        if row in rowsExecuted:
            break
        if row > len(commands):
            row = 0
            replaceJmp = False
            replaceNop = True
            replaceCount = 0
            break
        if row == len(commands):
            complete = True
            break
        rowsExecuted.append(row)
        command = commands[row]
    
        if replaceJmp and not replaced and jmpCount == replaceCount and command[0] == "jmp":
            command = ("nop", command[1])
            replaced = True
            replaceCount += 1
        elif replaceNop and not replaced and nopCount == replaceCount and command[0] == "nop":
            command = ("jmp", command[1])
            replaced = True
            replaceCount += 1
        if command[0] == "nop":
            nopCount += 1
            row += 1
        elif command[0] == "acc":
            row += 1
            acc += int(command[1])
        elif command[0] == "jmp":
            jmpCount += 1
            row += int(command[1])

print("Answer 2: " + str(acc))