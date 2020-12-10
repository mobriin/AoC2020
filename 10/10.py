with open('input.txt') as fp:
    lines = fp.readlines()

numbers = []
for i in lines:
    numbers.append(int(i))
numbers.sort()

oneDiff = 0
threeDiff = 1
currentVolt = 0
onesInARow = 0
res = 1
for number in numbers:
    if number == currentVolt + 1:
        oneDiff += 1
        onesInARow += 1
    if number == currentVolt + 3:
        threeDiff += 1
        if(onesInARow == 2):
            res *= 2
        elif(onesInARow == 3):
            res *= 4
        onesInARow = 0
    if (onesInARow > 3):
        res *= 7
    currentVolt = number
print("Answer 1: " + str(oneDiff * threeDiff))
print("Answer 2: " + str(res))