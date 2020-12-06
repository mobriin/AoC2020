with open('input.txt') as fp:
    lines = [int(x) for x in fp.read().split()]

i = 0
while i < len(lines):
    y = i + 1
    while y < len(lines):
        if (lines[i] + lines[y] == 2020):
            print("i: " + str(lines[i]) + "\n" + "y: " + str(lines[y]))
            print("Answer 1: " + str(lines[i] * lines[y]))
            break
        y += 1
    i += 1

i = 0
while i < len(lines):
    x = i + 1
    while x < len(lines):
        y = x + 1
        while y < len(lines):
            if (lines[i] + lines[x] + lines[y] == 2020):
                print("i: " + str(lines[i]) + "\n" + "x: " + str(lines[x]) + "\n" + "y: " + str(lines[y]))
                print("Answer 2: " + str(lines[i] * lines[x] * lines[y]))
                break
            y += 1
        x += 1
    i += 1